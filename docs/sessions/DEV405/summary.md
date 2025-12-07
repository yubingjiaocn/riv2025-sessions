# AWS re:Invent 2025 技术分享会总结：使用 Rust 构建高性能 MCP 服务器

## 会议概述

本次技术分享会由 AWS 开发者倡导者 Darkco 主讲，主题为"使用 Rust 编译超快速 MCP 服务器"。Darkco 拥有系统管理员背景，曾负责 AIX、Solaris、Unix 等系统维护工作，近三年专注于 Rust 语言开发，并在 AWS 的 Rust 生态系统中扮演重要角色。

会议采用开放式讨论形式，以实际代码演示为主，仅包含少量幻灯片。Darkco 通过现场编码展示了如何使用 Rust 构建 MCP（Model Context Protocol）服务器，并演示了一个有趣的应用场景：通过 MCP 服务器管理待办事项（to-do）列表，甚至可以使用网络打印机打印待办事项。

会议的核心观点是：随着 LLM 和代码助手的普及，Python 等动态语言的优势正在减弱，而 Rust 这样的编译型语言凭借其安全性、性能和现代工具链支持，正在成为构建 MCP 服务器的更优选择。Rust 编译的 MCP 服务器启动速度远快于 TypeScript 或 Python 实现（约 0.1 秒 vs 4 秒），且无需每次启动时从网络下载依赖。

## 详细时间线与关键要点

### 00:00 - 开场介绍
- 讲师自我介绍：Darkco，AWS 开发者倡导者，系统管理员出身
- 会议形式说明：以代码演示为主的开放式讨论
- 现场调查：多数参会者使用 Rust，部分编写过 MCP 服务器

### 02:30 - MCP 协议介绍
- MCP（Model Context Protocol）是开放协议，允许 LLM 与本地工具、资源和提示交互
- MCP 由 Anthropic 等公司推动，标准化了 LLM 工具调用方式
- 示例：Grimmoire MCP 服务器，用于保存和检索代码模式片段

### 05:00 - 为什么选择 Rust
- **核心论点**：Python 应该被淘汰，Rust 是更好的选择
- 理由：有了 LLM 和代码助手，编写 Rust 不再困难
- Rust 提供更高的安全性、性能和可编译性
- 大多数现有 MCP 服务器使用 TypeScript 或 Python

### 07:00 - 性能对比演示
- Rust MCP 服务器启动时间：约 0.1 秒
- TypeScript MCP 服务器启动时间：约 4 秒
- Rust 编译为二进制文件，无需每次从网络下载依赖
- TypeScript/Python 服务器需要通过 npx、pipx 或 uvx 安装

### 10:00 - 项目演示说明
- 演示项目：待办事项 MCP 服务器
- 功能：创建待办事项、获取所有待办事项、打印待办事项
- 后端：本地运行的 JSON API 服务器
- 硬件：网络收据打印机

### 12:00 - Rust MCP SDK 介绍
- 使用 RMCP（Rust MCP SDK）
- 几个月前才被正式列入 MCP SDK 列表
- 当前版本：0.10（三天前发布）
- 包含两个核心 crate：rmcp 和 rmcp-macros

### 15:00 - 第一阶段：空 MCP 服务器
- 项目结构：main.rs（入口点）和 todos.rs（工具和路由）
- 核心组件：
  - 定义包含 tool_router 的结构体
  - 使用 #[tool_router] 宏装饰实现块
  - 实现 ServerHandler trait
  - 提供 get_info() 方法（返回服务器信息和指令）
  - 提供初始化函数

### 18:00 - MCP Inspector 工具介绍
- 使用 npx @modelcontextprotocol/inspector 启动
- 在浏览器中提供调试界面
- 可以测试工具调用、查看消息和服务器通知
- 支持所有符合 MCP 协议的服务器

### 20:00 - Just 构建工具推荐
- Just 是 Make 的现代替代品，语法更简单
- Make 已有 40 多年历史
- 演示中使用 Just 文件定义构建和测试命令

### 22:00 - 第二阶段：添加第一个工具
- 定义数据结构：Todo 和 Todos（包装在 Arc 中）
- Arc（原子引用计数）用于处理异步调用的数据共享
- 实现 get_todos() 函数：调用 API 获取待办事项
- 实现 get_all_todos() 工具：
  - 使用 #[tool] 宏装饰
  - 返回 CallToolResult 类型
  - 错误处理使用 McpError
  - 成功时返回 JSON 内容

### 28:00 - 工具测试
- 使用 MCP Inspector 连接服务器
- 执行 list_tools 命令查看可用工具
- 成功调用 get_all_todos 工具并获取结果

### 30:00 - 第三阶段：带参数的工具
- 定义参数结构体：NewTodoParams
- 使用 schemars crate 提供 JSON Schema 支持
- 注意：某些 IDE（如 Kira）可能存在 JSON Schema 兼容性问题
- 实现 create_todo() 函数：向 API 发送 POST 请求
- 实现 create_new_todo() 工具：
  - 接受 NewTodoParams 参数
  - 从环境变量获取用户 ID
  - 返回文本内容而非 JSON（包含新创建的待办事项 ID）

### 35:00 - 最佳实践建议
- **重要**：不要向 LLM 返回过多 JSON 数据
- 只返回必要的数据和简短的指令
- 避免填满上下文窗口
- 结构化响应比原始 JSON 更有效

### 38:00 - 参数化工具测试
- 在 MCP Inspector 中测试 create_new_todo 工具
- 输入参数：body 和 title
- 成功创建待办事项并接收包含 ID 的响应

### 40:00 - 第四阶段：打印功能
- 定义 PrintTodoParams：只需要 todo_id
- 实现打印逻辑：
  - 获取所有待办事项
  - 根据 ID 查找特定待办事项
  - 获取打印机信息（从环境变量）
  - 格式化并发送到网络打印机

### 42:00 - 环境变量处理
- 使用标准 Rust std::env 模块
- 示例：获取用户 ID、打印机 IP 等配置
- 建议：不要硬编码 URL 和配置信息

### 45:00 - 传输协议讨论
- 本地 MCP 服务器：使用 stdio 传输
- 远程 MCP 服务器：可以使用 HTTPS
- 观众提问：MCP 也应该支持远程服务器
- 讲师回应：当前主要演示本地服务器，但 Rust SDK 支持远程服务器

### 48:00 - MCP 服务器分发挑战
- 当前行业尚未找到标准的 MCP 服务器分发方式
- 各种方法：npx、pipx、uvx、cargo install
- 需要类似应用商店的 MCP 服务器市场
- Rust 二进制文件分发最简单：直接放在系统路径中

### 50:00 - 工具与函数分离
- 建议将业务逻辑（函数）与工具处理（MCP 工具）分离
- 工具负责参数验证和响应格式化
- 函数负责实际业务逻辑
- 提高代码可维护性和可测试性

### 52:00 - JSON Schema 版本问题
- 使用 JSON Schema 2020 版本
- 某些 IDE 可能存在兼容性问题
- 需要进一步调试和与工具团队合作解决

### 55:00 - 实际应用案例
- AWS IAM Policy Autopilot MCP 服务器
- 使用 Rust 构建
- 根据代码自动生成 IAM 策略
- 确定性生成，而非依赖 LLM 猜测

### 58:00 - 总结与资源
- 代码将在会后提供
- 推荐使用 MCP Inspector 进行开发调试
- Rust MCP SDK 文档完善，持续更新
- 鼓励开发者尝试使用 Rust 构建 MCP 服务器

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


关键技术要点：
- Rust MCP 服务器性能优势明显（启动速度快 40 倍）
- 使用 #[tool_router] 和 #[tool] 宏简化开发
- Arc 用于异步环境中的数据共享
- JSON Schema 支持类型安全的参数传递
- MCP Inspector 是必备的开发调试工具
- 建议分离工具层和业务逻辑层