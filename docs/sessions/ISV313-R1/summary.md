# AWS re:Invent 2025 - 使用AI加速故障排除：OpenSearch中的自然语言查询与语义搜索

## 会议概述

本次会议是一个300级别的技术演讲，由AWS解决方案架构师Ulli（来自柏林）和Rueben Jimenez主讲，专注于CloudOps和可观测性优化。会议展示了如何利用AI技术加速故障排除过程，帮助更快地恢复客户服务、找到问题根因并进行缓解。

演讲者使用基于OpenTelemetry演示应用程序构建的多租户SaaS应用作为案例，该应用部署在Amazon EKS上，通过OpenTelemetry收集器将可观测性数据（日志、指标、追踪）发送到Amazon OpenSearch Service。会议涵盖三个主要AI用例：OpenSearch Dashboards中的自然语言查询生成、语义日志搜索，以及使用模型上下文协议(MCP)的AI代理集成。

## 详细时间线与关键要点

### 0:00-5:00 - 会议介绍与架构概述
- 介绍演讲者背景和会议目标
- 展示多租户SaaS演示应用架构
- 说明基于OpenTelemetry的可观测性数据流
- 介绍将要演示的三个AI用例

### 5:00-15:00 - 演示环境设置与问题发现
- 展示Kubernetes集群中的多租户部署（动物名称作为租户标识符）
- 使用kubectl命令查看命名空间和Pod状态
- 发现客户无法完成购买的关键业务问题
- 通过浏览器开发者工具确认504网关超时错误
- 演示问题复现过程

### 15:00-25:00 - 自然语言查询生成演示
- 进入OpenSearch Dashboards界面
- 展示传统日志分析的挑战（信号与噪声问题）
- 使用AI提示进行自然语言查询："寻找超出速率限制的日志"
- AI自动生成PPL（Piped Processing Language）查询
- 识别共享命名空间中的shipping-rate-limiter问题
- 通过可视化确认"嘈杂邻居"问题（eagle租户过度使用资源）

### 25:00-35:00 - 语义搜索技术深入
- 解释语义搜索与传统词汇搜索的区别
- 介绍Amazon Titan Text Embeddings V2模型
- 展示日志数据的采样技术（每秒10个事件限制）
- 配置OpenSearch Ingestion管道进行日志采样
- 在OpenSearch Dev Tools中设置语义搜索：
  - 创建到Amazon Bedrock的连接器
  - 注册和部署嵌入模型
  - 配置自动嵌入管道

### 35:00-42:00 - MCP集成与自动化修复
- 介绍模型上下文协议(MCP)和Kiro CLI
- 展示Python MCP服务器配置
- 演示通过自然语言与OpenSearch的交互
- AI代理自动识别问题并提供修复建议
- 自动扩展共享服务从1个副本到5个副本
- 验证修复效果：应用程序恢复正常功能

### 42:00-46:00 - 总结与问答
- 提供GitHub Gist链接包含所有代码和文档
- 回答关于OpenSearch与Bedrock跨区域连接的问题
- 解释OpenSearch Dev Tools的标准功能
- 会议总结和反馈收集