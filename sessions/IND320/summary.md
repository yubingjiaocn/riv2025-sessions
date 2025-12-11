# AWS re:Invent 2025 - Toyota 生成式AI与智能代理平台技术分享

## 会议概述

本次技术分享由AWS全球解决方案架构师Bryan Landes主持，联合Toyota Motor North America (TMNA)的Stephen Ellis和Toyota Connected North America的Stephen Short，深入探讨了Toyota在经销商数字化客户体验中的生成式AI应用。会议重点介绍了Toyota如何利用AWS的AgentCore平台构建智能代理系统，从传统的RAG实现演进到更先进的智能代理架构。

Toyota与AWS已合作超过7年，在多个业务线部署了47个不同的AI用例。本次分享特别聚焦于经销商产品信息查询系统，该系统目前每月处理超过7000次交互，帮助经销商更好地回答客户关于车辆规格、定价和配置的专业问题。会议展示了从Version 1的RAG系统到Version 2智能代理平台的技术演进路径。

## 详细时间线与关键要点

### 00:00-05:00 开场介绍与AWS生成式AI技术栈
- Bryan Landes介绍会议背景，强调Toyota在AWS平台上的深度合作
- 展示AWS生成式AI技术栈：从基础设施层(P4/P5 GPU、SageMaker)到应用层(Bedrock、Nova、Strands框架)
- 介绍AgentCore服务：提供可组合的基础设施单元，支持大规模智能代理部署

### 05:00-10:00 智能代理在汽车行业的应用场景
- 智能代理已部署在汽车制造业的多个业务线：软件定义车辆、车载助手、智能制造、产品工程
- 强调平台工程的重要性：通过集中化平台实现DevOps规模化
- 介绍内部开发平台(IDP)如何与智能代理框架集成，实现安全可控的大规模部署

### 10:00-15:00 AWS与Toyota合作历程
- Bryan分享7年合作经验，Toyota从小规模云应用发展到47个AI用例
- 涵盖Toyota全球业务：北美、日本总部、Toyota Connected、Woven by Toyota、NASCAR赛车队
- 强调持续创新和共同构建的合作模式

### 15:00-25:00 Toyota企业AI团队架构与策略
- Stephen Ellis介绍TMNA企业AI团队的独特结构：以工程师为主的卓越中心
- 三大核心能力：数据分析、内容生成、内容整合分发
- "构建-配置-购买"策略：从自建开始，逐步转向产品化和SaaS解决方案
- AI/ML治理委员会确保合规性和标准化

### 25:00-35:00 经销商产品信息系统业务背景
- 解决经销商面临的挑战：客户研究充分但销售人员信息不足
- 系统整合制造、销售、营销数据，通过RAG实现统一信息分发
- 目前服务全部Toyota经销商，月处理7000+交互

### 35:00-45:00 Version 1技术架构深度解析
- Stephen Short详细介绍RAG系统架构：
  - 前端通过Route 53和WAF访问，使用Lambda Edge进行Entra ID认证
  - 意图路由器识别车辆信息，集成内部Prompt Guard安全检查
  - EKS集群托管RAG应用，使用SageMaker生成嵌入向量
  - OpenSearch Serverless作为向量数据库，Bedrock提供推理能力
- ETL管道：Step Functions编排Glue脚本，并行处理30个车辆数据
- 数据质量检查和合规性验证：黄金数据集评估、免责声明处理、流分割技术

### 45:00-48:00 Version 2智能代理平台规划
- 识别Version 1局限性：数据静态化问题、ETL复杂性、功能扩展限制
- AgentCore平台优势：Firecracker VM隔离、无服务器扩展、低基础设施开销
- 目标架构：Strands智能代理+MCP服务器，支持产品专家和产品支持两类代理
- 创新应用：利用AgentCore Memory实现响应缓存，解决API调用限制
- 预计2026年Q1发布Version 2系统