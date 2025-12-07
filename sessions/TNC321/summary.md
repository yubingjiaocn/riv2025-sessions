# AWS re:Invent 2025 会议总结：SageMaker Unified Studio 安全配置

## 一、会议概述

本次技术分享会由AWS技术讲师Carl主讲，主要演示了如何安全地配置和使用Amazon SageMaker Unified Studio。Carl拥有五年半的AWS技术讲师经验，在本次会议中，他采用了大量实际操作演示的方式，向观众展示了如何为数据科学家和机器学习工程师建立一个安全、集中管理的工作环境。

会议的核心内容围绕三个主要部分展开：为什么需要关注机器学习工作负载的安全性（Why）、可以采取哪些保护措施和工具（What）、以及如何具体实施配置（How）。Carl特别强调，AI和机器学习在当今世界构成了威胁行为者的新型攻击目标，因此必须采取适当的安全措施。演讲中涵盖了从AWS Identity Center的身份管理、VPC网络隔离、KMS数据加密，到CloudTrail日志审计等多个安全层面的最佳实践。

特别值得注意的是，本次会议重点介绍了一项新功能——可信身份传播（Trusted Identity Propagation），这项功能能够在CloudTrail日志中直接显示实际操作用户的身份，而不仅仅是角色信息，大大简化了安全审计工作。整个演示过程中，Carl始终坚持使用多因素认证（MFA），以身作则地展示了安全最佳实践。

## 二、详细时间线与关键要点

### **开场与会议结构介绍 (00:00 - 02:30)**
- 讲师Carl自我介绍，拥有五年半AWS技术讲师经验
- 说明会议将分为三个部分：为什么（Why）、是什么（What）、如何做（How）
- 主要内容：演示SageMaker Unified Studio作为Identity Center应用程序的配置过程
- 重点关注安全相关配置项

### **威胁态势分析 (02:30 - 04:00)**
- 讨论AI和机器学习构成的新型威胁目标
- 强调威胁行为者可能将AWS账户变成"ATM机"来挖掘加密货币
- 指出攻击者不仅针对GPU，还会利用CPU和内存资源进行某些加密货币挖矿

### **安全工具与最佳实践 (04:00 - 08:30)**
- **身份与访问管理（IAM）**：强调必须深入理解AWS角色（Role）概念，这是身份认证的核心
- **基础设施与网络安全**：
  - 不建议在有互联网网关的VPC中运行机器学习工作负载
  - 推荐使用VPC端点与AWS服务通信
  - 使用Transit Gateway连接到默认网络以访问互联网
- **数据保护**：
  - 强烈推荐使用KMS（Key Management Service）
  - 引用CTO Werner Vogels的名言："加密一切"（Encrypt Everything）
  - KMS使数据加密变得简单，无需像传统数据中心那样配置硬件安全模块
- **模型安全**：做好以上三点是保护模型的基础
- **日志、监控与审计**：
  - CloudTrail服务记录所有API调用
  - 建议配置自定义Trail，而不仅依赖默认设置
  - 默认设置仅查看最近90天的管理事件

### **SageMaker产品线介绍 (08:30 - 10:00)**
- 承认SageMaker产品线众多，可能让用户困惑
- 重点介绍SageMaker Unified Studio：
  - 为数据科学家和机器学习工程师提供一站式工作环境
  - 用户无需学习AWS管理控制台
  - 单一界面（Single Pane of Glass）集成所有功能

### **Identity Center深入讲解 (10:00 - 14:00)**
- **历史演进**：
  - 2006-2011年：仅有根用户
  - 2011年：IAM服务推出，单账户可支持5000个用户
  - 现代最佳实践：使用多个AWS账户（可能有10、20、50、500甚至2000个账户）
- **Identity Center的作用**：
  - 作为集中式服务管理所有账户、身份和角色
  - 避免在多个账户中为同一用户创建多个IAM用户
  - 提供单一身份源（Single Source of Truth）
- **身份源选择**：
  - Identity Center Directory（内置目录）
  - Active Directory（企业常用）
  - 外部身份提供商（如Okta、Microsoft Entra ID，支持SAML 2.0）

### **实际演示：管理账户配置 (14:00 - 20:00)**
- 演示登录管理账户，强调使用MFA的重要性
- 展示组织结构：管理账户 + SageMaker成员账户
- **Identity Center配置**：
  - 展示用户组：Administrators、Data Scientists
  - 展示用户：Machine Learning Admin、Machine Learning User
  - **权限集（Permission Sets）**：
    - 定义用户组在特定账户中的权限
    - 由AWS托管策略或自定义策略组成
    - 创建后会在目标账户中自动生成角色（AWS-Reserved-SSO-*）
  - **多账户分配**：演示如何将权限集分配给多个账户和用户组

### **SageMaker Unified Studio域配置 (20:00 - 28:00)**
- 以SageMaker管理员身份登录SageMaker账户
- 访问DataZone服务（SageMaker Unified Studio基于DataZone构建）
- **创建域（Domain）**：
  - 域是连接用户、项目和共享资产的组织容器
  - 提供统一的管理和安全边界
- **VPC配置**：
  - 可使用内置CloudFormation模板创建VPC
  - 演示中选择预先创建的Machine Learning VPC和私有子网
- **角色配置**：
  - Domain Execution Role：代表用户执行操作
  - Domain Service Role：后台管理任务
- **加密设置**：可自定义加密配置

### **KMS最佳实践 (28:00 - 31:00)**
- **强烈建议使用客户托管密钥（Customer Managed Keys）而非AWS托管密钥**
- **原因一：角色分离**
  - 可分别定义谁能管理密钥、谁能使用密钥（加密/解密）
  - 防止账户管理员自动拥有解密所有数据的权限
- **原因二：CloudTrail日志**
  - 客户托管密钥的使用会记录在CloudTrail中
  - 可追踪谁在何时从哪个IP地址进行了解密操作
  - AWS托管密钥无法实现此功能
- **成本**：每个密钥每月1美元，每10,000次请求几美分

### **域配置完成与用户添加 (31:00 - 34:00)**
- 域创建完成（约1分钟）
- 添加单点登录用户到域
- 用户添加后，会在Identity Center门户的应用程序列表中看到该域

### **蓝图与项目配置 (34:00 - 37:00)**
- **蓝图（Blueprints）**：
  - 本质是CloudFormation模板
  - 用于创建Jupyter Notebooks、SQL数据库、Athena查询等资源
  - 可使用AWS提供的模板或自定义模板
- **项目配置文件（Project Profiles）**：
  - 蓝图的集合
  - AWS提供三个开箱即用的配置文件
  - 决定用户可以创建哪些类型的项目
- **关键配置：启用可信身份传播（Trusted Identity Propagation）**
  - 默认设置为false（因为许多现有服务不支持）
  - 对于新部署，强烈建议设置为true
  - 这是本次演示的核心安全功能

### **可信身份传播原理讲解 (37:00 - 40:00)**
- **功能说明**：允许AWS服务在跨服务边界时安全传递用户的实际身份（来自Identity Center），而不仅仅依赖IAM角色
- **工作流程**：
  1. 数据科学家登录Identity Center门户
  2. 访问SageMaker Unified Studio应用程序
  3. 创建或访问项目
  4. 在Jupyter Notebook中运行代码，查询S3存储桶
  5. CloudTrail日志不仅显示角色访问，还显示"代表（on behalf of）"信息
  6. 包含Identity Center实例ID和实际用户ID
- **优势**：无需追踪复杂的角色假设链，直接看到实际操作用户

### **S3配置演示 (40:00 - 会议结束)**
- 展示预先创建的S3存储桶（reinvent-demo-bucket）
- 存储桶中包含示例数据文件（products-10000.csv）
- **S3的可信身份传播配置**：
  - 每个支持可信身份传播的服务配置方式略有不同
  - S3的配置路径：访问管理 → 安全 → 访问授权（Access Grants）
  - 需要进行特定配置才能启用此功能
- 演示在此处中断，但已说明配置方向

### **关键技术要点总结**
- 始终使用MFA，Identity Center默认启用
- 理解并正确使用AWS角色概念
- 使用客户托管KMS密钥实现角色分离和审计
- 配置CloudTrail进行全面日志记录
- 使用Identity Center实现集中身份管理
- 启用可信身份传播简化安全审计
- 为机器学习工作负载使用隔离的VPC和私有子网