# AWS re:Invent 2025 Bedrock Agents 会议总结

## 会议概述

本次会议由来自巴西圣保罗的高级技术讲师 Maril Breto 主讲,重点介绍了 AWS Bedrock 在智能代理（Agentic Systems）领域的最新发展。会议探讨了客户如何从简单的聊天机器人应用转向更复杂的、能够与整个生态系统集成的 LLM 解决方案。这些解决方案不仅能处理云内外的组件集成,还能处理专业领域的真实数据,从而提供实际的业务洞察。

会议系统地介绍了三种主要的代理实现方式:Bedrock Agents（托管解决方案）、Inline Agents（动态配置方案）和 Agent Core（模块化定制方案）。讲师通过多个实际演示展示了这些技术的应用场景,包括客户支持系统、贷款审批流程等。会议还深入讲解了智能代理系统的关键组件,如 Guard Rails（安全防护）、Knowledge Bases（知识库）、Memory（记忆管理）、Multi-Agent Collaboration（多代理协作）以及 Bedrock Flows（工作流编排）等核心功能。

Agent Core 作为最新推出的服务（约6个月前发布）,为开发者提供了高度模块化的架构,支持多种开源框架和模型选择,甚至可以使用 AWS 之外的模型。这种灵活性使得开发者能够根据具体需求构建定制化的智能代理系统,同时保持各组件的独立性和可扩展性。

## 详细时间线

00:00:00 - 开场与会议介绍
- 讲师发放贴纸与观众互动
- 介绍过去一年 LLM 应用的重大转变:从简单文本生成到复杂生态系统集成
- 会议主题:Bedrock Agents 和 Agent Core 预览

00:01:30 - 会议议程概览
- 不同类型的代理配置
- Bedrock Agents、Inline Agents、多代理协作
- 使用 Bedrock Flows 编排结构化工作流
- Agent Core 介绍

00:02:00 - 智能代理系统生态系统
- 智能代理系统类似微服务架构,包含多个关键组件
- 四大核心组件:代理工作流、模块化组件、持续评估框架、反馈循环

00:03:30 - 代理工作流程
- 用户输入 → 代理检查 → 执行操作 → 返回响应
- 可选的人工审核环节（Human in the Loop）

00:04:00 - 系统组件详解
- Foundation Model:用于推理循环的基础模型
- Knowledge Bases:存储专有数据的知识库（S3、数据库等）
- Guard Rails:安全防护功能
- APIs 和工具:外部 API 集成
- Memory Management:上下文记忆管理
- Multi-Agent Collaboration:多代理协作模式

00:06:00 - 持续评估框架
- 指标收集的重要性
- 人工评估和 LLM 评判机制
- Ground Truth 功能（通过 SageMaker 控制台）

00:07:00 - Bedrock Agents 介绍
- 托管解决方案,适合内置需求
- 支持单代理和多代理协作
- 可配置模型、指令、知识库和 Lambda 函数操作

00:08:30 - Inline Agents
- 动态配置方案
- 每次调用可更改参数、模型、指令、知识库和操作
- 适合实验场景和特定动态需求

00:09:30 - Agent Core
- 模块化生态系统
- 组件独立:执行环境、内存、网关、身份控制
- 支持不同框架和任何模型（包括 AWS 外部模型）

00:10:30 - Bedrock Agents 工作原理
- 客户提示 → 代理分解任务 → 执行逻辑 → 观察结果 → 返回答案
- 组件:Foundation Model、Action Group、Knowledge Bases、Code Interpreter、Memory

00:12:00 - 银行助手架构示例
- Guard Rails 作为第一道防线过滤提示
- 内部操作使用 Lambda 函数
- Knowledge Bases 通过 RAG 提供数据
- 向量数据库（OpenSearch Serverless）存储文档的数学表示

00:14:00 - Guard Rails 详解
- 确定性控制:屏蔽词列表、合规性词汇
- 概率性控制:暴力、不当行为、仇恨言论等类别的阈值设置
- PII 控制:阻止或掩码个人身份信息
- 上下文基础检查:验证 RAG 质量和响应准确性

00:17:30 - Action Groups
- 配置代理指令
- 使用 OpenAPI 模板定义工具
- Lambda 函数执行逻辑
- 演示:时间查询功能（查询圣保罗的日期和时间）

00:19:00 - Memory（记忆管理）
- 三步配置:启用记忆、设置持续时间（最多365天）、选择加载的历史会话数
- 使用摘要而非完整对话
- 旅行助手示例:记住用户偏好（西班牙旅行、每天500美元预算）

00:21:30 - Inline Agents 详解
- 使用 invoke inline agent API
- 动态配置:指令、模型（Claude 3 Haiku）、Action Group、Code Interpreter
- 示例:Octank Inc. 员工 HR 助手

00:23:00 - 多代理协作模式
- Supervisor Agent 协调多个专业代理
- 客户支持场景演示:
  - Intent Classification Agent:分类请求
  - Tech Specialist Agent:处理技术问题
  - Policy Agent:检查内部政策
  - Support Case Lookup:查询现有工单

00:25:30 - 多代理协作演示
- 系统超时问题工单示例
- Supervisor Agent → Intent Classification → Tech Specialist
- 追踪功能显示模型推理过程

00:27:00 - Bedrock Flows 介绍
- 完全托管的工作流编排功能
- 构建块:Lambda 函数、Lex 聊天机器人、Knowledge Bases、Prompt 模板
- 五类节点:逻辑、数据、代码、代理、输出
- 两个 API:Bedrock Agents API（生命周期管理）、Runtime API（执行）

00:29:00 - Bedrock Flows 演示:贷款审批
- 输入:收入、债务、期限、金额、信用评分
- Lambda 函数计算最大可负担贷款
- 条件判断:批准或拒绝
- 拒绝路径:生成拒绝信
- 批准路径:代理询问更多问题以生成合同
- 追踪功能显示完整执行流程

00:33:00 - Agent Core 介绍
- 6个月前推出的新服务
- 高度定制化需求的解决方案
- 支持多种开源框架和任何模型
- 模块化架构:执行环境、模型、网关、浏览器、代码解释器、身份控制、内存、可观测性

00:35:00 - Agent Core Runtime
- 构建 Recipe:模型、框架、Runtime 装饰器、身份配置、可观测性配置
- 打包为 Docker 镜像并存储在 ECR
- 请求时启动 Runtime
- 空闲15分钟后终止（可延长至8小时）

00:37:00 - Agent Core Identity
- Inbound:选择认证提供商（IAM、Cognito、OAuth）
- Token 存储
- Outbound:Token 交换或生成新 Token
- AWS 内部可使用 IAM Signature v4

00:39:00 - Agent Core Gateway
- 存储安全 Token
- 暴露工具（MCP 服务器）
- 支持内部和外部工具调用
- 路由选项:关键词、意图、语义搜索

00:40:30 - Agent Core Memory
- 短期和长期记忆配置
- 长期记忆最多365天
- 三种存储类型:对话摘要、用户偏好、语义记忆
- Serverless 存储（自动管理 S3 和 DynamoDB）

00:42:30 - Agent Core Browser
- 无头浏览器（Playwright）
- Serverless 隔离会话
- 可流式传输浏览器操作
- 使用 Nova Act 解析信息
- 使用 DCV 查看流式传输
- CDP 命令执行浏览器操作
- 生成临时签名 URL

00:45:00 - Agent Core Code Interpreter
- 系统提供商:默认 Python、JavaScript、TypeScript 库
- 终端访问
- 临时文件系统（会话结束后删除）
- Micro VM 执行
- 自定义代码解释器:支持自定义依赖库

00:46:30 - Agent Core Observability
- CloudWatch 中的 GenAI 仪表板
- 会议结束