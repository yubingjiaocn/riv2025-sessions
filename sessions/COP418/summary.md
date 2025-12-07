# AWS re:Invent 2025 - 监控生成式AI工作负载的质量和准确性 (COP418)

## 会议概述

本次会议由AWS高级技术客户经理Ganesh Samandan和高级解决方案架构师Ravita Sunkali共同主持，重点介绍了如何使用Amazon CloudWatch GenAI Observability监控生成式AI代理的质量和准确性。会议采用互动式现场演示的形式，展示了如何使用Strands SDK构建AI代理，并将其部署到Amazon Bedrock Agent Core运行时环境中。

演讲者强调，虽然构建AI代理相对简单，但在生产环境中大规模监控和观测这些代理却极具挑战性。为解决这一问题，AWS推出了CloudWatch GenAI Observability服务，提供开箱即用的指标洞察、零代码插桩、端到端提示追踪、数据保护策略以及全新的评估指标功能。该服务支持多种部署平台，包括Bedrock Agent Core、EKS、ECS和Lambda等，为客户提供了灵活的监控方案。

会议通过一个名为"Wagle AI"的宠物食品推荐代理的实际案例，详细演示了从本地开发、添加工具调用、部署到生产环境，再到使用CloudWatch进行全面监控的完整流程。演示还展示了如何使用AWS Distro for OpenTelemetry SDK进行零代码插桩，以及如何通过轨迹图可视化代理的决策过程。

## 详细时间线

00:00 - 开场介绍
- 演讲者自我介绍：Ganesh Samandan（高级技术客户经理）和Ravita Sunkali（高级解决方案架构师）
- 互动环节：询问观众re:Invent期间的步数统计

02:30 - 会议议程概览
- AI代理简介及演进历程
- 可观测性的重要性
- AI代理现场演示
- CloudWatch GenAI Observability探索
- 常见故障排查步骤
- 资源分享

04:00 - 生成式AI的演进历程
- 2023年：聊天机器人、提示工程、RAG系统的探索阶段
- 2024年：AI能力的采用阶段，关注安全性和负责任的AI
- 2025年：AI无处不在，企业追求真正的自动化和业务价值

06:30 - AI代理框架介绍
- 介绍Strands SDK及其他流行框架（LangChain、Crew AI等）
- 强调构建代理简单，但监控代理困难的挑战

08:00 - CloudWatch GenAI Observability核心功能
- 精选的开箱即用指标和洞察
- 零代码插桩（使用OpenTelemetry）
- 端到端提示追踪
- 数据保护策略
- 评估指标（周二CEO主题演讲中发布的新功能）

10:30 - CloudWatch GenAI Observability的灵活性
- 支持多种运行环境：Bedrock Agent Core、EKS、ECS、Lambda等
- 跨基础设施监控AI代理的能力

12:00 - 监控架构层次说明
- Session（会话）：用户与AI代理之间的完整对话
- Trace（追踪）：单个请求和响应
- Span（跨度）：追踪中的单个任务
- Subspan（子跨度）：更细粒度的详细信息（如单个API调用）

15:00 - 现场演示第一部分：构建基础AI代理
- 展示代码结构和导入模块
- 定义系统提示（system prompt）
- 使用Bedrock模型（Claude Sonnet 4）初始化代理
- 本地运行代理并进行交互测试

18:30 - 演示第二部分：添加工具调用功能
- 导入HTTP请求工具
- 导入Bedrock Agent Core应用装饰器
- 修改系统提示以调用微服务API
- 配置代理调用宠物搜索和食品数据库端点

22:00 - 启用可观测性
- 在requirements文件中添加AWS Distro for OpenTelemetry SDK
- 零代码插桩的工作原理：拦截调用、提取遥测数据、发送到CloudWatch
- 使用Agent Core Starter Kit部署代理的步骤

25:30 - 其他平台部署配置
- 在EC2、EKS等平台上部署时需要的额外环境变量配置
- 指定日志组、区域、协议等参数

28:00 - 演示第三部分：Pet Adoptions应用介绍
- 展示宠物收养应用的前端界面
- 介绍Wagle AI聊天机器人集成
- 实时演示：询问为2个月大的黑色小狗Max推荐食品

31:00 - CloudWatch GenAI控制台演示
- 导航到新的CloudWatch GenAI Observability仪表板
- 介绍两个主要仪表板：模型调用和Bedrock Agent Core
- 展示模型调用日志记录功能

33:30 - 查看模型调用详情
- 查看单个请求的输入和输出
- 展示系统提示和用户输入
- 查看模型响应详情

35:00 - Bedrock Agent Core仪表板
- 查看所有代理的统一视图
- 显示代理列表、托管环境、会话数、追踪数、错误和限流信息
- 展示运行时指标：会话、调用、vCPU消耗、内存使用

37:30 - 深入单个代理分析
- 点击Pet Food Agent查看详细视图
- 查看预配置的小部件：错误、延迟、会话数、追踪数
- 查看基础模型令牌使用情况的时间序列图
- 查看客户端错误和限流信息

40:00 - 会话级别追踪
- 使用会话ID过滤特定会话
- 查看会话中的所有追踪（每个问题对应一个追踪）
- 点击单个追踪查看详细信息

42:30 - 追踪详情和轨迹图
- 查看追踪指标：跨度数量、延迟、令牌使用、错误
- 展示新的轨迹图（Trajectory Map）可视化
- 显示代理决策的完整流程：调用Agent Core → Strands Agent → 三个循环（搜索宠物、获取食品、LLM推荐）

45:00 - 对话详情分析
- 点击聊天跨度查看完整对话
- 查看系统提示、用户提示和代理响应
- 查看工具调用消息和微服务返回的JSON数据
- 追踪数据如何作为用户消息输入到LLM

48:00 - 快速过滤功能
- 演示按错误过滤跨度
- 演示按高延迟过滤以定位性能瓶颈
- 查看每个LLM调用的输入和输出令牌数量
- 建议设置告警以监控令牌使用超限

50:30 - 资源分享
- 代码示例：在不同平台（Agent Core、EC2、ECS、EKS）上部署代理
- Strands和LangChain SDK的可观测性资源
- 文档和发布博客链接

52:00 - 结束语
- 感谢观众参与
- 鼓励填写调查反馈