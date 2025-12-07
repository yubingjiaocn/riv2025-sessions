# AWS re:Invent 2025 会议总结：使用 Amazon Bedrock Agent Core 为遗留应用添加 AI Agent

## 会议概述

本次会议主要演示了如何在不修改遗留应用代码的情况下，使用 Amazon Bedrock Agent Core 和 Strands SDK 为其添加 AI Agent 功能。演讲者团队（Deepali Tandere、Fran、Stefan 和 Yantois）通过实际编码演示，展示了从零开始创建 AI Agent、部署到云端、以及与现有遗留系统集成的完整流程。

会议强调了遗留应用虽然可靠，但在适应性和自动化方面存在挑战，特别是对于不熟悉代码库的开发者。通过使用 Strands SDK 定义 Agent 能力、Agent Core 提供可扩展的运行时环境、以及 MCP（Model Context Protocol）标准化通信协议，开发者可以快速构建能够自主思考和行动的 AI Agent，无需重写任何遗留代码。

演示包括三个主要部分：首先在空项目中创建基础 Agent，然后将其部署到 AWS 云端，最后展示如何通过 Gateway 和 OpenAPI 规范将 Agent 连接到遗留的 Java 应用（一个独角兽商店），实现通过自然语言与遗留系统交互的能力。整个过程展示了 AWS 提供的工具链如何简化 AI Agent 的开发和部署流程。

## 详细时间线

### 开场介绍（开始）
- **内容**：介绍遗留应用的可靠性与现代化挑战，提出使用 AI Agent 与遗留系统交互的解决方案
- **演讲者**：Deepali Tandere

### 核心概念讲解（约 2-5 分钟）
- **内容**：解释 Agentic Loop 工作原理 - 包括 Prompt、Agent（控制器/编排器）、Model（基础模型）、Tools（外部实体）的循环机制
- **要点**：Agent 通过循环的方式进行行动、解释和规划，直到任务完成

### Strands SDK 介绍（约 5-8 分钟）
- **内容**：介绍 Strands 开源 Python SDK，强调其模型驱动方法和少量代码即可构建 Agent 的特点
- **特点**：可在任何基础设施上运行，支持 Amazon Bedrock 和 OpenAI 模型

### Agent Core 服务介绍（约 8-12 分钟）
- **内容**：讲解 Agent Core 作为托管运行时和基础设施的作用
- **核心组件**：
  - Runtime（运行时）：支持多用户访问、自动扩展、沙箱、会话管理
  - Memory（内存）：存储跨会话的上下文信息
  - Tools（工具）：原生 AWS 集成（S3、Lambda、DynamoDB）和 MCP 工具支持
  - Gateway（网关）：暴露内部 API 和 Lambda 函数为 MCP 工具
  - Identity（身份）：身份验证和授权选项

### MCP 协议讲解（约 12-15 分钟）
- **内容**：解释 MCP 作为开放标准，定义 Agent 与应用/服务通信的方式
- **三大能力**：
  - Tools（工具）：Agent 可执行的操作
  - Resources（资源）：Agent 可访问的外部数据源
  - Prompts（提示）：包含文本和参数的指令手册

### 实践演示开始 - Fran 接手（约 15-18 分钟）
- **内容**：切换到编码环节，说明将进行 50 分钟的实际编码演示
- **准备工作**：展示 requirements.txt 文件，包含三个核心包

### 创建虚拟环境和基础 Agent（约 18-25 分钟）
- **操作**：
  - 创建虚拟环境
  - 安装依赖包
  - 创建 reinvent_demo_agent_mam345.py 文件
  - 导入 Agent 类并实例化
  - 仅用 3-4 行代码创建第一个 Agent
- **测试**：询问"美国首都是什么"，成功获得回答

### 添加工具能力（约 25-32 分钟）
- **问题**：询问"拉斯维加斯今天天气如何"时，LLM 无法回答实时信息
- **解决方案**：
  - 从 strands_tools 导入 HTTP Request 工具
  - 添加系统提示（system prompt）
  - 将工具传递给 Agent
- **结果**：Agent 成功找到并调用外部 API 获取天气信息

### 转换为 Bedrock Agent Core Agent（约 32-40 分钟）
- **操作**：
  - 导入 bedrock_agent_core 包
  - 实例化 BedrockAgentCoreApp 类（创建 HTTP 服务器，监听 8080 端口）
  - 添加 @app.entry_point 装饰器
  - 修改输入方式从 CLI 改为 JSON payload
- **测试**：Agent 在本地运行，通过 curl 命令测试"纽约今天天气如何"

### 部署到云端（约 40-50 分钟）
- **工具**：使用 bedrock-agent-core-starter-toolkit
- **配置过程**：
  - 运行 agent-core configure 命令
  - 选择部署配置（ZIP 部署 vs Docker 部署）
  - 配置 Python 环境、执行角色、S3 存储桶
  - 选择授权方式（IAM）
  - 配置内存选项（跳过）
- **部署**：运行 agent-core launch 命令，打包并上传到 S3，部署到 Agent Core Runtime

### 控制台演示（约 50-55 分钟）
- **展示**：
  - 在 AWS Console 中查看 Agent Core 服务
  - 显示已部署的 Agent 列表
  - 展示 CloudWatch 日志集成
  - 使用 Web UI 测试 Agent（询问"德国首都是什么"）

### 遗留应用集成 - Yan 接手（约 55 分钟开始）
- **场景**：展示一个运行在 ECS 上的 Java 遗留应用（独角兽商店）
- **目标**：在不修改遗留应用代码的情况下添加 AI Agent 能力

### 使用 Amazon Q Developer 生成 OpenAPI 规范（约 58-62 分钟）
- **操作**：
  - 使用 Amazon Q Developer 分析遗留应用
  - 自动生成 OpenAPI 规范文件
  - 忽略 text/plain 端点

### 配置 Agent Core Gateway（约 62-68 分钟）
- **步骤**：
  - 在 Agent Core Console 中创建 Gateway
  - 添加 REST API Target
  - 粘贴 OpenAPI 规范（inline schema）
  - 配置授权（API Key，但本例中不需要）
- **说明**：Gateway 可以托管多个 Target（MCP 服务器、Lambda 函数、REST API）

### 架构说明（约 68-70 分钟）
- **展示架构图**：
  - 左侧：前端 UI 和 Agent
  - 中间：Gateway
  - 右侧：遗留应用（ECS、数据库）
- **强调**：完全不需要修改遗留应用代码，通过 OpenAPI 规范自动将路径转换为工具

### 更新 Agent 代码以使用 Gateway（约 70-80 分钟）
- **操作**：
  - 添加日志配置
  - 定义环境变量（Gateway URL、OAuth Provider URL、Memory、Model ID）
  - 更新系统提示为"帮助购买独角兽的 Agent"
  - 添加 @requires_access_token 装饰器获取访问令牌
  - 配置 Gateway 认证

### 会议结束
- **总结**：完整演示了从零创建 Agent、部署到云端、集成遗留应用的全流程
- **核心价值**：无需修改遗留代码即可添加现代 AI 能力