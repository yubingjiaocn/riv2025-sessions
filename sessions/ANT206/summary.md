# AWS re:Invent 2025: Amazon Redshift 和 Amazon Athena 新功能

## 会议概述

本次会议由 Amazon Redshift 产品管理高级经理 Imran Moin、Amazon Athena 首席产品经理 Scott Rigney 以及 Twilio 首席软件工程师 Sean McKibben 共同主讲。会议重点介绍了 Amazon Redshift 和 Amazon Athena 在 2025 年的重要功能更新和创新。

会议涵盖了云数据仓库的三大核心用例：结构化数据的云数据仓库、非结构化数据的云数据湖，以及将两者结合的湖仓一体化架构。Amazon Redshift 作为专用的云数据仓库提供高性能 SQL 分析，Amazon Athena 作为无服务器查询服务处理 S3 中的非结构化数据，而 Amazon SageMaker 则将两者统一，为高级分析和机器学习提供统一的数据基础。

Twilio 作为客户案例分享了如何使用 Redshift 和 Athena 重新构建其计费引擎，实现了 75% 的成本节约，同时处理每天数十亿的使用事件，展示了分布式数据仓库架构在大规模企业应用中的实际价值。

## 详细时间线与关键要点

### 00:00-10:00 会议开场与 Amazon Redshift 概述
- **00:00-02:00**: 会议介绍，三位演讲者自我介绍
- **02:00-05:00**: 客户分析需求的三大用例分析
  - 结构化数据的云数据仓库用例
  - 非结构化/半结构化数据的云数据湖用例  
  - 湖仓一体化架构用例
- **05:00-10:00**: Amazon Redshift 发展历程回顾
  - 2013年首次发布，首个云数据仓库
  - 2017年 Redshift Spectrum 发布
  - 2022年 Zero-ETL 支持
  - AI 驱动的自动扩展和优化功能

### 10:00-20:00 Redshift 2025年三大投资重点
- **10:00-15:00**: 云数据仓库基础功能
  - 性能优化：比最接近竞争对手快 2.2 倍的性价比
  - 物化视图增强功能（6月、7月、9月发布）
  - 多维数据布局（MDDL）功能，提供高达 10 倍的性价比提升
- **15:00-20:00**: 安全性增强
  - 1月发布的安全默认设置
  - 集群默认私有化、完全加密、强制 SSL 连接

### 20:00-30:00 分布式数据仓库架构
- **20:00-25:00**: 分布式数据仓库愿景
  - Hub and Spoke 架构
  - Data Mesh 架构
  - 工作负载隔离和成本可见性
- **25:00-30:00**: Redshift Serverless 增强功能
  - 3月：Trailing Track 支持
  - 5月：FedRAMP 授权
  - 6月：4 RPU 支持，每小时仅需 1.50 美元
  - 7月：受限网络环境支持

### 30:00-35:00 Serverless 预留实例和治理功能
- **30:00-32:00**: 4月发布的 Serverless 预留实例
  - 最高 24% 的折扣
  - 支持全额预付和部分预付
- **32:00-35:00**: 集中身份和统一治理
  - 与 AWS Lake Formation 和 AWS Glue Data Catalog 集成
  - 支持 IAM Identity Center 凭证登录

### 35:00-40:00 并发扩展和 Apache Iceberg 支持
- **35:00-37:00**: 并发扩展功能增强
  - 支持更多工作负载类型
  - 10月：DML 和 DDL 命令支持
- **37:00-40:00**: Apache Iceberg 支持
  - Iceberg 表读写功能
  - 数据湖查询性能提升 2 倍
  - 基于 Iceberg 数据的物化视图自动刷新

### 40:00-50:00 Twilio 客户案例分享
- **40:00-42:00**: Twilio 计费引擎重构背景
  - 处理数十亿使用事件
  - 传统架构的灵活性和分析能力限制
- **42:00-45:00**: 解决方案架构选择
  - 选择 Redshift 作为操作数据仓库
  - 串行化事务隔离保证
  - Redshift Serverless 实现 75% 成本节约
- **45:00-50:00**: 分布式数据仓库实施
  - 多个工作组共享数据
  - dbt 管道管理 2 亿个价格点
  - Zero-ETL 历史模式集成

### 50:00-54:48 Amazon Athena 新功能介绍
- **50:00-52:00**: Athena 服务概述和 Iceberg 性能提升
  - Iceberg 查询性能提升 1.5 倍
  - Parquet 列索引功能
  - 物化视图支持
- **52:00-54:48**: S3 Tables 和其他增强功能
  - S3 Tables GA 发布
  - Create Table as Select (CTAS) 功能
  - 容量预留和自动扩展解决方案
  - SageMaker 笔记本集成和可信身份传播支持