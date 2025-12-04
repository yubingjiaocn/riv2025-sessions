# AWS re:Invent 会议总结：使用 Amazon Bedrock Agent Core 构建多租户 SaaS 代理

## 会议概述

本次会议是一场 400 级别的技术深度分享，主题聚焦于如何使用 Amazon Bedrock Agent Core 构建多租户 SaaS 代理解决方案。演讲者 Bill Tar（首席合作伙伴解决方案架构师）和 Uday（高级首席合作伙伴解决方案架构师）详细介绍了将传统 SaaS 最佳实践应用于 AI 代理架构的方法。

会议围绕一个实际的示例架构展开，该架构包含一个编排代理（orchestrator agent），可以调用知识库代理、日志分析代理和编码代理来解决代码问题。演讲者强调这不是概念演示，而是有完整可用代码和配套 workshop 的真实解决方案，参会者可以通过 GitHub 获取代码或参加现场 workshop 进行实践。

会议系统性地解决了五大 SaaS 架构挑战：租户入驻（tenant onboarding）、SaaS 身份认证、数据分区、租户隔离和可观测性。演讲者详细讲解了如何在 Agent Core 的各个组件（Runtime、Gateway、Identity、Memory）中实现这些 SaaS 最佳实践，特别强调了在 silo（专用）和 pool（共享）两种部署模型下的不同实现策略。

## 详细时间线

### 开场与背景介绍
[00:00 - 02:30] 演讲者开场致谢，介绍会议主题为使用 Amazon Bedrock Agent Core 构建多租户 SaaS 代理，这是一场 400 级别的技术深度会议，需要参会者具备一定的编码和 Agent Core 背景知识。

[02:30 - 04:00] 介绍配套 workshop，强调所有演示内容都基于真实可用的代码库，参会者可以通过 GitHub 获取或参加现场 workshop 实践。

[04:00 - 06:30] 展示示例架构概览，包含 Agent Core Runtime（运行代理代码）、多个专用代理（编排代理、知识库代理、日志分析代理、编码代理）、Agent Core Gateway（管理工具）、Agent Core Identity（身份管理）和可观测性组件。

### SaaS 架构挑战
[06:30 - 09:00] Bill 介绍五大 SaaS 架构挑战：
- 租户入驻（快速让客户从了解产品到获得价值）
- SaaS 身份认证（授权和认证用户，传播租户上下文）
- 数据分区（逻辑或物理隔离租户数据）
- 租户隔离（定义租户访问权限的策略）
- SaaS 可观测性（监控租户健康状况）

### Agent 和 Agent Core 基础
[09:00 - 12:30] Uday 定义 Agent 的核心组件：
- 运行在计算环境中的代码
- 配置大语言模型
- 工具代码（扩展功能，访问外部资源）
- 身份管理（入站和出站调用授权）
- 内存管理（存储对话上下文）
- 可观测性（监控代理行为）

[12:30 - 15:30] 介绍 Amazon Bedrock Agent Core 如何解决这些挑战：
- Agent Core Runtime：部署和扩展代理代码
- Agent Core Gateway：部署工具代码（MCP as a service）
- Agent Core Identity：处理入站和出站授权
- Agent Core Memory：短期和长期内存管理
- Agent Core Observability：捕获指标和理解代理行为

### 多租户部署模型
[15:30 - 19:00] Bill 讲解多租户部署模型：
- Silo/专用模型：每个租户独立的完整技术栈，架构简单但运营成本高
- Pool/共享模型：共享基础设施，需要运行时决策和权限检查，架构复杂但效率高
- 混合/桥接模型：部分组件共享，部分组件专用

[19:00 - 22:00] Uday 展示多租户代理实现：
- Silo 代理：专用 Agent Core Runtime、专用 Memory、专用 Gateway 和专用资源
- Pool 代理：共享 Agent Core Runtime、共享 Memory、共享 Gateway 和共享资源
- 引入短期内存（存储会话级原始事件）和长期内存（存储跨会话摘要和偏好）概念

### 租户入驻解决方案
[22:00 - 25:30] Uday 讲解租户入驻最佳实践：
- 构建 SaaS 控制平面（包含入驻服务、租户配置服务、租户管理服务、租户注册服务）
- 通过控制平面部署租户特定架构到应用平面
- Silo 模型在租户入驻时配置专用资源
- Pool 模型可以预先配置共享资源
- 通过定价层级（基础层对应 pool 模型，高级层对应 silo 模型）向客户展示不同模型

### SaaS 身份认证深度解析
[25:30 - 29:00] Bill 讲解 SaaS 身份认证基础：
- 使用身份提供商（示例中使用 Amazon Cognito）管理租户用户
- 采用每租户一个用户池的策略建立租户边界
- 在用户上配置自定义声明/属性（如租户 ID、状态、层级等元数据）
- JWT token 作为传递数据的载体

[29:00 - 31:00] 解释 JWT token 结构：
- Identity token：自动继承所有自定义声明
- Access token：默认不继承自定义声明，需要使用 pre-token generation Lambda trigger 将自定义声明复制到 access token
- Access token 在 Agent Core 中传递使用

### Agent Core Identity 实现
[31:00 - 36:00] Uday 详细讲解入站授权：
- 用户通过身份提供商认证获得 JWT token（包含用户和租户信息）
- 租户使用 JWT token 调用 Agent Core Runtime 中的代理
- 配置 Agent Core Runtime 与 Agent Core Identity
- 配置 Agent Core Identity 与身份提供商
- Agent Core Identity 验证入站 JWT token 并授权调用

[36:00 - 42:00] 讲解出站授权机制：
- 对于 AWS 资源：使用 IAM 执行角色附加到 Agent Core Runtime
- 对于需要 OAuth token 或 API key 的外部资源：
  - 配置 Agent Core Identity 与外部凭证提供商
  - Agent Core Identity 为每个代理创建工作负载身份（workload identity）
  - 支持人工审批流程（human in the loop）
  - Agent Core Runtime 请求 Agent Core Identity 生成访问 token
  - Agent Core Identity 将请求映射到工作负载身份，再映射到配置的身份提供商，生成工作负载访问 token
  - 代码中只需使用 @iterate requires access token 注解即可获取 token

[42:00 - 44:30] 多租户出站授权：
- 外部资源可能需要 token 中包含额外的租户元数据
- 外部身份提供商可以自定义工作流，在生成访问 token 时添加自定义声明
- 利用之前讲解的 pre-token generation 机制实现

[44:30 - 47:00] Agent Core Gateway 的身份管理：
- 工具代码部署在 Agent Core Gateway 中
- Agent Core Runtime 使用 JWT token 调用 Agent Core Gateway
- 配置 Agent Core Gateway 与 Agent Core Identity 进行授权
- Gateway Interceptor 功能可以拦截请求，获取所有 headers 和 JWT token，提取租户上下文供工具使用

### 数据分区策略
[47:00 - 49:00] Bill 简要介绍数据分区概念：
- 数据分区是将租户数据分隔到逻辑或物理存储桶
- 在 Agent Core 中主要涉及两个领域：Agent Core Memory 和下游 AWS 资源（如知识库、DynamoDB）

[49:00 - 54:00] Uday 详解 Agent Core Memory 数据分区：

Silo 模型：
- 每个租户专用 Agent Core Runtime、专用代理、专用 Memory
- 短期内存事件创建需要：Memory ID（创建 Memory 时生成）、Session ID（每个会话唯一）、Actor ID（代理或用户的唯一标识）
- 数据分区约定：Actor ID = tenant_id:subject（从 JWT token 获取），实现按租户用户分区
- 长期内存使用命名空间（namespace）存储信息，命名空间中包含 Actor ID 实现分区

Pool 模型：
- 共享 Agent Core Runtime、共享代理、共享 Memory
- 使用相同的 Actor ID 约定（tenant_id:subject）在共享内存中实现数据分区
- 如果只需按租户分区（不按用户），Actor ID 可以只使用 tenant_id

[54:00 - 58:00] AWS 资源数据分区：

知识库（Knowledge Base）：
- Silo 模型：每个租户专用知识库，配置专用向量数据库
- Pool 模型：共享知识库配置共享向量存储，在数据摄取时附加租户 ID 作为元数据标签实现逻辑分区

会议在此处字幕截断，但已经覆盖了核心的架构挑战和解决方案。