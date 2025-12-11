# AWS re:Invent 2025：使用AI构建.NET应用程序

## 会议概述

本次技术分享由AWS首席开发者倡导者AM Grobelny和Amazon首席工程师Nicki共同主讲，重点介绍了如何使用AI技术构建.NET应用程序。会议涵盖了从传统的Semantic Kernel到微软最新的Agent Framework的演进，以及AWS AgentCore等基础设施服务的使用。

演讲者强调了当前AI开发领域的快速变化，特别是微软从Semantic Kernel向Agent Framework的转变。由于Agent Framework仍处于预览阶段，所有演示代码都具有实验性质。会议通过理论讲解和实际代码演示相结合的方式，展示了如何在AWS基础设施上部署和运行.NET AI应用程序，包括使用Amazon Bedrock、AgentCore Runtime、Gateway和Code Interpreter等服务。

## 详细时间线与关键要点

### 0:00-5:00 开场介绍
- 演讲者自我介绍：AM Grobelny（AWS首席开发者倡导者）和Nicki（Amazon首席工程师）
- 会议主题转变：原计划讲解Semantic Kernel，但微软推出了Agent Framework
- 重要警告：所有代码都处于预览/实验阶段，不建议用于生产环境

### 5:00-10:00 AI代理概念解释
- 引用AWS杰出工程师Mark Brooker的定义：代理是存在于循环中的LLM，能够调用工具执行额外工作
- AI代理的两个核心要素：循环机制和工具调用能力
- 实际应用场景：会议记录总结、个性化推荐、客户支持聊天机器人

### 10:00-15:00 Microsoft Extensions AI基础
- 介绍Microsoft Extensions AI作为抽象层的重要性
- 展示最基本的聊天客户端代码示例
- 强调抽象层在快速发展的AI领域中的价值

### 15:00-25:00 Semantic Kernel框架详解
- Semantic Kernel的核心组件：插件、AI模型、钩子和过滤器
- 插件用于函数调用和工具集成
- 钩子提供中间件功能，过滤器提供权限控制
- 代码演示：使用Bedrock的基本Semantic Kernel实现
- 与传统JavaScript Ajax开发的类比

### 25:00-35:00 Microsoft Agent Framework介绍
- Agent Framework作为Semantic Kernel的继任者
- 代码更简洁，功能更直观
- 目前缺乏对AWS服务的原生支持
- 呼吁社区贡献和反馈，推动AWS集成开发

### 35:00-40:00 AWS工具生态系统
- 介绍Bedrock MEAI（Microsoft Extensions AI）包
- Amazon Bedrock服务概述：为应用开发者提供完全托管的模型
- AgentCore服务组件：Runtime、Gateway、Memory、Identity、Code Interpreter、Browser Tool

### 40:00-50:00 AgentCore深度解析
- **Runtime**：基于Firecracker的容器化服务，提供会话隔离和自动扩展
- **Gateway**：将REST API转换为MCP服务器，无需手动构建
- **Code Interpreter**：隔离沙箱环境，支持Python、JavaScript、TypeScript代码执行

### 50:00-59:00 实际项目演示
- 展示占星术代理应用，包含UI界面和后端服务
- 对比Semantic Kernel和Agent Framework的实现差异
- Semantic Kernel版本：仅支持每日占星，使用直接API调用
- Agent Framework版本：通过MCP服务器支持每日、每周、每月占星
- 演示AgentCore Runtime的部署和调用方式
- 容器必须运行在8080端口，实现/ping和/invocations端点

### 技术要点总结
- 所有代码均为实验性质，不适用于生产环境
- Python工具链相比.NET更成熟，需要社区贡献改进.NET支持
- 提供了完整的GitHub代码库供学习参考
- 强调了会话管理、凭证获取等实现细节的重要性