# AWS re:invent 2025 - Amazon Aurora 和 Amazon RDS 性能与成本优化

## 会议概述

本次技术会议由 AWS 数据库解决方案架构师 Penny Debas 主讲,深入探讨了 Amazon Aurora 和 Amazon RDS 的性能优化与成本控制策略。会议通过一个虚构公司"Any Company"的实际案例,展示了如何解决数据库环境中最常见的性能瓶颈和成本挑战。

Any Company 是一家利用生成式 AI 赋能电商卖家的初创公司,使用 Amazon EKS 作为应用层,Amazon RDS 作为运营数据库。作为快速成长的初创企业,他们面临着在工作负载扩展过程中平衡性能需求与成本控制的典型挑战。会议系统性地介绍了三个主要成本维度:计算(Compute)、存储(Storage)和备份(Backup),并通过实际案例演示了如何使用 CloudWatch Database Insights 等可观测性工具识别问题,以及如何通过 SQL 优化、实例右sizing、读副本、优化读取(Optimized Reads)等技术手段实现性能提升和成本降低。

会议还特别强调了 Amazon Aurora 的独特架构优势,包括其云原生存储层设计、Aurora I/O-Optimized 定价模式,以及 Aurora Serverless 的自动扩展能力,为处理突发性工作负载提供了更具成本效益的解决方案。

## 详细时间线

### 开场与背景介绍
[00:00:00 - 00:03:30] 
- 会议开场,介绍演讲者 Penny Debas(AWS 数据库解决方案架构师)
- 介绍虚构客户案例"Any Company"及其业务背景
- 说明会议目标:提供可直接应用于数据库环境的可操作性见解

### Amazon RDS 服务概述
[00:03:30 - 00:06:00]
- Amazon RDS 基础介绍:全托管关系数据库服务
- 支持商业引擎和开源引擎
- Amazon Aurora 特别介绍:云原生数据库引擎,兼容 MySQL 和 PostgreSQL
- 说明本次会议不涵盖 Aurora DSQL(架构和定价模式完全不同)

### RDS 成本维度分析
[00:06:00 - 00:08:00]
- 介绍 RDS 的主要成本维度:计算、存储、备份、数据传输、IOPS
- 确定本次会议重点:计算、存储和备份三个维度

### 挑战一:CPU 使用率飙升与 SQL 优化
[00:08:00 - 00:15:00]
- **问题描述**:Any Company 的 CPU 使用率因低效 SQL 语句飙升至 100%
- **关键问题**:如何识别和解决问题 SQL?什么是正确的实例类型?
- 介绍 AWS 实例类型选择:可突增型(Burstable)、通用型(General Purpose)、内存优化型(Memory Optimized)、Graviton(基于 ARM 架构,性价比更高)

### CloudWatch Database Insights 演示
[00:15:00 - 00:22:00]
- 介绍 CloudWatch Database Insights:数据库可观测性的统一界面
- **实时演示**:
  - 舰队级视图(Fleet-level view)展示所有实例
  - 识别 Any Company 实例的数据库负载警告
  - 发现问题 SQL:customers 和 payments 表之间的 JOIN 查询
  - 查看执行计划:并行顺序扫描(parallel sequential scans),缺少索引
  - **解决方案**:在 payments 表的 amount 和 customer_id 字段创建索引
  - **结果**:查询时间从 30 秒降至 46 毫秒,CPU 利用率从 90%+ 降至 11%

### 实例右sizing与成本优化
[00:22:00 - 00:24:30]
- SQL 优化后进行实例降级:从 R6G.2xlarge 降至 R6G.xlarge(vCPU 和内存减半)
- 同时升级到最新 Graviton 4 代(R8A),获得更好的性价比
- **成果**:实例成本降低 46%,平均 CPU 利用率降低 70%

### 挑战二:嘈杂邻居问题(Noisy Neighbors)
[00:24:30 - 00:28:00]
- **问题描述**:数据分析师运行报表查询影响核心 API 性能
- **解决方案对比**:
  - 垂直扩展(Vertical Scaling):从 R8A.xlarge 升至 R8A.2xlarge,计算成本翻倍
  - 水平扩展(Horizontal Scaling):使用读副本(Read Replicas),可创建最多 15 个不同大小的副本
- 选择使用 R8A.large 读副本处理报表查询,成本显著降低
- **成果**:核心 API 性能提升 50%,无需增加主实例成本

### 缓存策略讨论
[00:28:00 - 00:29:30]
- 介绍 Amazon ElastiCache 作为替代方案
- Write-through 策略:更新数据库时同步更新缓存
- 提供微秒级延迟,但 Any Company 因查询多为动态过滤的 ad-hoc 查询而未采用

### 存储类型介绍
[00:29:30 - 00:32:00]
- **GP2**:IOPS 与存储容量绑定(1:3 比例)
- **GP3**:IOPS 和吞吐量可独立于存储大小配置
- **IO1/IO2 Block Express**:适用于关键任务应用
  - IO2 是 RDS 中唯一提供亚毫秒级 IO 延迟的 EBS 选项
  - IO2 提供 99.999% 耐久性,比 IO1 高 100 倍
  - IO2 与 IO1 价格相同,建议立即升级(低垂果实,无停机时间)

### 挑战三:EBS IO 延迟问题
[00:32:00 - 00:34:00]
- **问题描述**:IO 延迟从 2 毫秒飙升至 500 毫秒,达到 EBS IOPS 限制
- **需求**:支持 20K IOPS 和亚毫秒级 IO 延迟
- CloudWatch Database Insights 识别出 EBS IOPS 增加和 IO 延迟飙升
- **解决方案**:迁移至 IO2 Block Express
- **成果**:实现稳定的亚毫秒级 IO 延迟

### 挑战四:慢报表查询与临时对象
[00:34:00 - 00:39:00]
- **问题描述**:读副本上的复杂报表查询(JOIN、聚合、GROUP BY)生成大量临时对象,仪表板加载时间 10 秒
- **需求**:将仪表板加载时间降至 5 秒以内
- **根本原因**:临时对象写入 EBS 卷导致 IO 延迟
- CloudWatch Database Insights 识别:
  - IO:BufFileWrite 等待事件(紫色)
  - 数据库遥测显示 temp files 和 temp bytes per second 指标异常
- **解决方案**:使用 RDS Optimized Reads
  - 利用带本地 NVMe SSD 的实例类型(实例名称以"D"结尾,如 R8GD、M8GD)
  - 临时对象处理从 EBS 转移到本地 NVMe SSD
- **成本对比**:
  - 垂直扩展至 R8A.xlarge:成本翻倍
  - 使用 R8A.large-D:成本显著更低
- **成果**:仪表板加载时间提升 2 倍(100% 改进)

### 备份成本优化
[00:39:00 - 00:43:00]
- **RDS 备份类型**:
  - 自动备份:每日 EBS 快照 + 每 5 分钟事务日志,支持 35 天内的时间点恢复
  - 数据库快照:手动创建,无过期时间,适合长期保留
- **挑战五**:Any Company 保留 1 个月备份数据,但实际只需 1 周数据可恢复,其余仅用于合规查询
- **长期备份方案**:
  - 快照导出至 S3(Snapshot Export to S3):完整或部分导出为 Parquet 格式,可用 Amazon Athena 查询
  - 逻辑备份至 S3:使用 pg_dump(PostgreSQL)或 MySQL Shell Dump
  - 优势:可控制 S3 存储类别(标准、Glacier 等)
- **成本对比**:
  - 原方案(30 天自动备份):初始 500GB 免费,每日增量备份收费
  - 优化方案(7 天自动备份 + Parquet 导出):总成本大幅降低
- **成果**:备份成本降低 30%

### RDS 优化总结
[00:43:00 - 00:45:00]
- SQL 优化 + 实例右sizing + Graviton 4:实例成本降低 46%
- 读副本分离工作负载:核心 API 响应时间降低 50%
- IO2 Block Express:IO 延迟降至亚毫秒级
- Optimized Reads:仪表板加载时间提升 2 倍
- 备份策略优化:备份成本降低 30%

### Amazon Aurora 架构介绍
[00:45:00 - 00:48:00]
- Aurora 是云原生数据库引擎,完全兼容 MySQL 和 PostgreSQL
- Aurora 家族:
  - Aurora Provisioned(实例型):适用于可预测工作负载
  - Aurora Serverless:适用于突发和不可预测工作负载,自动扩展
  - Aurora DSQL:最新成员,几乎无限扩展,完全无服务器(本次不涵盖)
- 本次重点:Aurora Provisioned 和 Aurora Serverless

### Aurora 存储层架构
[00:48:00 - 00:52:00]
- **关键创新**:存储层与数据库实例解耦
- Aurora 存储舰队:
  - 多租户存储舰队,跨 3 个可用区分布
  - 由大量专用节点组成,负责存储、平衡、修复等操作
  - 在 3 个可用区创建 6 个数据副本(每个可用区 2 个副本)
  - **仅按 1 个副本收费**
- 可承受整个可用区不可用 + 1 个额外存储节点故障

### Aurora 挑战一:增长与突发工作负载
[00:52:00 - 00:55:00]
- **问题描述**:客户增长 + 突发流量(如特定地区醒来、Taylor Swift 演唱会门票开售)
- **需求**:自动驾驶式扩展 + 成本可预测性 + 降低 IO 成本

### Aurora 存储定价模型
[00:55:00 - 00:58:00]
- **按使用付费**,两个维度:
  1. **存储大小**:按 GB/月计费,无需预配置,自动增长和收缩
     - 可通过删除未使用分区、VACUUM 等操作控制存储
     - 使用 CloudWatch 的 VolumeBytesUsed 指标监控
  2. **存储 IO**:按百万次 IO 操作计费
     - 读取:每页读取计为 1 次 IO
     - 写入:以 4KB 为单位(Aurora 写入日志而非页面)
- IO 自动可扩展,无需预定义 IOPS
- 添加更多副本时,所有副本共享同一存储层

### Aurora 成本示例与突发 IO 挑战
[00:58:00 - 01:01:00]
- **场景**:100GB 存储,每天增长 100MB,600 IOPS(400 读 + 200 写)
- 使用 R8A.xlarge 实例
- **常规 IO 成本**:约 $27/月
- **突发 IO 挑战**:每天 2 小时 15,000 IOPS
- **突发 IO 成本**:$648/月(成本显著增加)

### Aurora I/O-Optimized 定价模式
[01:01:00 - 01:04:30]
- **问题**:突发 IO 导致成本不可预测
- **解决方案**:Aurora I/O-Optimized
  - 计算成本提高约 30%
  - **IO 成本为零**(无论 IO 量多大)
  - 适用于 IO 密集型和不可预测工作负载
- **成本对比**:
  - 标准模式(含突发 IO):$1,275/月
  - I/O-Optimized 模式:$828/月
- **成果**:月度成本降低 35%,成本可预测性提高

### Aurora 挑战二:全球扩展
[01:04:30 - 01:06:00]
- **问题描述**:Any Company 扩展至欧洲和亚洲,需要低延迟全球访问
- **需求**:跨区域复制 + 快速故障转移 + 灾难恢复

### Aurora Global Database
[01:06:00 - 01:08:30]
- **功能**:
  - 跨多个 AWS 区域复制数据
  - 次区域的复制延迟通常 < 1 秒
  - 支持最多 5 个次区域
  - 每个次区域最多 16 个读副本
  - 快速故障转移:RTO < 1 分钟
- **成本**:仅为跨区域数据传输付费,无额外许可费用
- **成果**:全球用户延迟降低 60%,实现灾难恢复能力

### Aurora Serverless 介绍
[01:08:30 - 01:11:00]
- **挑战三**:开发/测试环境成本高,夜间和周末无使用但仍在运行
- **Aurora Serverless 特性**:
  - 自动启动、关闭和扩展
  - 按 Aurora Capacity Units (ACUs) 计费
  - 1 ACU = 约 2GB RAM + 对应 CPU 和网络
  - 可设置最小和最大 ACU
  - 空闲时自动暂停,恢复时间几秒钟
- **使用场景**:开发/测试环境、不频繁使用的应用、不可预测工作负载

### Aurora Serverless 成本示例
[01:11:00 - 01:13:00]
- **场景**:开发环境,工作日 8 小时使用,夜间和周末暂停
- **Aurora Provisioned**:db.r6g.large 全天候运行 = $175/月
- **Aurora Serverless**:
  - 最小 0.5 ACU,最大 16 ACU
  - 仅工作时间运行
  - 成本:$35/月
- **成果**:开发环境成本降低 80%

### Aurora Serverless v2 高级功能
[01:13:00 - 01:15:00]
- 即时扩展(秒级),无连接中断
- 可与 Aurora Provisioned 实例混合使用
- 支持所有 Aurora 功能(Global Database、读副本等)
- 细粒度扩展:以 0.5 ACU 为增量

### Aurora 优化总结
[01:15:00 - 01:17:00]
- I/O-Optimized 定价:月度成本降低 35%,成本可预测
- Aurora Global Database:全球延迟降低 60%,实现 DR 能力
- Aurora Serverless:开发环境成本降低 80%

### 最佳实践与建议
[01:17:00 - 01:20:00]
- 使用 CloudWatch Database Insights 进行统一可观测性
- 优先优化 SQL 查询,再考虑扩展实例
- 利用 Graviton 实例获得更好性价比
- 根据工作负载特征选择合适的存储类型
- 使用读副本分离不同工作负载
- 考虑 Optimized Reads 处理临时对象密集型查询
- 优化备份策略,使用 S3 存储长期归档数据
- 对于突发工作负载,考虑 Aurora I/O-Optimized 或 Serverless
- 全球应用使用 Aurora Global Database
- 开发/测试环境使用 Aurora Serverless

### 会议总结与问答
[01:20:00 - 结束]
- 回顾 Any Company 的完整优化旅程
- 强调性能优化与成本控制并非对立,而是相辅相成
- 鼓励参会者应用这些策略到自己的数据库环境
- 开放问答环节