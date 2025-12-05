# AWS re:Invent 2025 会议总结：使用 AI 加速故障排查

## 会议概述

本次 AWS re:Invent 2025 的 300 级技术会议重点探讨了如何利用 AI 技术提升故障排查效率。演讲者 Ulie（来自柏林的解决方案架构师）和 Ruben Jimenez（专注于云运维和可观测性的高级解决方案架构师）通过实际演示，展示了如何在 Amazon OpenSearch Service 中集成 AI 能力，帮助运维团队更快地恢复服务、定位根本原因并缓解问题。

会议使用了一个基于 OpenTelemetry 演示应用改造的多租户 SaaS 应用作为示例。该应用部署在 Amazon EKS 上，模拟了一个在线商店系统，包含多个微服务（如购物车、产品目录、结账、配送等）。演示环境包含 10 个租户（以动物名称命名）和共享服务，所有可观测性数据（日志、指标、追踪）通过 OpenTelemetry Collector 收集并经由 OpenSearch Ingestion 导入 Amazon OpenSearch Service。

会议涵盖了三个核心 AI 应用场景：自然语言查询生成、语义日志搜索，以及通过模型上下文协议（MCP）实现的 AI 代理集成。所有演示代码和配置都将通过 GitHub Gist 提供，方便参会者后续深入学习。

## 详细时间线与关键要点

### 开场介绍（开始）
- **会议定位**：300 级代码实战会议，重点展示实际操作而非逐行代码讲解
- **演讲者介绍**：Ulie 和 Ruben 均为 AWS 高级解决方案架构师，专注于 SaaS 客户和 OpenSearch 社区
- **资源承诺**：所有代码片段、参考资料将通过 GitHub Gist 提供

### 演示应用架构介绍
- **应用基础**：基于 OpenTelemetry 演示应用（开源项目）改造的多租户网店系统
- **多租户设计**：10 个租户实例 + 共享服务层，模拟真实 SaaS 架构模式
- **技术栈**：
  - 运行环境：Amazon EKS (Kubernetes)
  - 数据收集：OpenTelemetry Collector
  - 数据处理：OpenSearch Ingestion (ETL 工具)
  - 数据存储：Amazon OpenSearch Service
  - 可视化：OpenSearch Dashboards

### 问题场景设定
- **故障描述**：CEO 报告所有客户的网店无法完成购买，用户可以浏览和添加商品到购物车，但无法结账
- **初步排查**：通过 kubectl 命令检查 Kubernetes 集群状态，表面上所有服务运行正常
- **问题复现**：使用 kubectl port-forward 将 Falcon 租户应用映射到本地，访问 localhost:8080 测试
- **错误确认**：浏览器开发者控制台显示结账请求超时，返回 504 Gateway Timeout 错误

### 第一部分：自然语言查询生成
- **工具使用**：OpenSearch Dashboards 的 AI 辅助查询功能
- **挑战描述**：面对海量日志数据（每分钟数千条），手动编写查询语句耗时且需要专业知识
- **AI 提示词**：输入自然语言描述"查找超出速率限制的日志"
- **AI 响应**：
  - 自动生成 PPL (Piped Processing Language) 查询语句
  - 筛选出相关日志条目
  - 识别出 "Rate limit exceeded" 错误
  - 定位到共享命名空间中的 shipping service
- **根因分析**：AI 总结指出配送速率限制器可能影响下游流程，建议检查高流量租户
- **可视化演示**：
  - 使用自然语言生成租户活动可视化图表
  - 图表清晰显示 Eagle 租户活动异常高
  - 确认"嘈杂邻居"（noisy neighbor）问题：Eagle 租户过度使用共享服务导致其他租户受影响

### 第二部分：语义日志搜索
- **技术背景**：
  - 传统词法搜索：基于关键词精确匹配
  - 语义搜索：基于含义匹配，无需知道确切关键词
- **实现架构**：
  - 使用 Amazon Bedrock 的 Titan Text Embeddings v2 模型
  - 向量嵌入：将文本转换为浮点数数组，编码语义信息
- **日志数据特殊性**：
  - 挑战：日志量大，无法对每条日志都进行嵌入（成本高）
  - 优势：日志内容重复性高，语义相似
  - 解决方案：采样技术（每个服务每秒仅处理 10 条日志）

### OpenSearch 配置实战
- **采样管道配置**：
  - 在 OpenSearch Ingestion 中创建采样子管道
  - 使用 rate limiter 限制每服务每秒 10 个事件
  - 将采样日志存入独立索引 sampled-logs
- **连接 Amazon Bedrock**：
  1. 创建 Bedrock 连接器，指定嵌入模型
  2. 创建模型组并注册模型
  3. 部署模型到 OpenSearch 域
  4. 测试模型预测功能
- **索引配置**：
  - 创建 ingest pipeline 自动处理日志嵌入
  - 定义索引模板，添加 body_embedding 向量字段
  - 删除并重建索引以应用新配置
- **语义搜索演示**：
  - 查询："something is taking too long"（某些东西耗时太长）
  - 结果：成功找到 "Rate limit exceeded request queued" 日志
  - 关键点：查询词与日志内容词法上完全不同，但语义相关

### 第三部分：模型上下文协议（MCP）集成
- **技术框架**：
  - 客户端：Kiro CLI（AWS AI 代理工具）
  - 服务端：自定义 Python MCP 服务器
  - 功能：整合自然语言查询和语义搜索能力
- **MCP 服务器配置**：
  - 使用 boto3 连接 AWS 服务
  - 使用 fast-MCP 框架构建服务器
  - 配置 OpenSearch 连接（endpoint、region、credentials）
  - 使用 SigV4 认证访问 OpenSearch
  - 集成 Python OpenSearch 客户端
- **代理能力**：
  - 通过自然语言提示与 OpenSearch 交互
  - 自动执行语义搜索
  - 不仅诊断问题，还能协助缓解措施

### 技术要点总结
- **成本优化**：通过采样技术大幅降低 AI 模型调用成本
- **实用性**：无需记忆确切日志格式或关键词即可搜索
- **集成性**：OpenSearch 原生支持向量搜索和 AI 模型集成
- **可扩展性**：MCP 协议支持构建自定义 AI 代理工具链

### 资源与后续
- **GitHub Gist**：包含完整代码、配置和详细说明
- **适用场景**：多租户 SaaS 应用、EKS 集群运维、大规模日志分析
- **最佳实践**：结合传统查询、AI 辅助和语义搜索的混合故障排查方法