# AWS re:Invent 2025 技术分享会总结：使用 Strands Agent 构建多智能体角色扮演游戏主持人

## 会议概述

本次技术分享会展示了如何使用 AWS 的 Strands Agent SDK 构建一个多智能体工作流系统，用于辅助《龙与地下城》(D&D) 游戏主持人。演讲者通过实际编码演示，展示了如何在短短几十行代码内创建一个具有多个专业化智能体的复杂系统。

Strands Agent 是 AWS 内部使用的 Python SDK（Amazon Q 等产品的底层技术），最近已开源。该 SDK 的核心优势在于大幅简化了智能体开发流程，并原生支持 MCP（Model Context Protocol）和 A2A（Agent-to-Agent）两大协议标准。MCP 协议用于智能体与工具之间的通信，类似于 AI 领域的 REST API；而 A2A 协议则标准化了智能体之间的对话和协作方式。

演示项目包含一个主编排智能体（游戏主持人），它可以调用角色管理智能体、规则查询智能体（使用 RAG 技术访问完整的 D&D 规则手册），以及通过 MCP 服务器提供的骰子投掷工具。整个架构展示了现代 AI 智能体系统的最佳实践：将复杂任务分解给专业化的子智能体处理，每个智能体专注于特定领域。

## 详细时间线与关键要点

00:00:00 - 会议开场与背景介绍
- 演讲者询问观众对桌面角色扮演游戏（如《龙与地下城》）的了解程度
- 介绍项目背景：作为 D&D 玩家，寻找游戏主持人（Game Master）很困难，因为担任 GM 需要掌握大量规则和技能
- 提出使用 AI 辅助游戏主持人的想法

00:02:30 - 智能体（Agent）概念讲解
- 区分 LLM 与 Agent：LLM 只能对话，而 Agent 具有执行能力（agency）
- Agent 通过访问工具（APIs、函数、数据库、其他 Agent）来执行实际操作
- 介绍多智能体架构：通常有一个编排者（orchestrator）连接多个专业化智能体
- 举例：学习辅导系统中，主教练智能体可以调用数学、物理、历史等各学科专家智能体

00:05:00 - MCP 与 A2A 协议介绍
- MCP（Model Context Protocol）：标准化智能体发现和使用工具的方式，被称为"AI 的 REST"
- 在 MCP 之前，连接工具需要自定义维护，无法共享；MCP 使工具可以被任何智能体发现和使用
- A2A（Agent-to-Agent）：标准化智能体之间的通信协议
- 关键区别：MCP 用于工具调用（单向请求-响应），A2A 用于智能体对话（双向思考过程）

00:07:30 - 项目架构说明
- 主智能体：AI 游戏主持人（编排者）
- 子智能体 1：角色管理智能体（创建和管理角色，访问角色数据库）
- 子智能体 2：规则智能体（RAG 系统，访问完整 D&D 规则手册）
- MCP 工具：骰子投掷服务（D20 等各类骰子）

00:09:00 - Strands Agent SDK 介绍
- AWS 内部使用的 SDK（Amazon Q 等产品的底层技术）
- 几个月前开源，支持 Python（本周将宣布更多语言支持）
- 核心优势：用极少代码构建智能体和多智能体工作流
- 原生支持 MCP 和 A2A 协议
- 安装方式：pip install strands-agents

00:10:30 - 实时编码演示开始
- 演示环境：空白项目，只有 app.py 和 requirements.txt
- 第一步：三行代码创建基础智能体
 python
  from strands import Agent
  agent = Agent()
  agent("Good morning Vegas")
  
- 默认使用 Amazon Bedrock 的 Claude Sonnet 模型

00:12:00 - 模型配置演示
- 展示如何切换模型：从 Claude Sonnet 切换到 Amazon Nova Premier
- 演示温度（temperature）等参数配置
- 强调 Strands 的模型无关性：支持 Bedrock、Anthropic、Gemini、Llama、Mistral 等
- 演示使用 Ollama 在本地运行 Llama 3.2 模型

00:15:30 - 工具集成演示
- 问题演示：询问"现在几点"时，LLM 无法回答实时信息
- 引入 Strands 社区工具包（strands-agents-tools）
- 演示添加 current_time 工具：
 python
  from strands_tools import current_time
  agent = Agent(tools=[current_time])
  
- 智能体成功调用工具获取当前时间

00:18:00 - 文件操作工具演示
- 添加 file_write 和 python_repl 工具
- 演示复杂任务：要求智能体编写斐波那契数列函数并执行
- 智能体自动完成：编写代码 → 写入文件 → 执行代码
- 展示安全防护机制：执行敏感操作前需要用户确认（可通过环境变量在 CI/CD 中禁用）

00:21:00 - 自定义工具创建
- 演示创建骰子投掷函数
- 使用 @tool 装饰器将普通函数转换为智能体工具：
 python
  from strands import tool
  @tool
  def roll_dice(faces: str):
      # 实现代码
  
- 成功演示投掷 D6 和 3D20（三个 20 面骰子）

00:24:00 - MCP 服务器创建演示
- 使用 FastMCP 库创建 MCP 服务器（注意：FastMCP 不是 Strands 的一部分）
- 将骰子工具部署为 MCP 服务器（端口 8081）
- 配置使用 Streamable HTTP 传输协议
- 服务器成功运行在 localhost:8081

00:27:00 - MCP 客户端集成
- 在主智能体中添加 MCP 客户端：
 python
  from strands import MCPClient, streamable_http
  dice_mcp = MCPClient(streamable_http("http://localhost:8081/mcp"))
  agent = Agent(tools=dice_mcp.tools)
  
- 演示智能体通过 MCP 协议调用远程工具
- 展示服务器端的请求日志

00:30:00 - A2A 智能体创建
- 创建角色管理智能体（character_agent.py）
- 配置智能体名称、描述和工具访问权限（file_read、file_write）
- 创建 A2A 服务器：
 python
  from strands import A2AServer
  server = A2AServer(agent=character_agent)
  server.run(host="localhost", port=8082)
  
- 角色管理智能体成功运行在端口 8082

00:33:00 - A2A 客户端集成
- 在主智能体中添加 A2A 客户端提供者：
 python
  from strands import A2AClientProvider
  a2a_provider = A2AClientProvider(["http://localhost:8082"])
  agent = Agent(tools=a2a_provider.tools)
  
- 关键区别说明：
  - MCP：需要为每个服务器创建单独的客户端，可以列出所有工具
  - A2A：一个提供者可以管理多个智能体，只发送提示词，不知道对方的内部实现

00:36:00 - 系统提示词（System Prompt）配置
- 添加系统提示词指导主智能体行为：
  - 定义角色：D&D 游戏主持人
  - 说明可用资源：骰子工具、角色管理智能体
  - 关键指令：永远不要自己回答，始终使用工具或智能体
- 这是多智能体系统的最佳实践

00:38:00 - 完整系统演示
- 测试命令："创建一个名为 Steve 的暗夜精灵角色，投掷骰子生成属性，并保存到文件"
- 系统执行流程：
  1. 主智能体调用 MCP 骰子服务投掷多次（生成力量、敏捷等 6 项属性）
  2. 主智能体通过 A2A 调用角色管理智能体
  3. 角色管理智能体使用 file_write 工具保存角色信息
  4. 成功创建 steve_nightelf_character.txt 文件

00:41:00 - 查询演示
- 测试命令："告诉我关于角色 Steve 的信息"
- 执行流程：
  1. 主智能体列出可用的 A2A 智能体
  2. 发现角色管理智能体并发送查询
  3. 角色管理智能体使用 file_read 读取文件
  4. 返回完整角色信息
  5. 主智能体甚至添加了对角色的评价（"Steve 可能更依赖智力而非体质"）

00:43:00 - Docstring 最佳实践讲解
- 强调工具发现依赖于 docstring（文档字符串）
- Docstring 应包含：描述、参数说明、返回类型、示例
- 建议使用 AI 代码助手（如 Amazon Q）根据 Strands 文档中的最佳实践自动生成 docstring
- 展示 current_time 工具的 docstring 示例，说明如何通过参数（如时区）增强工具能力

00:45:00 - 总结与展望
- 演示了如何用极少代码构建复杂的多智能体系统
- 强调 Strands Agent 的核心优势：简洁、标准化、模型无关
- 提到完整项目还包括规则查询智能体（使用 RAG 访问 D&D 规则手册）
- 预告将展示更复杂的演示版本

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


技术要点总结：
- **代码简洁性**：基础智能体仅需 3 行代码，完整多智能体系统约 50 行
- **协议标准化**：MCP 和 A2A 使工具和智能体可复用、可共享
- **模型灵活性**：支持云端（Bedrock、Anthropic）和本地（Ollama）模型
- **安全机制**：敏感操作需用户确认，可配置自动批准
- **最佳实践**：系统提示词、docstring 规范、专业化智能体分工