# AWS re:Invent 2025 - AWS与SAP数据集成会议总结

## 会议概述

本次会议由AWS首席解决方案架构师Satish和SAP业务数据云CTO Bion Friedman共同主讲，重点介绍了AWS与SAP长达17年合作伙伴关系所带来的企业级数据集成解决方案。会议核心内容围绕如何利用AWS和SAP的技术特性，快速从SAP和非SAP数据源中获取洞察，构建统一的数据湖仓架构。

演讲者详细介绍了AWS在SAP工作负载方面的优势，包括支持最广泛的SAP数据平台（SAP HANA、Data Sphere、BW等）以及200多项AWS原生服务。会议特别强调了两项关键技术：AWS Glue的Zero ETL功能和SAP Business Data Cloud。Zero ETL作为完全托管的服务，能够实现从多种数据源到统一湖仓的近实时数据复制，无需编写代码。SAP Business Data Cloud则通过数据产品（Data Products）的概念，将SAP数据的语义和元数据一并管理，使得SAP数据能够更容易地与非SAP数据集成，并支持AI和分析应用场景。

会议通过实际演示展示了Zero ETL的配置过程，从选择SAP OData连接、指定数据对象（如采购订单）、设置目标存储（S3）到配置刷新间隔，整个过程简单直观。演讲者还介绍了SAP Business Data Cloud的湖仓架构，采用青铜-白银-黄金三层架构（Medallion Architecture），支持从原始数据到主数据产品再到派生数据产品的转换流程，并通过Delta Share等开放协议实现零拷贝的数据共享。

## 详细时间线

### 开场与背景介绍
[00:00 - 02:30] 
- 会议开场，介绍AWS与SAP的17年合作伙伴关系
- Satish自我介绍，担任AWS首席解决方案架构师
- 会议主题：利用AWS和SAP特性加速数据洞察，无论数据位于SAP还是非SAP系统

### AWS在SAP工作负载方面的优势
[02:30 - 05:45]
- AWS提供最广泛的SAP数据平台支持（SAP HANA、Data Sphere、BW等）
- 提供200多项AWS原生服务用于安全治理、数据策略、数据管道和生成式AI工作负载
- 展示客户案例：Moderna（疫苗供应链优化）、Toyota、Volkswagen、Adidas等企业在AWS上运行关键SAP工作负载

### SAP数据平台选择
[05:45 - 07:30]
- SAP Business Data Cloud于2025年2月首次在AWS上发布
- AWS原生数据栈：AWS Glue（数据处理）、EMR、Redshift（数据仓库）、QuickSight（可视化）、SageMaker（AI/ML）
- 第三方ISV选项：Qlik、Collibra、Snowflake、Databricks

### 统一湖仓架构的重要性
[07:30 - 09:15]
- 强调不要让数据分散在各处，应将数据整合到统一湖仓中
- 客户面临的挑战：数据整合复杂，涉及不同技术、技能和人员
- AWS Glue提供原生连接器，简化ETL管道构建

### Zero ETL功能介绍
[09:15 - 11:00]
- Zero ETL是完全托管的服务，帮助从多种数据源复制数据到统一湖仓
- 工作原理：首次设置时创建源数据快照并同步到目标（S3、S3 Tables或Redshift）
- 之后进行持续增量复制，通常在10秒内完成（近实时）
- 支持选择特定数据对象进行复制，可自定义刷新间隔

### Zero ETL实际演示
[11:00 - 14:30]
- 在AWS Glue管理控制台中创建Zero ETL集成
- 通过SAP OData连接选择数据源
- 演示选择采购订单（Purchase Orders）数据对象并预览数据
- 选择S3作为目标，配置在Glue数据库中
- 设置刷新间隔为15分钟（默认为1小时）
- 展示数据复制完成后在Amazon Athena中查询数据

### Zero ETL支持的数据源和目标
[14:30 - 15:30]
- 支持AWS原生数据库作为数据源
- 支持第三方应用（SAP、Salesforce）
- 2025 re:Invent新发布：支持自管理数据库（Oracle、MySQL、SQL Server、PostgreSQL），无论托管在EC2还是本地

### SAP Business Data Cloud介绍
[15:30 - 17:45]
- Bion Friedman（SAP Business Data Cloud CTO）接手演讲
- 介绍SAP数据与非SAP数据的集成挑战
- SAP数据的复杂性：语义特定且复杂，传统方式需要反复重建语义
- Business Data Cloud通过整体解决方案解决SAP数据集成问题

### Business Data Cloud架构
[17:45 - 20:30]
- 目标：简化SAP数据与非SAP数据的结合使用
- 支持AI和智能代理理解SAP数据语义并采取行动
- 底层：SAP应用（S/4HANA、Ariba、SuccessFactors等）
- 中间层：创建数据产品（Data Products），提供源数据的360度视图
- 顶层：知识图谱，供智能代理使用

### Business Data Cloud组件
[20:30 - 22:45]
- 湖仓层：在对象存储中管理数据产品
- Business Data Fabric：提供多种数据消费选项
  - Data Sphere（云数据仓库）
  - SAP Analytics Cloud
  - BW现代化迁移路径
  - SAP Databricks（内置AI/ML解决方案）
- 支持AWS等合作伙伴使用这些数据
- 应用层：智能应用（行业解决方案或基于BTP的应用）

### 数据产品详解
[22:45 - 25:00]
- 数据产品不仅是关系数据集，还包括完全托管的SaaS服务
- 包含源系统的语义和元数据
- 使用开源协议Open Resource Discovery（ORD）
- 提供多种API访问方式：Delta Share（零拷贝消费）、SQL访问

### 数据产品生态系统
[25:00 - 27:15]
- SAP托管数据产品：来自S/4HANA Cloud、SuccessFactors、Ariba、Concur等云原生LOB解决方案
- 客户自定义托管数据产品：来自本地ECC、S/4HANA本地版、BW或第三方数据
- 通过开源协议和Delta Share实现双向数据共享
- 支持合作伙伴创建数据产品并与SAP共享

### Business Data Cloud技术架构
[27:15 - 31:00]
- 核心：基于湖仓的对象存储管理数据产品
- 解耦摄取层和消费层
- 工作流程：
  1. 消费者或管理员通过BDC Cockpit触发数据产品安装
  2. 编排层管理整个数据集成链
  3. 调用源系统API（如S/4HANA）收集数据
  4. 数据推送到对象存储的青铜层（原始数据）
  5. 应用Medallion架构进行转换
  6. 白银层：主数据产品（源数据的稳定API表示）
  7. 黄金层：派生数据产品（组合多个数据源）
- 通过Spark管道执行转换
- 在统一客户环境（Unified Customer Landscape）目录服务中注册元数据

### 会议总结与行动呼吁
[31:00 - 32:00]
- 提供相关链接供进一步了解Business Data Cloud和Zero ETL集成
- 提醒观众通过正常渠道提供会议反馈
- 会议结束