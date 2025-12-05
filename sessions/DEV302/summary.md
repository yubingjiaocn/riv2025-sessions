# AWS re:Invent 2025 - 使用 .NET 构建 AI 应用程序

## 会议概述

本次技术分享会由 AWS 的两位工程师主讲，重点介绍如何使用 .NET 技术栈构建 AI 应用程序。会议原本计划讨论 Semantic Kernel，但由于 Microsoft 推出了新的 Agent Framework 来取代 Semantic Kernel，因此内容进行了调整，涵盖了两个框架以及它们与 AWS 服务的集成。

演讲者首先明确了 Agentic AI 的核心定义：一个在循环中运行的 LLM（大语言模型），能够调用工具来执行额外的工作。这是构建 AI 代理的哲学基础，而不仅仅是技术实现。会议展示了多个实际应用场景，包括会议记录总结、个性化推荐、客户支持聊天机器人等。

技术栈方面，会议详细介绍了 Microsoft 的工具（Microsoft.Extensions.AI、Semantic Kernel、Agent Framework）和 AWS 的服务（Amazon Bedrock、Agent Core）。特别强调了 Agent Framework 目前仍处于预览阶段，尚未原生支持 AWS 服务，演讲者呼吁社区提供反馈以推动集成开发。会议还深入讲解了 AWS Agent Core 的三个核心组件：Runtime（运行时容器服务）、Gateway（MCP 服务器管理）和 Code Interpreter（隔离代码执行环境）。

## 详细时间轴

### 开场与背景介绍
- **00:00:00** - 会议开始，介绍主题：使用 .NET 构建 AI 应用程序
- **00:00:15** - 说明原计划讲解 Semantic Kernel，但 Microsoft 已转向 Agent Framework
- **00:00:45** - 演讲者自我介绍：AM（AWS 首席开发者倡导者）和 Nikki（Amazon 首席工程师）
- **00:01:30** - 强调所有演示代码都是实验性的，因为 Agent Framework 仍在预览阶段

### Agentic AI 概念
- **00:02:00** - 引用 Mark Brooker 对 Agent 的定义：在循环中运行的 LLM，能够调用工具
- **00:02:45** - 讨论实际应用场景：会议记录总结、个性化、支持聊天机器人
- **00:03:30** - 会议内容分为两大类：Microsoft 工具和 AWS 工具及其交集

### Microsoft.Extensions.AI
- **00:04:00** - 介绍 Microsoft.Extensions.AI 作为抽象层的作用
- **00:04:30** - 展示第一个代码示例：使用抽象 chat client 的基本实现
- **00:05:00** - 说明该库简化了不同 AI 提供商的集成

### Semantic Kernel
- **00:05:30** - 介绍 Semantic Kernel 框架及其组成部分
- **00:06:00** - 讲解 Plugins（插件/工具调用）、AI Models（AI 模型）、Hooks 和 Filters（中间件）
- **00:07:00** - 展示 Semantic Kernel 代码示例，包含约 10 行代码
- **00:07:45** - 说明 Semantic Kernel 原生支持 Amazon Bedrock

### Microsoft Agent Framework
- **00:08:30** - 介绍 Agent Framework 作为 Semantic Kernel 的继任者
- **00:09:00** - 强调 Agent Framework 目前没有原生 AWS 支持
- **00:09:30** - 呼吁社区通过 GitHub 提供反馈和贡献
- **00:10:15** - 展示 Agent Framework 代码示例，比 Semantic Kernel 更简洁
- **00:11:00** - 讨论 Agent Framework 的功能：工具调用、循环、内存、多轮对话
- **00:11:45** - 指出 Agent Framework 使用标准接口（IChatClient），不是原生 Bedrock 集成

### AWS 工具介绍
- **00:12:30** - 开始介绍 AWS 工具，重点是基础设施层面
- **00:13:00** - 介绍 Bedrock.ME.AI 包（AWS 对 Microsoft.Extensions.AI 的实现）
- **00:13:45** - 展示使用 Bedrock.ME.AI 的代码示例
- **00:14:30** - 说明该包提供 embedding generator 和 image generator

### Amazon Bedrock
- **00:15:00** - 介绍 Amazon Bedrock 作为完全托管的 AI 模型服务
- **00:15:30** - 对比 SageMaker（训练模型）和 Bedrock（直接使用预训练模型）
- **00:16:00** - 说明 Bedrock 面向应用开发者，提供 Anthropic、Amazon Nova 等模型

### Agent Core 概述
- **00:16:30** - 介绍 Agent Core 作为无服务器基础设施
- **00:17:00** - 列举 Agent Core 组件：Runtime、Gateway、Memory、Observability、Identity、Code Interpreter、Browser Tool
- **00:18:00** - 说明本次演示将重点展示 Runtime、Gateway 和 Code Interpreter

### Agent Core Runtime
- **00:18:30** - 详细介绍 Runtime：基于 Firecracker 的隔离微虚拟机
- **00:19:00** - 说明 Runtime 需要实现两个端点：/ping 和 /invocations
- **00:19:45** - 解释调用流程：UI → invoke-agent SDK → Runtime /invocations
- **00:20:30** - 展示 Runtime 架构图：ARM 容器、ECR、会话隔离
- **00:21:15** - 讨论 Runtime 的优势：自动扩展、会话隔离

### Agent Core Gateway
- **00:22:00** - 介绍 Gateway 作为 MCP 服务器的简化方案
- **00:22:30** - 说明只需 REST API 和 OpenAPI 规范即可创建 MCP 服务器
- **00:23:00** - 展示 Gateway 可以管理多个 MCP 服务器和 API 密钥
- **00:23:45** - 说明支持 API 端点和 Lambda 函数作为目标

### Agent Core Code Interpreter
- **00:24:30** - 介绍 Code Interpreter：隔离沙箱中运行代码
- **00:25:00** - 举例：LLM 读取 CSV 文件并计算统计数据
- **00:25:45** - 说明 Code Interpreter 是独立容器，无出站互联网访问
- **00:26:30** - 支持 Python、JavaScript、TypeScript
- **00:27:00** - 可以包含文件（如 CSV）并使用 Python 统计库
- **00:27:45** - 讨论何时使用 Code Interpreter vs 自定义工具

### 代码演示开始
- **00:28:30** - 开始实际代码演示
- **00:29:00** - 第一个演示：使用 Bedrock.ME.AI 的基本示例
- **00:29:30** - 展示代码：实例化 Bedrock 客户端，发送提示"is this thing on"
- **00:30:00** - 运行演示，成功获得响应

### Semantic Kernel 演示
- **00:30:45** - 开始 Semantic Kernel 演示
- **00:31:00** - 展示添加日期插件的代码（LLM 无法自己判断时间）
- **00:31:45** - 说明插件为 LLM 提供额外工具
- **00:32:15** - 介绍 Kernel 类作为 Semantic Kernel 的核心
- **00:32:45** - 建议在 Web 服务中使用 transient service 模式

注：字幕在此处截断，完整演示内容未包含在提供的文本中