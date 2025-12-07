# AWS re:Invent 2025 DAT410 会议总结：PostgreSQL 性能调优实战

## 会议概述

本次会议（DAT410）主题为"PostgreSQL 性能：真实工作负载调优"，由 AWS RDS 和 Aurora PostgreSQL 高级数据库工程师 Bajishek 和数据库技术负责人 Vlad Blash Chana 主讲。会议通过一个电商应用的实际案例，演示了如何诊断和解决常见的 PostgreSQL 性能问题。

演讲者以一个虚拟角色 John（高级数据库工程师）的困境开场——尽管他正确配置了数据库并设置了监控告警，但随着数据增长，仍在凌晨 3 点收到性能告警。会议通过修复五个关键性能问题，展示了系统化的查询调优方法论。整个演示使用了一个运行超过 150 个并发连接的电商负载生成器，包含订单、产品和用户等表，通过 Performance Insights 和 Database Insights 实时监控性能改进效果。

会议强调了性能调优的迭代过程：从 Performance Insights 识别活跃会话和 CPU 消耗，查看 pg_stat_activity 视图，生成带有 buffers 选项的 EXPLAIN ANALYZE 计划，然后逐步优化。通过五个实际案例，演示了如何将查询执行时间从 1 分钟降至 800 毫秒，并在相同硬件上将总查询吞吐量从 15,000 提升至 20,000。

## 详细时间线与关键要点

### 开场与背景介绍
时间戳：开始
- 会议代号 DAT410，主题为 PostgreSQL 性能真实工作负载调优
- 提出核心问题：是否曾因数据库性能下降（高 CPU、查询执行时间长、执行计划切换）在凌晨 3 点收到告警
- 介绍演讲者：Bajishek（RDS/Aurora PostgreSQL 高级数据库工程师）和 Vlad（数据库技术负责人）

### 性能调优关键领域
时间戳：约 3-5 分钟
- **CPU 利用率**：次优查询导致全表扫描、工作负载与实例规模不匹配、并行查询过多
- **内存**：内存密集型查询、基于进程的架构（每个连接消耗内存）、内存参数配置过高
- **存储和 IOPS**：MVCC 机制产生的膨胀（bloat）、未使用或重复的索引、work_mem 不足导致临时文件写入磁盘
- **应用模式**：查询相互阻塞、长事务或空闲事务、过多空闲连接（连接池可优化）

### 查询调优方法论
时间戳：约 5-7 分钟
- 步骤化流程：查看 Performance Insights 的活跃会话摘要或 pg_stat_activity 视图
- 识别消耗资源的 Top SQL 和等待事件
- 生成带 buffers 选项的 EXPLAIN ANALYZE 计划
- 这是一个迭代过程，需要持续识别和修复 Top SQL

### EXPLAIN ANALYZE 计划解读
时间戳：约 7-10 分钟
- 计划节点结构：每个箭头代表一个计划节点，顶行是所有节点的汇总
- 两部分信息：
  - **估算值**：启动成本、总成本、预估行数、平均行宽度
  - **实际值**：实际启动时间（毫秒）、总时间（毫秒）、实际行数、循环次数
- 关键指标：执行时间、行数、循环次数、缓冲区读取

### 演示环境设置
时间戳：约 10-12 分钟
- 电商应用：包含 orders、products、users 表
- 负载生成器：超过 150 个连接，读写平衡，每 30 秒提供查询摘要
- 监控工具：Performance Insights、Database Insights、CloudWatch 指标

### 问题 1：函数调用导致的全表扫描
时间戳：约 12-25 分钟
- **问题识别**：函数调用 get_sale_movement_count() 消耗大量 CPU
- **根本原因**：函数内部查询使用 movement_type = get_movement_type() 作为过滤条件，优化器不知道函数返回值，对 1100 万行执行全表扫描
- **关键指标**：
  - 执行时间：约 60 秒
  - Rows removed by filter：1000 万行
  - Shared buffer hits：87,000 个 8KB 块（约 800MB）
  - 尽管存在 movement_type 索引，仍进行顺序扫描
- **解决方案**：将函数调用改写为 SELECT 子查询：movement_type = (SELECT get_movement_type())
- **改进效果**：
  - 执行时间：从 60 秒降至 800 毫秒
  - Shared buffer hits：从 87,000 降至 2,800 块
  - 成本：从 300 万降至 43,000
  - 函数调用次数：从每 30 秒 9 次提升至 12 次，后续持续改善
  - Commit latency：从 23 降至 21

### 问题 2：部分索引优化
时间戳：约 25-35 分钟
- **问题识别**：查询获取特定类别活跃产品的平均价格，使用 bitmap index scan
- **根本原因**：
  - Rows removed by filter：30,000 行
  - Shared buffer hits：13,800 块
  - 只有 33% 的产品是活跃状态，但索引包含所有产品
- **解决方案**：创建部分索引（partial index）：
 sql
  CREATE INDEX CONCURRENTLY idx_category_active 
  ON products(category) 
  WHERE is_active = true
  
- **改进效果**：
  - 执行时间：从 360 毫秒降至 23 毫秒
  - Rows removed by filter：从 30,000 降至 900
  - Shared buffer hits：从 13,000 降至 10,000
  - 查询吞吐量：从 1,200 提升至 2,000（100% 改进）
  - 总体查询数：从 15,000 提升至 20,000
- **Q&A 讨论**：为什么不使用复合索引？因为复合索引仍包含非活跃产品，部分索引更精准

### 问题 3：查询提示（Hint）导致的错误索引选择
时间戳：约 35-50 分钟
- **问题识别**：查询使用 pg_hint_plan 扩展强制使用 created_at 单列索引
- **根本原因**：
  - 查询有两个谓词：created_at 和 total_amount
  - 已存在复合索引 (created_at, total_amount)，但提示强制使用单列索引
  - Rows removed by filter：400,000 行
  - Shared buffer hits：400,800 块
- **长期解决方案**：删除查询中的提示，让优化器自动选择复合索引
- **短期解决方案**：使用 Aurora 的 Query Plan Management (QPM) 扩展切换执行计划
  - 创建 apg_plan_mgmt 扩展（需要重启实例）
  - 扩展捕获所有查询计划到 dba_plans 表
  - 执行删除提示的查询，捕获新计划（使用复合索引）
  - 使用 aurora_stat_plans() 函数查看实时计划使用情况
  - 使用 set_plan_status() 函数批准新计划、拒绝旧计划
- **改进效果**：
  - Rows removed by filter：降至 0
  - Shared buffer hits：从 400,000 降至 37,000
  - 计划自动切换，无需修改应用代码
- **Q&A 讨论**：
  - QPM 扩展仅适用于 Aurora PostgreSQL（不适用于 RDS）
  - AWS 正在努力确保扩展的前向兼容性，但目前尚未完全保证

### 问题 4：堆仅元组（Heap-Only Tuple）更新优化
时间戳：约 50 分钟后（提及但未详细演示）
- 会议提到这是第四个性能问题，涉及 HOT 更新如何提升性能
- 未在演示中详细展开

### 问题 5：轻量级日志分析
时间戳：约 50 分钟后（提及但未详细演示）
- 会议提到存在一些轻量级日志需要分析和修复
- 未在演示中详细展开

### 监控和验证
时间戳：贯穿整个演示
- **Performance Insights**：显示 CPU 等待事件占主导，60-70 个会话消耗 CPU
- **Database Insights**：Performance Insights 的扩展版本，提供更详细的 SQL 分析
- **CloudWatch 指标**：
  - CPU 利用率：接近 100%
  - Commit latency：从 23 降至 21
  - Queries finished：持续改善
  - Total query time：从 500 万降至 52.5 万
- **负载生成器输出**：每 30 秒显示 8 个查询的执行次数和聚合统计

### 关键技术要点
时间戳：贯穿整个会议
- **EXPLAIN ANALYZE 分析重点**：
  - 错误的行数估算（统计信息过时）
  - 顺序扫描（应使用索引）
  - 高 buffer reads
  - Rows removed by filter（表示不必要的工作）
  - 识别慢操作的计划节点
- **索引扫描类型**：
  - Index Scan：逐行从索引获取
  - Bitmap Index Scan：批量获取行，减少迭代次数，某些场景下更高效
- **最佳实践**：
  - 在谓词中使用函数时添加 SELECT 子查询
  - 根据数据分布创建部分索引
  - 避免过度使用查询提示
  - 定期监控未使用的索引
  - 使用 CONCURRENTLY 选项创建索引以避免锁定

### 观众问答要点
时间戳：贯穿整个会议
- 为什么优化器不自动内联函数调用？这是优化器的工作方式，需要显式子查询
- 为什么不使用复合索引而用部分索引？部分索引更精准，避免包含不需要的数据
- 如何平衡索引数量？过多索引会降低写入性能，需要持续监控未使用的索引
- 如何识别需要优化的查询？查看 "rows removed by filter" 高的查询
- 这些技术适用于 RDS 和 Aurora 吗？大部分适用，但 QPM 扩展仅限 Aurora
- 扩展的前向兼容性？AWS 正在努力，但目前未完全保证

### 总结
时间戳：会议结尾
- 通过五个实际案例展示了系统化的性能调优方法
- 在不改变硬件的情况下，将查询吞吐量提升 33%（15,000 → 20,000）
- 强调持续监控和迭代优化的重要性
- 演示了 AWS 工具（Performance Insights、Database Insights、QPM）在实际调优中的应用