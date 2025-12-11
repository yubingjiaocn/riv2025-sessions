# AWS re:Invent 2025 Oracle Database at AWS 技术会议总结

## 会议概述

本次技术会议由AWS OCI MulticCloud产品经理Michael Barris主持，联合AWS Oracle联盟团队的Pat Bangalore和Jeremy Shearer，以及客户Equifax的Avinash Singh，深入探讨了Oracle Database at AWS服务。该服务是Oracle与AWS合作推出的革命性解决方案，将Oracle数据库服务运行在Oracle硬件上，由Oracle云基础设施管理，部署在AWS数据中心内。

会议重点介绍了该服务自2024年AWS re:Invent有限预览发布以来的发展历程，包括今年7月正式上线的两个主要服务产品，覆盖2个区域各2个可用区。服务已支持Terraform、自主恢复服务、AWS密钥管理服务集成等功能，并宣布将在未来一年内扩展到20个新区域。

## 详细时间线与关键要点

### 0:00-5:00 开场介绍与服务概述
- Michael Barris介绍演讲嘉宾和会议主题
- 回顾Oracle Database at AWS服务发展历程：从2024年有限预览到2025年7月正式发布
- 服务核心概念：Oracle硬件运行在AWS数据中心，由OCI管理，通过AWS Marketplace购买

### 5:00-10:00 客户需求驱动的解决方案
- 联合客户提出的三大需求：
  - 完整的Oracle Exadata和RAC功能特性
  - 低延迟连接以支持关键任务应用
  - 与AWS服务的无缝集成体验
- 客户迁移三步骤：AWS Marketplace订阅、资源配置、数据迁移与统一

### 10:00-15:00 服务架构与核心组件
- Oracle Exadata硬件平台介绍：12年优化的数据库专用硬件
- Exadata Database Service：专用基础设施，起始配置2个计算节点、3个存储节点
- Autonomous Database Service：完全托管的数据库体验
- Zero Data Loss Autonomous Recovery Service：企业级备份恢复解决方案

### 15:00-20:00 AWS集成与网络架构
- 深度集成AWS服务：IAM、CloudTrail、CloudWatch、KMS、S3备份
- ODB网络构建：类似VPC但专用于Oracle数据库资源
- 最大可用性架构(MAA)：跨AZ复制和故障转移配置

### 20:00-25:00 数据迁移策略
- 三种迁移方式：现有数据迁移工具、Oracle零停机迁移、Golden Gate逻辑复制
- 物理迁移vs逻辑迁移选择标准
- 支持在线和离线迁移模式

### 25:00-30:00 Oracle Database 26AI新特性
- 向量数据类型支持AI工作负载
- 数据库内嵌入LLM模型能力
- 房地产搜索用例演示：向量距离查询实现智能匹配

### 30:00-35:00 AWS合作伙伴视角
- Jeremy Shearer和Pat Bangalore介绍AWS-Oracle联盟
- 多可用区高可用架构部署模式
- 成本优化策略：试点配置、单节点部署选项

### 35:00-40:00 企业级功能与支持
- AWS Resource Access Manager跨账户资源共享
- KMS透明数据加密密钥管理
- CloudWatch监控集成
- 协作支持模式：技术问题联系Oracle，账单问题联系AWS

### 40:00-45:00 Equifax客户案例分享
- Avinash Singh介绍Equifax全球金融服务平台
- Oracle BRM计费系统迁移需求：突破RDS 64TB存储限制
- ADB at AWS选择原因：性能提升、存储扩展、AI就绪能力
- 迁移时间表：非生产环境已完成，生产环境计划4-5月上线