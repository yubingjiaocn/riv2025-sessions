# AWS re:Invent 2025 会议总结：使用 Kiro 转型金融服务 AI 开发生命周期

## 会议概述

本次分会由 AWS AI Hero Vivek Wilson 主讲，重点介绍了如何使用 Kiro（原 Q）通过规范驱动工作流来转型金融服务行业的 AI 开发生命周期（AIDLC）。演讲者拥有 27 年行业经验，曾担任 AWS 社区构建者和大使。会议聚焦于解决企业在开发过程中面临的三大核心挑战：技术债务、合规负担和安全漏洞。

Kiro 规范驱动工作流包含四个核心组件：Kiro Specs（需求、设计、架构和任务的声明式集合）、Agent Steering（代理引导，通过规则强制执行合规性）、Agent Hooks（自动化处理文档更新和策略即代码）以及 MCP 服务器功能（连接组织数据以提高代码准确性）。演讲者通过实际案例展示了如何使用这些功能在不到一小时内构建贷款审批微服务，并自动化处理技术债务、实现左移合规检查，以及通过自定义代理优化上下文管理。所有示例代码均可在演讲者的 GitHub 仓库中获取。

## 详细时间线

00:00 - 开场介绍
- 演讲者 Vivek Wilson 自我介绍，说明 AWS AI Hero 是机器学习英雄类别的新名称
- 询问现场观众使用 Kiro 的情况，提到本届 re:Invent 有 99 场关于 Kiro 的会议

01:30 - 会议议程
- 介绍将讨论金融服务开发周期中的挑战
- 说明如何通过规范驱动工作流和 Kiro 辅助 AIDLC
- 承诺分享实践示例和最佳实践，所有内容将在 GitHub 仓库中提供

02:15 - 企业开发面临的三大挑战
- **技术债务**：超过 20% 的 IT 预算用于处理技术债务问题，开发人员每天花费超过一小时修复 Lambda 运行时问题、生命周期结束支持和容器镜像验证
- **合规负担**：受监管行业面临严重的罚款风险，即使单行代码更改也需要通过 5 分钟的完整流水线，开发体验不佳
- **安全债务**：事件堆积和未修补的开源依赖漏洞导致组织安全债务巨大

04:00 - Kiro 规范驱动工作流介绍
- Kiro Specs：需求、设计、架构和任务的集合，以声明式方式生成代码
- Agent Steering：通过代理引导强制执行合规性，即使 LLM 不是确定性的
- Agent Hooks：自动化处理文档更新等手动任务，实现策略即代码
- MCP 服务器：连接 Confluence、SharePoint、Jira 等组织数据，提高代码准确性
- Kiro CLI：使用子代理提高生产力和上下文工程

06:00 - Agent Steering 实践案例
- 演示构建贷款审批微服务：API Gateway + Lambda 后端 + DynamoDB + CloudWatch
- 使用 CDK（TypeScript）和 Python 在不到一小时内完成构建
- 指出问题：Claude Opus 4.5 生成的代码使用过时的 CDK 库（2.0 而非 2.170）和已停止支持的 Python 3.9 运行时

08:30 - 全局 Agent Steering 解决方案
- 介绍全局 Agent Steering：在工作站上定义一个引导文件，应用于所有项目
- Steering 文件是用纯英文编写的规则集，可指示使用稳定版本、不硬编码密钥等
- 建议使用"must"、"critical"等关键词，Claude 模型对这些词特别敏感
- 演示通过一个提示应用 Steering 文件，在 1 分钟内更新所有包并消除技术债务

10:00 - 代码质量检查工具
- Kiro 是 VS Code 的分支（类似 Windsurf 和 Cursor）
- 可安装 Pylint（Python）和 ESLint（TypeScript）等 Linting 扩展
- 这些扩展可在 IDE 中快速分析代码错误和最佳实践违规
- 注意：这些扩展需要手动启用，默认未启用

11:30 - Agent Hooks 和策略即代码
- 介绍 AWS CFN Guard 开源工具：领域特定语言（DSL），可读取 PCI、NIST、HIPAA 等框架的规则集
- CFN Guard 可在 CloudFormation 模板、Kubernetes 配置文件和 Terraform 计划上运行规则
- 演示两步流程：本地运行 CFN Guard 验证配置，通过后再部署

13:00 - 使用 Agent Hooks 自动化合规检查
- 演示创建 Agent Hook，在基础设施文件保存时自动触发 CFN Guard 检查
- Hook 自动运行规则并在 Kiro IDE 中显示通过的规则
- 实现左移策略，无需手动执行

14:30 - AWS Toolkit 集成
- 介绍 AWS CloudFormation Language Server 的新功能
- 可在 IDE 中直接显示 CloudFormation 堆栈错误，无需切换到 AWS 控制台
- 可在 AWS Toolkit 设置中应用 Guard 规则
- 建议使用 JSON 格式而非 YAML，因为 YAML 的内置扩展（如感叹号）有时不能很好地与 CDK Guard 配合
- 演示在堆栈中用蓝色波浪线高亮显示 YAML 配置错误

16:30 - MCP 工具和服务器
- 介绍 Kiro.dev 网站简化了 MCP 服务器的安装
- 现在有统一的 AWS MCP 服务器，可一键安装和启用
- 支持环境变量，简化团队间 MCP JSON 文件的共享
- 团队成员使用时需要本地批准环境变量

18:00 - Diagrams MCP 服务器
- 演讲者最喜欢的 MCP 工具
- 以前创建 Draw.io 架构图需要一小时，现在使用 Diagrams MCP 不到一分钟
- 介绍其他有用的 MCP 服务器：Headless Chrome Dev Tools Browser，用于调试 UI 和前端应用

19:30 - Kiro CLI 和自定义代理
- Kiro CLI 是 Q CLI 的重新品牌
- 强调上下文是编码辅助的关键
- 问题：大型代码库中，4-5 个问题后上下文填充到 100%，需要重新开始

20:30 - 自定义代理解决方案
- 创建专用代理：审查代理、架构代理、合规代理
- 专业化代理优化上下文，避免上下文窗口耗尽
- 两步流程：使用 /agent create 命令创建自定义代理，提供 JSON 配置
- 代理配置包括：MCP 服务器名称、提示和 Steering 文件
- 建议根据任务使用特定 MCP 服务器（如前端任务使用 Chrome Dev Tools）

22:00 - 启动自定义代理
- 使用 /agent launch 命令在后台启动代理，完成任务后报告状态
- 使用 /agent swap 命令将代理切换到前台作为默认代理

23:00 - 结束语
- 引用亨利·福特名言，将其与 Kiro 转型金融服务和其他行业的 AI 代理编码相类比
- 提供 GitHub 仓库 QR 码，包含所有演示示例
- 邀请观众在 LinkedIn 上联系，会后交流 Kiro 使用经验
- 提醒完成会议调查