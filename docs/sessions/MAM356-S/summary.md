# AWS re:Invent 2025 技术会议总结：Fortive BRAIN AI平台构建

## 会议概述

本次技术会议由Capgemini美洲云卓越中心的Scott Warren和AWS全球技术领导者Cedric Bordonne共同主讲，重点介绍了为工业技术公司Fortive构建的AI概念验证项目"Fort BRAIN"。Fortive是一家总部位于华盛顿州埃弗里特的工业技术公司，拥有18,000名全球员工，在50个国家开展业务，主要专注于工作场所安全、医疗保健和环境安全等领域。

该项目的核心目标是为Fortive旗下多个独立运营的子公司(OpCos)构建一个统一、安全、标准化的聊天机器人平台，能够处理结构化数据、非结构化数据和软件工程数据。项目最大的创新在于从静态数据处理转向动态数据处理，通过AWS服务实现了8周内完成POC开发，并展示了如何利用最新的AWS Kiro服务进一步加速开发流程。

## 详细时间线与关键要点

### 0:00-5:00 会议开场与Fortive公司介绍
- Scott Warren介绍会议议程和技术困难解决
- Fortive公司背景：工业技术公司，18,000员工，50个国家运营
- 三大业务支柱：智能运营解决方案、精密技术、医疗保健解决方案
- 创新中心"Fort"孵化了BRAIN项目概念

### 5:00-10:00 BRAIN项目需求分析
- 多种数据源类型：结构化数据(Postgres、SQL、Oracle、Snowflake)、非结构化数据(SharePoint、Jira)、软件工程数据(GitHub、Atlassian)
- 核心挑战：从静态转向动态数据处理
- 项目要求：集中化平台、安全治理、实时数据访问、标准化API

### 10:00-15:00 架构设计与AWS服务选择
- Cedric介绍8周POC目标：支持三种数据源类型、快速响应、对话式交互
- 前端：Fargate容器化Web应用，CloudFront和WAF提供安全性
- 后端：API Gateway和Lambda进行请求编排
- 代理架构：SQL查询代理和操作组代理
- 数据源连接：PostgreSQL和GitHub通过MCP服务器，SharePoint通过Bedrock知识库

### 15:00-20:00 MCP协议与动态数据处理
- Model Context Protocol(MCP)实现动态数据访问
- MCP不仅支持查询，还支持与外部系统交互
- SharePoint使用Amazon Bedrock知识库和OpenSearch向量数据库
- 演示三种数据源的实际应用场景

### 20:00-26:00 未来发展与AWS Kiro集成
- 下一步计划：添加更多数据源类型、实施AgentCore服务
- AWS Kiro集成测试：
  - 快速创建测试数据库
  - 自动生成MCP服务器代码
  - 自动化测试流程
  - 复杂业务查询处理
- 项目成果：8周内完成POC，证明了快速构建企业级AI平台的可行性