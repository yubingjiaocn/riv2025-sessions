# AWS re:Invent 2025 多云数据库服务技术分享会总结

## 会议概述

本次技术分享会由AWS多云产品副总裁Kambiz Aghili主持，并邀请了Equifax公司的Avinash分享客户实践经验。会议主要围绕Oracle数据库在AWS上的多云解决方案展开，重点介绍了Oracle Database at AWS服务的技术特性和实际应用案例。

会议涵盖了多云架构的核心概念、Oracle Exadata技术在AWS数据中心的原生部署、以及与AWS服务的深度集成能力。Equifax作为重要的数据服务公司，分享了他们从RDS Oracle迁移到Autonomous Database at AWS的实践经验，特别是在处理大规模OLTP工作负载和账单系统方面的应用。

## 详细时间线与关键要点

### 0:00-2:00 会议开场与议程介绍
- Kambiz Aghili介绍会议安排：7-8分钟技术概述，客户分享，4-5分钟问答环节
- 确认Oracle Database at AWS多云服务的战略定位

### 2:00-5:00 多云架构核心概念
- Oracle数据库技术40年发展历程，在各行业的广泛应用
- 首次在AWS数据中心原生部署完整的Oracle Exadata技术栈
- Oracle在AWS、Azure、GCP等多云环境中的原生运行能力

### 5:00-8:00 三大创新领域详解
- **管理运维简化**：支持基础设施即代码、API、CLI、SDK、CloudFormation和Terraform
- **自动化数据保护**：提供近实时的自主恢复服务
- **安全集成增强**：与AWS KMS集成，支持OCI Vault和Oracle Key Vault

### 8:00-10:00 技术架构优势
- Exadata硬件在AWS数据中心的原生部署
- 跨多个可用区实现零RTO/RPO
- 微秒级延迟的低延迟网络配置
- 与AWS Bedrock等AI服务的原生集成

### 10:00-12:00 Equifax客户案例分享
- Equifax作为数据公司的业务背景和服务范围
- 内部数据织物层云架构设计
- 从RDS Oracle迁移到ADB的业务驱动因素
- 64TB数据规模的高性能OLTP系统需求

### 12:00-14:00 实施效果与未来规划
- **性能优化**：Exadata提供的高吞吐量和优化性能
- **存储扩展**：PB级存储容量解决数据增长问题
- **AI就绪**：支持Oracle 23ai和26ai，为数据AI化做准备
- **运维简化**：减少维护活动，实现与AWS服务的无缝集成

### 14:00-14:48 服务可用性与问答环节
- 当前在美国东西部地区GA可用
- 月底将新增3个区域，未来9-10个月内将覆盖20多个区域
- 开放现场问答环节