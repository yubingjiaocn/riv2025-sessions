# AWS re:Invent 2025 技术会议总结

## 会议概述

本次技术会议由AWS专家Roland Barcia（全球专业技术总监）和Carlos Santana（平台工程师和Kubernetes专家）主讲，重点展示如何将现有的微服务应用与AWS AgentCore和MCP（Model Context Protocol）网关集成，构建智能代理系统。会议通过一个生动的家庭保险场景演示，展现了如何利用EKS集群上运行的现有业务逻辑，通过MCP网关暴露给AI代理使用。

演讲者通过代码实战的方式，详细展示了平台工程师如何配置基础设施，以及代理开发者如何构建和部署智能代理。整个演示涵盖了从EKS集群管理、微服务部署、MCP网关配置到最终用户界面交互的完整流程，为企业级AI代理开发提供了实用的技术方案。

## 详细时间线与关键要点

### 0:00-5:00 开场介绍和场景设定
- Roland和Carlos通过幽默的厨房清洁场景引入主题
- Carlos在跳萨尔萨舞时意外撞坏冰箱，引出保险理赔场景
- 介绍构建AI代理的需求：处理保险理赔、预约维修等业务流程

### 5:00-10:00 架构概览和技术栈介绍
- 展示现有微服务架构：预约服务、客户服务、技师服务等
- 介绍AgentCore组件：Runtime、Identity、Gateway、Memory
- 强调EKS作为容器化应用平台的重要性
- Carlos介绍EKS新功能：Capabilities、Auto Mode、预配置控制平面

### 10:00-15:00 整体架构设计
- 聊天UI作为用户交互界面
- EKS集群运行现有微服务API
- AgentCore Gateway暴露服务并提供安全访问
- AgentCore Identity确保安全的服务访问
- AgentCore Runtime部署代理应用
- Bedrock提供LLM推理能力

### 15:00-25:00 EKS集群和微服务演示
- Carlos展示EKS控制台：1.33版本、Auto Mode启用
- 演示Karpenter自动扩缩容功能和节点池管理
- 展示External DNS、cert-manager等社区插件
- 介绍EKS Community Add-ons的优势
- 演示kubectl命令查看集群状态和部署情况

### 25:00-35:00 微服务API和OpenAPI规范
- 展示三个微服务：appointments、customer、technician
- 演示Swagger UI界面和API文档
- 强调OpenAPI规范对MCP网关的重要性
- 展示如何通过Ingress暴露服务并配置域名
- 介绍External DNS自动配置Route 53记录

### 35:00-45:00 MCP网关配置代码演示
- Carlos展示Python代码创建MCP网关
- 演示IAM角色和Cognito身份验证配置
- 展示如何创建AgentCore Identity服务
- 演示将OpenAPI规范上传到S3并创建网关目标
- 介绍Secrets Manager集成和安全最佳实践

### 45:00-50:00 代理开发和部署
- Roland展示代理开发代码
- 演示SSM参数获取和MCP客户端创建
- 展示使用装饰器模式刷新访问令牌
- 演示Strands SDK创建AI代理
- 展示AgentCore Runtime中的代理部署

### 50:00-53:30 实时演示和总结
- 成功演示完整的用户交互流程
- 代理自动创建保险理赔单并安排紧急维修预约
- 展示代理的推理能力和多轮对话功能
- 提供资源链接和后续会议信息
- 强调现有系统现代化和安全最佳实践的重要性