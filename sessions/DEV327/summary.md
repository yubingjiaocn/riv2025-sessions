# AWS re:Invent 2025 - 构建 AI Agent 应用实战

## 会议概述

本次 AWS re:Invent 2025 分组会议由来自香港的两位 AWS 专家主讲，深入探讨了如何在 AWS 平台上构建 AI Agent 应用。会议由开发者倡导者 Hong Huang 和高级解决方案架构师 Jackie Wu 共同呈现，重点介绍了使用 Amazon Nova Act 和开源 Stress Agents（Streamlit Agents）框架构建企业级 AI Agent 的实践方法。

会议首先阐述了 Agentic AI 的未来趋势，引用了 Sequoia Capital 对 2030 年代"Agent 经济"的预测——AI Agent 将形成全球神经网络般的互联系统，甚至可能出现由单人运营、估值达 10 亿美元的"独角兽"公司。演讲者强调，虽然目前 Agentic AI 仍处于早期阶段，但基础设施（如 MCP 和 A2A 通信协议）已在快速构建中。会议通过两个实际演示展示了 AI Agent 的强大能力：一个是自动获取香港天气信息的 Agent，另一个是使用 Manim 库生成数学教育动画的 Agent。Jackie Wu 则从金融行业视角，详细讲解了多 Agent 协作模式，特别是量化交易场景中的应用。

## 详细时间线

### 开场与背景介绍
[00:00 - 02:30] 会议开场，Hong Huang 和 Jackie Wu 自我介绍，说明会议目标是展示如何从零开始构建 AI Agent 应用，而不仅仅是理论讲解。

[02:30 - 04:45] 介绍会议议程：AI Agent 基础概念、使用 MCP 和 Amazon Nova Act 构建天气信息 Agent、使用开源 Stress Agents 构建企业级解决方案、多 Agent 协作模式及金融用例。

### AI Agent 的未来趋势
[04:45 - 07:20] 讲解 Generative AI 的演进路径，从低自主性（需要大量人工监督）到高自主性（可独立做出战略决策）的发展历程，强调目前仍处于早期阶段。

[07:20 - 10:15] 引用 Sequoia Capital 在 AI Ascent 2025 的预测：未来 AI 系统将演变为具有推理、规划、协作和高度自主能力的智能 Agent，2030 年代将形成"Agent 经济"全球网络。提出"随机思维"（Stochastic Mindset）的重要性——开发者需要调整与 LLM 交互的方式。

[10:15 - 12:00] 介绍 2025 年 Agentic AI 的基础设施建设，重点提及 MCP（Model Context Protocol）和 A2A（Agent-to-Agent）通信协议，以及 AWS 在这些开源项目中的积极参与。

### AWS Agent AI 产品组合
[12:00 - 13:30] 展示 AWS 完整的 Agent AI 产品组合架构，分为三层：基础设施层、AI 和 Agent 开发软件层、应用层。会议重点关注 Agent 开发 SDK，包括 Nova Act 和 Stress Agents。

### 实战演示一：香港天气信息 Agent
[13:30 - 16:45] 播放视频演示，展示使用 Amazon Nova Act 构建的天气 Agent。用户只需提供香港天文台网站 URL，然后用自然语言（英语、西班牙语或中文）询问"香港现在天气如何"，Agent 就能自动进行网页抓取，定位信息并保存截图验证。

[16:45 - 18:30] 讲解技术实现细节：左侧代码展示 run_nova_actor_forecast 函数，使用自然语言指令让 Nova Act 提取九天天气预报信息；右侧展示 MCP2 装饰器和在独立线程中运行 Nova Actor 的过程。

[18:30 - 19:15] 推荐两篇技术博客文章：第一篇介绍如何独立使用 Amazon Nova Act 设计 AI Agent，第二篇演示如何结合 MCP 和 Nova Act 实现 Agent，并提供 QR 码供扫描访问。

### 使用开源 Stress Agents 构建企业级 Agent
[19:15 - 22:45] 讲解构建自定义 Agent 系统的挑战：需要连接器（工具和 MCP）、编排器（执行工作流）、内存系统（短期和长期记忆）、推理框架（ReAct、Reflection、Chain of Thought）、角色定义（Persona）以及可观测性和护栏机制。指出 80-90% 的工作与业务逻辑无关。

[22:45 - 24:00] 介绍 Stress Agents（Streamlit Agents）：AWS 最近贡献给开源社区的 SDK，能够用最少代码构建 AI Agent，简化复杂的编排工作，利用先进的 LLM 处理规划、推理链和工具调用。

### 实战演示二：数学动画生成 Agent
[24:00 - 27:30] 播放演示视频，展示使用 Manim（数学可视化 Python 库）创建数学动画的 Agent。用户输入自然语言提示，Agent 自动编写 Manim 脚本并生成精美动画（如三次函数图形从 x=-3 到 x=3 的可视化）。

[27:30 - 30:45] 详细分析核心实现代码：
- 导入 agent 类和 MCP client 类
- 使用标准输入输出建立与 Manim MCP 服务器的连接
- 从 MCP 服务器检索可用工具并初始化 Agent
- 使用自然语言提示处理任务（如"创建绘制三次函数的 Manim 场景"）
- 演示中 Agent 智能地检测到本地环境问题，自动创建简化版本完成任务

[30:45 - 31:30] 提供 QR 码供观众重看视频和获取完整演示代码。

### Jackie Wu 部分：多 Agent 协作模式
[31:30 - 33:00] Jackie Wu 接手演讲，进行现场调查：有多少开发者、使用 VS Code 的人数、已经编写过 Agent 的人数。

[33:00 - 36:15] 解释为什么需要多 Agent 系统：
- **专业化**：专门的 Agent 在特定领域工作，提高精确度
- **可扩展性**：可以添加或删除 Agent 而不影响整体系统
- **可维护性**：调试 100 行代码比调试 10,000 行代码容易得多
- **成本优化**：可以根据任务复杂度匹配合适的模型（智能度、速度、成本）

[36:15 - 37:30] 类比说明：单 Agent 像独奏者，多 Agent 系统像协调良好的团队；单体 Agent 像独自管理投资组合的交易员，多 Agent 系统像对冲基金团队（分析师、量化研究员、交易员、风险管理员、IT 人员）。

### 多 Agent 协作模式一：Agent as Tool
[37:30 - 40:00] 介绍第一种模式"Agent as Tool"：有一个编排 Agent（Orchestrator）接收用户需求，理解意图，然后调用专门的 Agent 执行特定任务。以旅行规划为例：编排 Agent 将任务传递给研究 Agent，再传递给产品推荐 Agent。

[40:00 - 42:30] 量化对冲基金实际案例：量化研究员需要快速验证交易策略（如移动平均线交叉）。展示简单输入界面：股票代码（如 Amazon）、回测窗口、买入/卖出条件，输出回测结果（盈亏、夏普比率）和改进建议。

[42:30 - 44:45] 展示架构图：编排 Agent（Quant Research Agent）调用两个工具（市场数据工具、回测工具）和两个 Agent（策略生成 Agent、结果摘要 Agent）。重点介绍三个组件的实现。

### SageMaker Agent Core Gateway
[44:45 - 48:30] 详细讲解如何使用 SageMaker Agent Core Gateway 构建工具：
- 提供简单安全的方式将 API、Lambda 函数或现有服务封装为 MCP 兼容工具
- 演示使用 Lambda 函数作为后端目标，从 S3 表中存储和检索历史市场数据
- 使用 agent_core_gateway_create_mcp_gateway 创建网关
- 默认使用 Cognito 进行入站身份验证
- 定义清晰的输入输出参数（如 get_market_data 工具）

[48:30 - 50:15] 展示如何将网关作为工具添加到 Quant Research Agent：
- 使用 @tool 装饰器定义工具
- 指定参数和返回值
- 使用 Cognito 进行身份验证
- 使用 httpx 客户端调用网关获取历史市场数据

### Agent Core Runtime
[50:15 - 53:45] 讲解如何将 Agent 部署到 Agent Core Runtime：
- 从 Streamlit 导入 agent 类
- 定义指令（如"你是交易策略代码生成器，使用 Backtrader 框架"）
- 指定名称、系统提示和模型（策略生成 Agent 使用 Claude Sonnet 以利用其编码能力）
- 导入 bedrock_agent_core_apps
- 指定 app.entry_point 和运行端口（默认 8080）
- 使用 agent_core_config 指定文件和依赖
- 使用 agent_core_launch 部署
- 支持自定义容器（如 Java）

[53:45 - 55:30] 展示如何将 Agent 作为工具：
- 使用 @tool 装饰器
- 定义 JSON 格式输入（名称、买入条件、卖出条件）
- 使用 Agent Core Runtime 调用 Agent

### 编排 Agent 实现
[55:30 - 57:15] 展示 Quant Research Agent（编排 Agent）的实现：
- 导入 agent 类
- 定义系统提示（获取历史市场数据、生成策略、运行回测代码、分析结果）
- 定义四个工具：fetch_market_data、generate_strategy、run_back_test、create_result_summaries
- 如果出错，编排 Agent 会重新运行代码生成

### 实时演示：量化交易策略回测
[57:15 - 62:00] 使用 Kiro CLI 运行实时演示：
- 输入 10 日简单移动平均线与 30 日简单移动平均线交叉策略
- Agent 首先调用 generate_trading_strategies 工具，生成 JSON 格式输入和 Python 代码
- 耗时 6 秒生成代码
- 调用 fetch_market_data 通过网关获取约 200 个数据点（Amazon 股票一年数据）
- 运行实际回测，使用 Backtrader 框架的 Cerebro 引擎
- 输出初始价值、利润、总回报
- 使用 Agent Core Memory 保存回测结果
- 生成结果摘要，包括建议、警报和关键关注点

[62:00 - 62:45] 提供 QR 码供观众扫描体验实时演示，并声明这不构成任何投资建议。

### 多 Agent 协作模式二：Swarm Pattern
[62:45 - 65:30] 介绍第二种模式"Swarm Pattern"：
- 与 Agent as Tool 模式根本不同，没有单一的"老板"（编排 Agent）
- Agent 之间相互通信，动态协作解决问题
- 维护共享上下文，所有 Agent 都可以访问
- 关注"谁在 Swarm 系统中"、"其他 Agent 是谁"等信息

[65:30 - 会议结束] 会议在此处字幕截断，但 Jackie 继续讲解 Swarm 模式的更多细节和其他协作模式。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


关键技术要点：
- Amazon Nova Act：用于网页抓取和自然语言交互
- MCP（Model Context Protocol）：Agent 工具互操作性协议
- Stress Agents（Streamlit Agents）：AWS 开源的 Agent SDK
- SageMaker Agent Core Gateway：构建 MCP 兼容工具
- Agent Core Runtime：托管和部署 Agent
- Agent Core Memory：Agent 间共享状态
- 多模型策略：根据任务选择合适模型（Claude Sonnet 用于编码，Nova 用于摘要）