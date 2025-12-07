# AWS re:Invent 2025 会话总结：使用 JSON Web Tokens 实现外部服务身份联合

## 概述

本次会话由 AWS Security Token Service (STS) 团队的 Rah Maharaj Puram（高级软件开发经理）和 Vishnavi Merugu（高级产品经理）主讲，重点介绍了 AWS 推出的一项全新功能：使用 JSON Web Tokens (JWTs) 将 AWS 工作负载安全地连接到外部服务。这项创新功能彻底解决了开发者长期面临的安全性与易用性之间的权衡难题。

传统上，当 AWS 工作负载需要访问外部服务（如 Azure、GCP、Databricks、Snowflake 等）时，开发者不得不管理长期凭证（如密码、访问密钥），这带来了巨大的安全风险。根据 AWS 客户事件响应团队的数据，三分之二的安全事件都源于未授权访问者使用有效的长期凭证进行初始访问。新功能允许用户使用现有的 AWS 凭证（IAM 角色、用户凭证）原生地交换为符合标准的 JSON Web Tokens，从而实现与第三方服务的安全连接，完全无需管理任何长期凭证。

该功能已在所有 AWS 商业区域、GovCloud 区域和中国区域上线，且不收取额外费用。通过简单的 API 调用（get-web-identity-token），用户可以获取短期的 JWT（默认 5 分钟有效期，最长可延长至 1 小时），并使用这些令牌与外部服务进行身份验证。整个过程大大简化了操作复杂度，同时显著提升了安全性。

## 详细时间线与关键要点

[00:00 - 01:30] 开场与问题引入
- 演讲者询问现场观众是否讨厌管理密码、访问密钥和长期凭证，几乎所有人举手表示认同
- 介绍演讲者：Rah Maharaj Puram（STS 工程负责人）和 Vishnavi Merugu（高级产品经理）

[01:30 - 03:00] 功能概述
- 宣布推出新功能：使用 AWS 凭证原生连接到外部服务
- 支持的外部服务包括：其他云服务提供商（Azure、GCP）、本地工作负载、SaaS 提供商（Databricks、Snowflake）
- 使用符合标准的 JSON Web Tokens (JWTs) 实现身份联合
- 无需复杂的变通方案或管理长期凭证

[03:00 - 04:30] 实时演示准备
- 演示目标：将 EC2 实例连接到 Azure 并调用 Azure API，无需创建 Azure 访问密钥或密码
- 展示 EC2 实例及其关联的 IAM 角色凭证
- 运行 aws sts get-caller-identity 命令验证当前凭证

[04:30 - 06:00] 演示步骤 1-2：启用功能并查看配置
- 使用 aws iam get-outbound-web-identity-federation-info 命令查看功能状态
- 返回结果包含两个关键元素：
  - 发行者标识符（Issuer Identifier）：账户的唯一 URL
  - JWT 发放已启用（jwtVendingEnabled: true）
- AWS 为账户创建非对称密钥对，并在发行者 URL 上托管公钥

[06:00 - 08:00] 演示步骤 3：获取 JWT
- 运行 aws sts get-web-identity-token 命令获取 JWT
- 指定受众参数（audience）为 Azure
- 选择签名算法 RS256
- 返回的 JWT 包含三部分：头部（header）、载荷（payload）、签名（signature）
- 默认过期时间为 5 分钟，可延长至 1 小时

[08:00 - 10:00] 演示步骤 4：解析 JWT 内容
- 对 JWT 进行 Base64 解码并解析 JSON
- 标准声明（Standard Claims）：
  - Subject：EC2 实例角色 ARN
  - Audience：目标服务
  - 过期时间、发行者 URL 等
- 自定义声明（Custom Claims）：
  - 命名空间为 sts.amazonaws.com
  - 包含 EC2 实例属性、ARN 信息、角色标签、会话标签等
- 附加用途：可用于内省授权上下文和故障排查

[10:00 - 12:00] 演示步骤 5-7：与 Azure 集成
- 将 JWT 发送到 Azure 令牌交换端点
- 使用 client_credentials 授权类型和 JWT 断言类型
- 成功获取 Azure 访问令牌
- 使用 Azure 令牌调用 Microsoft Graph API
- 展示 Azure 端的配置：仅需提供 Subject、Issuer URL 和 Audience

[12:00 - 14:00] 令牌验证机制
- 展示发行者 URL 上的公开端点：
  - .well-known/openid-configuration：包含支持的声明类型、算法和 JWKS URL
  - JSON Web Key Set (JWKS) 端点：托管 RSA 和 ECDSA 公钥
- Azure 通过这些端点获取公钥并验证 JWT 签名
- 用户可使用任何支持 JWT 的标准库进行验证

[14:00 - 16:00] 功能优势
- **增强安全性**：消除长期凭证，三分之二的安全事件源于长期凭证泄露
- **降低操作复杂度**：无需管理或轮换长期凭证，无需复杂的预签名 URL 或身份验证流程
- **互操作性**：设计为与多种外部云服务提供商、SaaS 提供商以及本地应用程序互操作

[16:00 - 18:00] JWT 声明详解
- **标准 OIDC 声明**：Subject、Audience、过期时间、唯一标识符、发行者 URL
- **AWS 自定义声明**（命名空间 sts.amazonaws.com）：
  - 身份上下文：AWS 账户 ID、源区域
  - 组织信息：组织 ID、组织路径
  - 主体标签：角色标签和会话标签
  - 计算上下文：EC2、Lambda 等特定声明
  - 联合提供商信息（如适用）

[18:00 - 19:30] 发行者 URL 设计
- 每个 AWS 账户拥有唯一的发行者 URL
- 设计目标：提供安全的默认体验并保证租户隔离

[19:30 - 21:00] 请求标签（Request Tags）
- 用户可通过 API 参数传递自定义键值对
- 这些标签会出现在 JWT 的 requestTag 部分
- 可用于外部服务的细粒度授权

[21:00 - 23:00] 访问控制
- 关键权限：sts:GetWebIdentityToken
- 拥有此权限的 IAM 主体可生成 JWT
- 可在多种策略类型中使用：SCP、RCP、基于身份的策略、VPC 策略
- **三个新条件键**：
  - sts:IdentityTokenAudience：限制允许的受众列表
  - sts:DurationSeconds：强制执行最大令牌生命周期（60 秒至 1 小时）
  - sts:SigningAlgorithm：指定签名算法（ES384 或 RS256）

[23:00 - 24:30] 可用性与成本
- 在所有 AWS 商业区域、GovCloud 区域和中国区域上线
- 无额外费用

[24:30 - 26:00] 最佳实践
- 用短期 JWT 替换所有 API 密钥和密码
- 尽可能缩短令牌生命周期以防止未授权访问
- 验证签名后再查看授权上下文
- 确保令牌由 AWS 发行且有效
- 利用自定义声明实现细粒度访问控制
- 不要记录令牌内容
- 随时可请求新令牌
- 始终通过 TLS 发送请求

[26:00 - 27:00] 资源与结束
- 提供博客文章和文档的 QR 码
- 博客文章包含功能演练
- 文档提供深入指南
- 感谢观众并提醒填写会话调查