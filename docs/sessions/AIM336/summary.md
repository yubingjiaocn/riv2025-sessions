# AWS re:Invent 2025 会议总结：使用 AI Agent 构建弹性工作负载

## 一、会议概述

本次 AWS re:Invent 2025 分会场主题聚焦于如何利用生成式 AI 和 Agent 技术来提升应用程序的弹性（Resilience）。演讲者引用了 Werner Vogels 的著名格言"一切都会失败"（Everything fails all the time），强调在构建应用时必须为故障做好准备，尤其是在人道主义工作负载等关键场景中，系统的高可用性和恢复能力至关重要。

会议的核心内容是演示如何使用 Anthropic 的 Strands Agent 框架构建一个 AI 驱动的弹性顾问（Resilience Advisor）。该 Agent 能够自动分析 AWS 账户中的工作负载，识别弹性漏洞，并根据恢复时间目标（RTO）和恢复点目标（RPO）提供可操作的改进建议。演讲者通过现场编码演示，逐步展示了如何从一个基础 Agent 发展到具有会话状态管理和多工具集成能力的完整解决方案。

整个演示强调了 Agentic AI 的核心价值：通过赋予 AI 自主行动能力，结合大语言模型的推理能力和各种工具的执行能力，可以大幅简化复杂的弹性分析工作。这种方法不仅降低了构建高弹性系统的技术门槛，还能够根据不同的业务需求动态调整评估标准。

## 二、详细时间线与关键要点

### **00:00 - 开场与弹性基础概念**
- 引用 Werner Vogels 名言："一切都会失败，为故障而构建则不会失败"
- 强调在人道主义工作负载中高可靠性的重要性（如洪水等紧急情况下不能出现 404 或超时）
- 介绍构建弹性系统的挑战：高可用性、自愈能力、多区域部署等复杂技术任务

### **03:30 - AWS 弹性心智模型三要素**
1. 高可用性（High Availability）：应用的主站点如何抵御常见故障（服务器宕机、网络中断等）
2. 灾难恢复（Disaster Recovery）：当主站点受到重大影响时如何故障转移到备用站点
3. 持续改进（Continuous Improvement）：基于故障经验不断优化应用弹性

### **05:45 - 五大故障类别（SEAMS 框架）**
- **S - 单点故障（Single Points of Failure）**：任何单一组件失败会导致整个应用崩溃
- **E - 过载（Excessive Load）**：应用能否承受突发流量增长，是否具备弹性扩展能力
- **E - 过度延迟（Excessive Latency）**：应用能否处理网络中断和不可预测的延迟
- **M - 配置错误和 Bug（Misconfiguration and Bugs）**：能否快速回滚或修补问题
- **S - 共享命运（Shared Fate）**：跨应用的共同依赖是否会导致级联故障

### **09:20 - Agentic AI 架构介绍**
- 使用 Amazon Bedrock 作为基础模型推理引擎
- 集成 AWS Cloud Control API（通过 MCP 服务器）进行资源 CRUD 操作
- 集成 AWS 文档工具提供最佳实践建议
- Agent 能够自主调查工作负载、查找文档并生成评估报告

### **12:00 - 实战演示：构建基础 Agent**
- 使用 Strands Agent 框架创建最简单的 Agent
- 系统提示词：定义 Agent 为 AWS 弹性专家，输出 GitHub Markdown 格式
- 实现两个核心方法：
  - ping() 方法：返回健康状态
  - invocations() 方法：处理用户请求并调用 Agent

### **16:30 - 创建交互式客户端**
- 编写 Python 脚本与 Agent 交互
- 实现持续循环接收用户输入
- 通过 POST 请求发送提示词到 /invocations 端点
- 使用 Markdown 库美化输出结果

### **19:00 - 第一次测试：基础 Agent 的局限性**
- 提示词："我有一个标签为 aws:cloudformation:stack-name=food-agent 的工作负载，帮我理解其弹性"
- Agent 返回通用建议（如考虑多可用区部署）但未实际分析具体工作负载
- 结论：需要赋予 Agent 访问 AWS 账户的能力

### **21:45 - 增强 Agent：添加工具和详细提示词**
- 扩展系统提示词：
  - 要求仅执行非变更操作（non-mutative actions）
  - 定义输出格式：RTO/RPO 分析 + 五大弹性类别评分（A-F 字母等级）
- 指定使用 Claude Sonnet 3.5 模型（通过 Bedrock）
- 设置温度参数控制输出随机性

### **24:30 - 实现自定义工具：calculate_letter_grade**
- 输入参数：critical、high、medium、low 级别的弹性漏洞数量
- 评分逻辑：
  - 存在 critical 漏洞 → D
  - 存在 high 漏洞 → C
  - 存在 medium 漏洞 → B
  - 否则 → A
- 使用 @tool 装饰器将方法注册为 Agent 工具

### **27:00 - 集成 AWS 工具：use_aws**
- 从 Strands SDK 导入内置的 use_aws 工具
- 该工具封装了 AWS Cloud Control API 的所有复杂性
- Agent 可自动识别需要查询 CloudFormation 堆栈并获取资源信息
- 强调安全性：在生产环境应使用只读权限角色

### **30:15 - 第二次测试：具备工具的 Agent**
- 提示词："我有标签为 food-agent 的工作负载，RTO 24 小时，RPO 12 小时，帮我理解弹性"
- Agent 自动执行：
  1. 调用 use_aws 工具查询 CloudFormation 堆栈
  2. 检索堆栈中的所有资源
  3. 分析每个资源的弹性特性
  4. 多次调用 calculate_letter_grade 计算评分
- 返回结果：大部分评分为 C 和 D（冗余性 D、容量 D、延迟 D、正确性 C、故障隔离 D）

### **34:00 - 发现问题：缺少会话状态**
- 尝试追问："这些评分是否真实反映了我的 RTO 和 RPO？"
- Agent 回复："我没有关于之前评分或 RTO/RPO 值的上下文"
- 问题根源：每次请求都是独立的，没有会话记忆

### **36:30 - 添加会话管理功能**
- 创建 S3 存储桶用于存储会话数据（reinvent-session-data）
- 实现 S3SessionManager：
  - 接收客户端传入的 session_id
  - 将会话数据存储到 S3 指定前缀（如 prod/）
- 修改客户端：生成 UUID 作为 session_id 并随请求发送
- 在 Agent 初始化时添加 session_manager 参数

### **40:00 - 第三次测试：具备会话状态的 Agent**
- 重新提问相同的工作负载分析请求
- Agent 返回相同的 C/D 评分
- 追问："考虑到我的 RTO 和 RPO，这些评分准确吗？"
- Agent 响应：
  - "你说得对，这些评分不合理"
  - "对于 24 小时 RTO 和 12 小时 RPO，许多我标记为 critical 的问题实际上是优化项"
  - 重新计算评分：大部分提升到 B 和 C（冗余性 B、容量 B、延迟 C、正确性 B）

### **43:30 - 讨论流式响应优化**
- 当前实现：等待完整结果后一次性返回
- 改进建议：实现 token 流式传输，提供类似聊天机器人的实时体验
- 适用场景：需要更强交互性的用户界面

### **45:00 - 预告：集成 MCP 服务器**
- 已展示的工具类型：
  1. Strands Agent 内置工具（use_aws）
  2. 自定义 Python 工具（calculate_letter_grade）
- 下一步：演示如何集成第三方 MCP（Model Context Protocol）服务器
- MCP 是标准化协议，允许应用为 LLM 提供上下文和工具

### **46:30 - 会议核心要点总结**
- 构建弹性系统的复杂性可以通过 Agentic AI 大幅降低
- Strands Agent 框架提供简洁的 API 用于创建具备工具使用能力的 Agent
- 会话管理对于多轮对话至关重要
- 通过调整 RTO/RPO 参数，同一工作负载可获得不同的弹性评估结果
- 安全最佳实践：生产环境使用最小权限原则（只读访问）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


技术栈总结：
- **框架**：Anthropic Strands Agent
- **LLM**：Claude Sonnet 3.5（通过 Amazon Bedrock）
- **工具集成**：AWS Cloud Control API、自定义 Python 函数、MCP 服务器
- **会话存储**：Amazon S3
- **输出格式**：GitHub Markdown