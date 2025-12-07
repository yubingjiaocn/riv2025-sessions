# AWS re:Invent 2025 会议总结：使用 Agentic AI 改善会员金融机构体验

## 会议概述

本次会议由 AWS 高级解决方案架构师 Uluri Ramanatan 和首席解决方案架构师 Muda Balis Braman 主讲，重点介绍了如何利用 Agentic AI 技术改善会员制金融机构（如信用合作社、保险公司等）的贷款审批流程。

演讲者展示了一个基于 AWS Bedrock Agent Core 构建的企业级贷款发起系统（Loan Origination System）。该解决方案采用多智能体协作架构，通过 Agent-to-Agent (A2A) 协议实现智能体之间的通信。系统能够自动处理贷款申请文档、提取数据、进行信用风险评估和合规检查，最终生成审批决策，大幅缩短了贷款处理时间，提升了会员满意度。整个解决方案使用 AWS Strands Agents 框架开发，并部署在 Agent Core Runtime 上，展示了从文档上传到最终决策的完整自动化流程。

演讲还详细介绍了 Amazon Bedrock Agent Core 平台的核心组件，包括无服务器运行时、智能体内存管理、Agent Core Gateway（托管的 MCP 服务器）、身份认证服务以及可观测性功能。特别强调了该平台的模型无关性和框架无关性，支持开放协议如 Model Context Protocol (MCP)，并与 AWS CloudWatch 集成提供全面的日志、指标和追踪能力。

## 详细时间线与关键要点

### **开场介绍 (00:00 - 03:30)**
- 00:00 - 演讲者自我介绍，确认观众背景（主要来自保险公司和银行）
- 01:45 - 介绍会议主题：使用 Agentic AI 改善会员制金融机构的会员体验
- 02:30 - 说明解决方案基于 AWS Bedrock Agent Core 构建

### **Amazon Bedrock Agent Core 平台介绍 (03:30 - 12:00)**
- 03:30 - 询问观众对 Agent Core 的了解程度
- 04:15 - 介绍其他 Agentic 框架（Autogen, Langraph, Crew AI 等）
- 05:00 - Agent Core Runtime：无服务器计算组件，用于部署容器化智能体应用
- 06:20 - Agent Memory：支持短期和长期记忆，实现多轮对话和跨智能体会话
- 07:45 - Agent Core Gateway：托管的 MCP 服务器，作为统一接口连接各种工具和 API
- 09:30 - Agent Core Identity：集中管理入站和出站 OAuth 认证
- 10:50 - Agent Core Browser 和 Code Interpreter：浏览器工具和代码解释器工具
- 11:30 - 可观测性：支持 OpenTelemetry，与 AWS CloudWatch 集成

### **贷款发起系统架构讲解 (12:00 - 25:00)**
- 12:00 - 开始介绍贷款发起系统的整体架构
- 13:15 - 文档上传流程：申请人上传文档到 S3 存储桶，触发 Lambda 函数
- 14:30 - Supervisor Agent（监督智能体）：负责协调整个贷款处理工作流
- 15:45 - A2A 协议：Supervisor Agent 使用 A2A 协议读取其他智能体的 Agent Cards
- 16:50 - 三个专业智能体：文档智能体、信用风险智能体、合规智能体
- 18:20 - Document Agent（文档智能体）：验证文档并提取信息
- 19:40 - Bedrock Data Automation Agent：使用 AI 从文档和图像中智能提取数据
- 21:00 - Agent Core Gateway 作为 MCP 服务器：展示如何连接数据提取工具
- 22:30 - 数据验证流程：文档智能体验证所需数据完整性
- 23:45 - 失败处理：如数据缺失，使用 Code Interpreter 发送邮件通知申请人

### **信用风险和合规检查 (25:00 - 30:00)**
- 25:00 - Credit Risk Agent（信用风险智能体）：使用 Code Interpreter 调用 ML 模型
- 26:15 - ML 模型存储在 S3，智能体动态生成代码下载并交互
- 27:30 - 实际场景中可调用 SageMaker 端点
- 28:00 - Compliance Agent（合规智能体）：使用 Code Interpreter 执行合规检查
- 29:00 - 所有结果返回给 Supervisor Agent 进行最终决策

### **决策和输出 (30:00 - 33:00)**
- 30:00 - Supervisor Agent 根据标准操作程序（SOP）做出决策
- 30:45 - 三种可能结果：批准贷款、人工审核、拒绝贷款
- 31:30 - 使用 Code Interpreter 和 Amazon SES 发送邮件通知
- 32:15 - 自动生成 PDF 报告上传到 S3，供承销商审核

### **现场演示 (33:00 - 48:00)**
- 33:00 - 开始现场演示
- 34:00 - 观众提问：关于 ML 模型特征工程和 MCP 实现
- 35:30 - 演示文档上传：贷款申请、工资单、银行对账单、雇佣验证、税务申报
- 37:00 - CloudWatch 日志展示：Supervisor Agent 发现专业智能体
- 38:15 - 文档智能体开始搜索数据提取智能体
- 39:30 - 找到文档提取智能体，使用工具与 Bedrock Data Automation 通信
- 41:00 - 数据提取完成，文档验证智能体开始验证
- 42:30 - 验证通过，Supervisor Agent 并行调用信用风险和合规智能体
- 44:00 - 信用风险智能体使用 Code Interpreter 下载 ML 模型
- 45:15 - ML 模型预测：98% 成功还款概率
- 46:00 - Supervisor Agent 完成决策逻辑，批准贷款
- 47:00 - 展示自动生成的 PDF 报告，包含所有详细信息

### **安全性和准确性讨论 (48:00 - 52:00)**
- 48:00 - 观众提问：如何防止文档注入攻击
- 48:45 - 回答：使用 A2A 协议和 OAuth 认证保护智能体通信
- 49:30 - 补充：可使用 Amazon Bedrock Guardrails 防止提示注入
- 50:30 - 观众提问：如何确保数字数据在多个智能体调用中的准确性
- 51:15 - 回答：Bedrock Data Automation 提取的数据持久化在 S3，可审计追溯

### **开发工具介绍：Kiro Agent IDE (52:00 - 62:00)**
- 52:00 - 介绍使用 Kiro（Agent IDE）构建整个解决方案
- 53:00 - Kiro 是独立的 Agentic AI IDE，不是插件
- 54:00 - 规范驱动开发（Spec-driven Development）：遵循严格的 SDLC 流程
- 55:30 - 需求文档：用户故事、A2A 协议要求、智能体发现机制
- 56:45 - 每个智能体都有特定的验收标准
- 57:30 - 设计文档：Kiro 生成初稿，通过自然语言迭代优化
- 58:45 - 展示架构图：贷款请求流向 Supervisor Agent，再通过 A2A 分发
- 59:30 - 任务分解：分阶段实施
  - **Phase 1**：基础设施设置（S3、OAuth/Cognito、Secrets Manager、IAM 角色、Agent Core Gateway）
  - **Phase 2**：构建和部署所有智能体到 Agent Core Runtime

### **代码演示：Supervisor Agent (62:00 - 结束)**
- 62:00 - 代码分为四个部分
- 62:30 - 第一部分：库导入
  - Strands multi-agent A2A
  - A2A client 和 tool provider（用于智能体发现）
  - Code Interpreter 工具
  - A2A 服务器运行所需库
- 64:00 - 第二部分：配置
  - AWS 区域、S3 存储桶等参数
  - OAuth 令牌处理代码（智能体间通信的令牌刷新）
  - 从 Secrets Manager 检索客户端 ID、密钥和令牌 URL
- 66:00 - 第三部分：提示词（Prompt）
  - 定义智能体角色和任务
  - 如何发现其他可用智能体
  - 访问哪些工具进行智能体发现
  - **标准操作程序（SOP）**：选择智能体的标准（如文档验证智能体的 Agent Card 应包含"document validation"、"compliance"、"completeness"等关键词）
  - 指导智能体按预期方式执行

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


会议要点总结：
- 展示了企业级多智能体协作系统的完整实现
- 强调 A2A 协议在大规模智能体管理中的优势
- 突出可观测性、安全性和可审计性在生产环境中的重要性
- 介绍了 Kiro Agent IDE 的规范驱动开发方法
- 演示了如何通过提示工程和 SOP 指导智能体行为