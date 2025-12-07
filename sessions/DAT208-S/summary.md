# AWS re:Invent 2025 - Oracle Database at AWS 会议总结

## 会议概述

本次会议由Oracle OCI Multicloud产品经理Michael Baris主讲,AWS Oracle联盟团队的Pat Bangalore和Jeremy Sheer,以及客户Equifax的代表Abin Singh共同参与。会议重点介绍了Oracle Database at AWS服务的最新进展和核心能力。

该服务是Oracle和AWS之间的革命性合作,将运行在Oracle硬件上的Oracle数据库服务部署在AWS数据中心内,由Oracle云基础设施管理。自2024年re:Invent大会上宣布限量预览以来,该服务已于2025年7月正式上线,目前在两个区域(北弗吉尼亚和俄勒冈)提供服务,每个区域配备两个可用区。服务已支持Terraform、自治恢复服务、AWS KMS集成、渠道合作伙伴私有优惠等功能,并计划在未来一年内扩展到20多个区域。

这项服务解决了客户长期以来的痛点:既能获得Oracle Exadata和RAC的完整功能,又能享受AWS数据中心内的低延迟连接,同时提供与AWS服务的无缝集成体验。客户可以通过AWS Marketplace购买,使用AWS API和工具进行配置,并与IAM、CloudTrail、CloudWatch等AWS服务直接集成,最重要的是能够让运行在EC2、ECS、EKS、SageMaker等服务上的工作负载访问Oracle数据库。

## 详细时间线与关键要点

00:00:00 - 会议开场与背景介绍
- Michael Baris介绍自己和团队成员
- 回顾服务发展历程:从2024年限量预览到2025年7月正式上线
- 服务已从单个区域单个服务扩展到两个区域多个服务

00:03:30 - Oracle Database at AWS核心概念
- 合作模式:Oracle硬件运行在AWS数据中心,由OCI管理
- 通过AWS Marketplace购买,连接到Amazon VPC
- 提供Exadata硬件与AWS服务之间的低延迟连接

00:05:00 - 客户需求驱动的合作
- 客户需要Oracle Exadata和RAC的完整功能
- 需要低延迟连接以支持关键任务应用
- 需要无缝的AWS集成体验(Marketplace、API、IAM等)
- 需要将企业数据与AWS原生服务结合

00:07:00 - 客户旅程三大步骤
1. 通过AWS Marketplace订阅服务
2. 在AWS账户中配置Oracle数据库资源
3. 迁移数据并与AWS服务集成

00:08:00 - 订阅与购买流程
- 通过私有优惠(Private Offer)与Oracle账户团队合作
- 支持直接购买或通过渠道合作伙伴购买
- 费用计入AWS支出承诺
- 灵活的许可选项:License Included(按小时付费)或BYOL(自带许可)
- BYOL提供最优许可指标,相比基于vCPU的授权云环境减少一半许可需求

00:11:00 - Oracle Exadata平台介绍
- Exadata是Oracle过去12年打造的最佳Oracle数据库运行平台
- 数据智能软硬件,硬件理解数据库结构
- 提供业界领先的性能、可用性和可扩展性
- 可在本地、OCI或多云环境中运行相同硬件

00:13:00 - Exadata Database Service详解
- 专用基础设施服务,起始配置:2个计算节点、3个存储节点
- 约400个CPU核心、240TB存储
- 可按需添加计算或存储节点(每次80TB)
- Oracle管理基础设施、虚拟化层和网络配置
- 客户在VM集群级别订阅,可灵活划分资源

00:16:00 - Autonomous Database服务
- 在Exadata基础上构建的全托管数据库体验
- 可与Exadata VM集群共享同一专用基础设施
- 自动处理性能调优、配置和数据库操作
- 支持OLTP和数据仓库工作负载
- 自动调整SGA、PGA等参数以适应工作负载变化

00:18:00 - Zero Data Loss Autonomous Recovery Service
- 基于本地零数据丢失恢复设备的云服务
- 提供最佳备份保护和最低备份影响
- 首次完整备份后,后续全部增量备份
- 时间点恢复时自动合成所需的块状态

00:20:00 - AWS集成能力
- 通过AWS管理控制台、API、CLI、Terraform配置
- 与IAM、CloudTrail、CloudWatch集成
- 支持AWS KMS进行透明数据加密
- 可备份到Amazon S3

00:22:00 - 网络架构说明
- Oracle数据库服务部署在AWS可用区内
- 通过高可用冗余链路连接到OCI区域控制平面
- 引入ODB Network新构造,类似VPC但仅包含Oracle和AWS资源
- 通过VPC对等连接访问服务

00:25:00 - 高可用性架构(MAA Gold认证)
- 支持跨区域复制配置
- 使用Data Guard进行数据复制
- 支持快速启动故障转移(Fast Start Failover)
- 第二个Exadata可以pilot light模式运行以控制成本
- 支持在线CPU扩展和单节点RAC配置

00:28:00 - 数据迁移方案
- 支持现有的数据迁移方法(Data Pump、Export等)
- Oracle Zero Downtime Migration工具
- 支持物理迁移(RMAN、Data Guard)和逻辑迁移(Data Pump、GoldenGate)
- GoldenGate可免费使用6个月用于迁移到OCI服务

00:32:00 - 托管服务的价值
- DBA可专注于数据管理和AI集成,而非基础设施维护
- 减少故障排除、补丁和配置工作
- 数据是AI时代最重要的资产

00:34:00 - Oracle Database 26 AI新特性
- 新增Vector数据类型用于AI应用
- 可将复杂数据属性向量化并存储在数据库中
- 支持使用SQL进行向量距离查询
- 可集成Amazon Bedrock的Titan模型生成嵌入
- 无需单独的向量存储,降低安全和治理开销

00:38:00 - Jeremy Sheer介绍AWS视角
- 服务已在北弗吉尼亚和俄勒冈上线
- 计划在全球推出20个额外区域
- 每个区域部署多个可用区

00:40:00 - AWS高可用性架构
- AWS区域定义为包含多个可用区
- 可用区地理位置分离但延迟低
- 使用Data Guard在可用区间同步复制
- 支持最大保护模式或最大可用性模式
- 在第三个可用区部署Data Guard Observer

00:43:00 - 应用层高可用性
- 应用层跨多个可用区部署
- 使用AWS Application Load Balancer分发流量
- 实现完整的应用和数据库高可用性模式

00:45:00 - 成本控制策略
- 第二个Exadata可以pilot light配置运行
- 仅在故障转移或灾难恢复时启用所需CPU
- 支持在线扩展CPU
- 可部署单节点RAC配置

00:47:00 - AWS服务集成
- 与200多个AWS服务集成
- S3备份、Terraform、CloudFormation支持
- AWS Resource Access Manager共享资源
- CloudWatch可观测性
- KMS密钥管理

00:49:00 - AWS Resource Access Manager应用
- 跨多个AWS账户共享Exadata基础设施
- 不同业务单元可在同一硬件上运行独立实例
- 支持生产和非生产环境分离
- 常见模式:在辅助可用区部署非生产环境

00:52:00 - AWS KMS集成
- 直接在KMS中管理Oracle TDE密钥
- 统一管理应用加密密钥和数据库密钥
- 大规模安全管理解决方案

00:54:00 - CloudWatch可观测性
- 在CloudWatch仪表板中查看Exadata指标
- 监控CPU、磁盘IO和性能特征
- 与应用层指标并列显示
- 缩短平均恢复时间(MTTR)

00:56:00 - Pat Bangalore介绍合作关系
- 90%的财富100强公司使用AWS
- 87%的客户运行Exadata
- 合作源于明确的客户需求
- 客户希望应用和数据库更接近

00:58:00 - 协作支持模型
- 技术问题:联系Oracle支持或通过AWS TAM联系Oracle值班经理
- 需要OCI租户和客户支持标识符(CSI)
- 账单问题:联系AWS支持(CSM或TAM)
- 服务通过AWS Marketplace交易,账单在AWS侧

01:01:00 - 入职流程支持
- 通过私有优惠入职
- 初期可能未分配CSI号码
- 可使用免费电话联系Oracle获取CSI
- 或通过值班经理协助解决

01:03:00 - 商业价值与资金机制
- 迁移加速计划(MAP)支持从本地迁移到AWS
- 提供评估、动员、迁移和现代化资金
- 包含工具、技术和资源支持

01:05:00 - 私有定价协议(PPA)优势
- ODB at AWS消费100%计入PPA承诺
- 取消了Marketplace通常的25%上限
- 可通过ODB消费完全履行PPA承诺

01:07:00 - 渠道合作伙伴私有优惠(CPPO)
- 2024年10月推出
- 面向系统集成商、ISV和分销商
- 合作伙伴拥有和控制账单
- 可提供迁移、托管服务和统一账单
- 合作伙伴的PPA也可100%通过CPPO履行承诺

01:09:00 - 会议总结
- 强调服务的技术创新和商业价值
- 突出AWS和Oracle的深度合作
- 为客户提供完整的云数据库解决方案