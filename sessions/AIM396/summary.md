# AIM 396: 集成开源框架与Amazon Bedrock Agent Core

## 会议概述

本次AWS re:Invent 2025技术分享会由AWS首席数据科学家Shreya Subramanyan、AWS高级GenAI专家解决方案架构师Ari，以及Cohere Health工程副总裁Keith共同主讲。会议重点探讨了如何将开源Agent框架与Amazon Bedrock Agent Core进行集成，从概念验证(POC)到生产环境的完整实施路径。

演讲者首先介绍了构建Agent所需的复杂组件，包括框架选择、工具集成、状态管理等挑战。随后详细展示了Agent Core如何简化这些集成过程，支持LangGraph、CrewAI、Strands等主流开源框架，并通过MCP和A2A等开放协议实现标准化连接。会议还深入讨论了从传统DevOps向AgentOps的演进，以及在医疗保健等关键领域的实际应用案例。

## 详细时间线与关键要点

### 0:00-5:00 开场介绍与背景
- 介绍演讲团队：Shreya(AWS首席数据科学家)、Ari(AWS高级GenAI专家SA)、Keith(Cohere Health工程VP)
- 现场调研：大部分与会者已使用无代码/低代码工具或开源框架构建过Agent
- 展示主流开源框架和协议：LangGraph、CrewAI、Strands、MCP、A2A等
- 强调从POC到生产环境的挑战性

### 5:00-15:00 Agent Core架构概览
- Agent Core作为端到端Agent技术平台的核心组件介绍
- Runtime服务：支持部署任何开源Agent和MCP/A2A服务器，无需或仅需最小代码更改
- 集成服务包括：身份管理、内存管理、策略与评估、可观测性
- 基于OpenTelemetry格式的统一可观测性解决方案
- 演示客户服务场景：从人工客服和技术支持转向Agent自动化

### 15:00-25:00 框架选择与集成方案
- 三大主流框架对比：
  - LangGraph：基于图的执行，学习曲线陡峭但功能强大
  - CrewAI：易于上手，适合基于角色的多Agent团队
  - Strands：AWS开源框架，提供企业级功能
- 演示本地开发到云端部署的迁移过程
- Agent Core Runtime的核心优势：自动扩缩容、多模型提供商支持、严格安全控制
- 支持双向流式传输，便于语音接口集成

### 25:00-35:00 部署与开发工具
- 两种部署方式：Docker容器(ECR)和ZIP文件(S3)
- 代码修改最小化：仅需导入SDK、初始化应用、添加装饰器
- Agent Core CLI工具链：
  - agent-core configure：配置部署参数
  - agent-core deploy：一键部署到Runtime
  - 一分钟内完成部署并可开始调用
- 演示客户服务Agent(Strands)和技术支持Agent(LangGraph)的并行部署

### 35:00-45:00 开放协议与标准化集成
- 上下文工程在Agent中的重要性：用户指令、系统指令、RAG检索、短期记忆、工具上下文
- MCP(Model Context Protocol)：安全访问外部数据和工具的通用接口
- A2A(Agent-to-Agent)：标准化Agent间通信协议
- Agent Core Gateway：为现有API创建MCP接口
- 深度开源集成：Strands内置会话管理器、LangGraph内存检查点保存器
- 与LangChain AWS库的合作，通过pip安装获得AWS超能力

### 45:00-55:00 AgentOps与生产运维
- 从传统DevOps向AgentOps的演进：基础设施、工具、流程、文化四个维度
- 与Langfuse的深度集成：开源LLM工程平台，支持OpenTelemetry标准
- 三阶段方法论：
  1. 实验与超参数优化阶段
  2. QA测试与CI/CD集成
  3. 生产运维与持续学习
- Cohere Health实际案例：医疗保险预授权流程自动化
- 使用Agent Core实现30-40%的审查速度提升
- 企业级安全与合规要求：身份管理、访问控制、审计追踪

### 55:00-56:30 总结与资源
- 总结Agent Core与开源框架的集成优势
- 提供代码仓库和深度学习资源
- 现场答疑环节安排