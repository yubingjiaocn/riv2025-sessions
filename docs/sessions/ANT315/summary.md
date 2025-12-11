# AWS re:Invent 2025 - 使用Amazon OpenSearch Service实现智能可观测性和现代化

## 会议概述

本次技术分享由Amazon OpenSearch Service高级专家解决方案架构师Sohaib Katariwala和产品经理Joshua Bright主讲，重点介绍了如何使用Amazon OpenSearch Service构建智能可观测性平台。会议通过虚构公司Any Company的案例，展示了现代微服务架构面临的可观测性挑战，包括微服务复杂性、数据管道混乱、开发者生产力低下和成本管理困难等问题。

演讲者详细介绍了OpenSearch Service的完整生态系统，从数据收集、转换、存储到可视化分析的全流程解决方案。特别强调了2024-2025年推出的新功能，包括下一代OpenSearch UI、增强的管道处理语言(PPL)功能，以及基于模型上下文协议(MCP)的AI代理集成。会议展示了如何通过AI代理实现自动化根因分析，将传统需要数小时的故障排查时间缩短至几分钟。

## 详细时间线与关键要点

### 00:00-05:00 会议开场与Any Company案例介绍
- 介绍演讲者和会议主题：智能可观测性和现代化
- 提出Any Company虚构案例：快速增长的电商平台
- 架构包含React前端、微服务后端、EKS容器化服务
- 四大挑战：微服务复杂性、数据管道混乱、开发者生产力、成本管理

### 05:00-15:00 可观测性平台基础概念
- 解释分布式系统可观测性的重要性
- 介绍AWS可观测性服务生态：CloudWatch、Prometheus、OpenSearch Service
- OpenSearch开源项目发展：13亿次下载，3400+贡献者，28个版本
- Amazon OpenSearch Service托管服务优势

### 15:00-25:00 数据收集与处理架构
- OpenTelemetry数据收集机制
- Amazon OpenSearch Ingestion数据缓冲和转换
- 数据存储分层策略：热层、温层、S3冷存储
- OpenSearch Dashboards用户体验介绍

### 25:00-35:00 可视化分析与监控功能
- 服务地图和追踪组可视化
- 异常检测和告警配置
- 多租户支持和权限管理
- 跨多个OpenSearch部署的数据管理挑战

### 35:00-45:00 新一代OpenSearch UI功能演示
- Joshua Bright介绍2024-2025年新功能
- 简化日志分析方法：优先用户体验而非复杂功能
- 开箱即用的蓝图模板：ALB日志、CloudTrail、Lambda等
- 增强的管道处理语言(PPL)：join、lookup、时间分析命令

### 45:00-52:00 AI代理集成演示
- 模型上下文协议(MCP)架构介绍
- 使用Amazon Q Developer CLI(现称Kiro CLI)的实时演示
- Black Friday故障场景：自动根因分析
- AI代理自动关联日志、指标、追踪和业务数据

### 52:00-57:00 总结与资源推荐
- AI代理优势：8分钟完成传统需数小时的分析
- 事故影响减少70-80%
- 推荐后续学习资源：ANT-330 Chalk Talk、技术博客、AWS Skill Builder
- 会议总结和问答环节