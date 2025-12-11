# AWS re:Invent 2025 会话总结：外向身份联邦新功能

## 会议概述

本次技术会话由AWS安全令牌服务(STS)高级软件开发经理Ram Maharajapuram和高级产品经理Vaishnavi Merugu主讲，重点介绍了AWS新推出的外向身份联邦功能。该功能旨在解决开发者在管理密码、访问密钥等长期凭证时面临的安全与易用性权衡问题。

新功能允许用户使用AWS凭证原生连接到外部服务，包括其他云服务提供商(如Azure、GCP)、SaaS提供商(如Databricks、Snowflake)以及本地工作负载。通过标准化的JSON Web Token(JWT)实现安全连接，无需管理任何长期凭证，显著提升了安全性并降低了运维复杂度。

## 详细时间线与关键要点

### 0:00-3:00 会话开场与问题背景
- 主讲人介绍：Ram Maharajapuram(STS工程负责人)和Vaishnavi Merugu(高级产品经理)
- 现场调研：几乎所有与会者都讨厌管理长期凭证
- 新功能概述：使用AWS凭证原生连接外部服务，支持云服务提供商、SaaS提供商和本地工作负载

### 3:00-8:00 实时演示：EC2连接Azure
- 演示环境：EC2实例连接Azure API，无需创建Azure访问密钥
- 步骤1：检查当前凭证 - 使用aws sts get-caller-identity确认EC2实例角色凭证
- 步骤2：启用外向身份联邦功能 - 使用aws iam get-outbound-web-identity-federation-info
- 返回结果包含发行者标识符和JWT启用状态
- AWS为账户创建非对称密钥对和唯一标识符，公钥托管在指定URL

### 8:00-12:00 JWT令牌详解
- 获取JWT：使用aws sts get-web-identity-token命令
- JWT结构：包含头部(绿色)、载荷和签名三部分
- 默认过期时间：5分钟，可扩展至1小时
- 支持的签名算法：RS256等多种选项
- JWT内容解析：包含标准声明(主体、发行者、过期时间)和AWS特定声明
- AWS命名空间声明：包含EC2实例属性、组织信息、角色标签等

### 12:00-15:00 Azure集成与验证机制
- Azure令牌交换：将JWT提交到Azure令牌交换端点
- 交换参数：grant_type为client_credentials，assertion_type为JWT bearer
- Azure设置：仅需配置主体、发行者URL和受众即可建立联邦凭证
- 验证流程：Azure通过well-known OpenID配置端点和JWKS端点获取公钥验证令牌
- 支持的算法：RSA和ECDSA算法类型

### 15:00-18:00 功能优势与最佳实践
- 三大核心优势：
  - 增强安全性：消除长期凭证(客户事件响应团队2/3的案例源于长期凭证泄露)
  - 降低运维复杂度：无需管理和轮换长期凭证
  - 提升互操作性：支持多种云服务和SaaS提供商
- 权限控制：新增sts:GetWebIdentityToken权限和三个条件键
- 最佳实践：尽可能缩短令牌生命周期、验证签名后检查授权上下文、避免记录令牌、使用TLS传输
- 可用性：所有AWS商业区域、GovCloud和中国区域均已支持，无额外费用