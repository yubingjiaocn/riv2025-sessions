# AWS re:Invent 2025 会议总结：使用 Agentic AI 改善会员金融机构体验

## 会议概述

本次会议由 AWS 高级解决方案架构师 Uluri Ramanatan 和首席解决方案架构师 Muda Balis Braman 主讲，重点介绍了如何利用 Agentic AI 技术为会员制金融机构（信用合作社、保险公司等）构建智能贷款审批系统。

演讲者展示了一个基于 AWS Bedrock Agent Core 构建的端到端贷款发起系统（Loan Origination System）解决方案。该系统通过多智能体协作，能够自动处理贷款申请文档、提取数据、进行信用风险评估和合规检查，从而大幅缩短贷款审批时间，提升会员满意度。整个解决方案采用 Agent-to-Agent (A2A) 协议实现智能体间通信，使用 Strands Agents 框架开发，并部署在 Agent Core Runtime 上。演讲还特别强调了该系统的企业级特性，包括完整的可观测性、OAuth 身份认证、审计追踪等功能。

会议通过现场演示展示了从文档上传到最终决策的完整流程，并深入讲解了代码实现细节。演讲者还介绍了使用 AWS Kiro（一个 Agentic AI IDE）进行规范驱动开发的方法，展示了如何通过需求、设计和任务三个阶段系统化地构建企业级 AI 应用。

## 详细时间线

### 开场与介绍 (00:00 - 05:30)
- **00:00** - 会议开始，演讲者自我介绍：Uluri Ramanatan（高级解决方案架构师）和 Muda Balis Braman（首席解决方案架构师）
- **01:15** - 询问现场观众背景：信用合作社、保险公司、加拿大皇家银行等金融机构代表
- **02:30** - 介绍会议主题：展示如何使用 Agentic AI 改善会员制金融机构的贷款审批流程
- **03:45** - 调查观众对 Amazon Bedrock Agent Core 的了解程度
- **04:20** - 询问观众使用的其他 Agentic 框架：Autogen、Langraph、Crew AI 等

### Agent Core 平台介绍 (05:30 - 12:00)
- **05:30** - 介绍 Amazon Bedrock Agent Core：综合性 Agentic 平台，于去年 re:Invent 发布，10月中旬正式可用
- **06:15** - 讲解 Agent Core Runtime：无服务器计算组件，用于部署容器化智能体应用
- **07:00** - 介绍 Agent Memory：支持短期和长期记忆，实现多轮对话和跨智能体会话
- **08:10** - 讲解 Agent Core Gateway：托管的 MCP（Model Context Protocol）服务器，提供统一接口
- **09:20** - 介绍 Agent Core Identity：集中管理入站和出站 OAuth 认证授权
- **10:30** - 补充说明 Agent Core Browser 和 Code Interpreter 工具
- **11:15** - 强调 Agent Core Observability：支持 OpenTelemetry，集成 CloudWatch 进行日志、指标和追踪

### 解决方案架构讲解 (12:00 - 25:00)
- **12:00** - 开始讲解贷款发起系统架构
- **12:45** - 文档上传流程：申请人上传文档到 S3 存储桶，触发 Lambda 函数
- **13:30** - Supervisor Agent（监督智能体）：负责协调整个贷款处理工作流
- **14:15** - A2A 协议应用：Supervisor Agent 通过读取 Agent Cards 发现可用智能体
- **15:00** - 三个专业智能体：Document Agent（文档智能体）、Credit Risk Agent（信用风险智能体）、Compliance Agent（合规智能体）
- **16:20** - Document Agent 工作流程：验证文档并委托数据提取任务
- **17:30** - Bedrock Data Automation Agent：使用 AI 智能提取文档数据
- **18:45** - Agent Core Gateway 的 MCP 应用：作为工具访问的统一接口
- **20:00** - 数据验证与决策逻辑：验证失败时使用 Code Interpreter 发送邮件通知
- **21:15** - Credit Risk Agent：使用 Code Interpreter 调用机器学习模型进行信用评估
- **22:30** - Compliance Agent：执行合规检查
- **23:20** - 最终决策：批准、人工审核或拒绝贷款
- **24:15** - 自动生成 PDF 报告并上传到 S3，发送邮件通知申请人

### 现场演示 (25:00 - 38:00)
- **25:00** - 开始现场演示，切换到演示环境
- **25:45** - 观众提问：关于 MCP 与信用风险模型的特征工程
- **27:00** - 演示文档上传：贷款申请表、工资单、银行对账单、雇佣验证、税务申报等
- **28:15** - 展示 CloudWatch 日志中的 Agent Core Observability
- **28:45** - Supervisor Agent 发现专业智能体并启动工作流
- **29:30** - Document Agent 搜索并调用 Document Extraction Agent
- **30:20** - 使用 Bedrock Data Automation 提取数据（需要约1分钟）
- **31:00** - 讲解 A2A 协议的优势：适合企业级多智能体场景
- **32:15** - Document Agent 完成验证并返回结果
- **33:00** - Supervisor Agent 并行调用 Credit Risk 和 Compliance Agent
- **34:30** - Credit Risk Agent 使用 Code Interpreter 下载并调用 ML 模型
- **35:15** - 观众提问：如何防止文档注入攻击（通过 OAuth 认证和 Bedrock Guardrails）
- **36:20** - 观众提问：如何确保数字数据的准确性（BDA 提取的数据持久化在 S3）
- **37:00** - ML 模型返回 98% 的贷款偿还成功概率
- **37:30** - Supervisor Agent 完成决策逻辑，批准贷款并生成 PDF 报告

### 代码实现讲解 (38:00 - 50:00)
- **38:00** - 介绍使用 Kiro（AWS Agentic AI IDE）构建解决方案
- **38:45** - 询问观众对 Kiro 的了解程度
- **39:15** - Kiro 简介：独立的 Agentic AI IDE，擅长规范驱动开发
- **40:00** - 展示规范驱动开发流程：需求（Requirements）、设计（Design）、任务（Tasks）
- **41:00** - 需求文档：用户故事、A2A 协议要求、智能体发现、各智能体的验收标准
- **42:30** - 设计文档：架构图、Supervisor Agent 与专业智能体的通信流程
- **43:45** - 任务分阶段执行：Phase 1（基础设施设置）、Phase 2（智能体构建与部署）
- **44:30** - Phase 1 任务：设置 S3 存储桶、OAuth（Amazon Cognito）、Secrets Manager、IAM 角色、Agent Core Gateway
- **45:45** - Phase 2 任务：构建所有智能体并部署到 Agent Core Runtime
- **46:30** - 开始讲解 Supervisor Agent 代码实现
- **47:00** - 第一部分：导入库（Strands multi-agent A2A、A2A client、Code Interpreter 等）
- **47:45** - 第二部分：配置（AWS 区域、S3 存储桶、OAuth 令牌处理）
- **48:30** - 强调从 Secrets Manager 检索敏感信息（Client ID、Client Secret、Token URL）
- **49:00** - 第三部分：Prompt 定义（智能体角色、任务、智能体发现方法、标准操作程序）
- **49:45** - Prompt 中的指导原则：如何选择合适的智能体（例如文档验证智能体应包含"document validation"、"compliance"等关键词）

### 会议结束
- **50:00** - 会议内容结束，准备进入问答环节

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


关键技术要点：
- 使用 Strands Agents 框架和 Agent Core 平台
- A2A（Agent-to-Agent）协议实现智能体间通信
- Agent Core Gateway 作为 MCP 服务器
- Code Interpreter 实现动态代码生成与执行
- Bedrock Data Automation 进行智能文档数据提取
- OAuth 认证和 Bedrock Guardrails 保障安全
- OpenTelemetry 和 CloudWatch 提供完整可观测性
- Kiro IDE 支持规范驱动的企业级开发流程