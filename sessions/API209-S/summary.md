# Streaming Without Limits: Sky如何利用Redis Cloud重塑流媒体平台

## 会议概述

本次AWS re:Invent 2025技术分享会由Redis首席产品官Jon Fritz和NBCUniversal Sky全球流媒体工程经理Lena Youssef共同主讲，主题为"Streaming Without Limits: How Sky scale's bookmarking and powers the future of streaming with Redis Cloud"。会议重点介绍了Redis Cloud的最新创新功能，以及Sky如何利用Redis Cloud重新架构其流媒体平台，特别是书签功能的实现。

Jon Fritz首先介绍了Redis的市场地位和最新技术发展，包括Redis 8.4版本的性能提升、Redis Cloud的两种部署模式，以及在生成式AI领域的应用。随后，Lena Youssef详细分享了Sky从Cassandra迁移到Redis Cloud的实践经验，展示了如何通过Redis Cloud解决大规模流媒体服务中的技术挑战，并介绍了他们在生成式AI平台Genepi中的应用探索。

## 详细时间线与关键要点

### 0:00-10:00 Redis技术概览与产品创新
- **Redis市场地位**: 全球最受欢迎的内存数据库，Docker拉取量超过100亿次
- **Redis 8.4发布**: 延迟改善高达90%，性能和可扩展性显著提升
- **Redis Cloud两种版本**:
  - Redis Cloud Essentials: 完全无服务器平台，成本最低
  - Redis Cloud Pro: 高可用性、高性能版本，支持五个九的可用性
- **AWS部署模式**: 托管计算模式和自带云模式(BYOC)

### 10:00-15:00 Redis Cloud新功能发布
- **Redis Flex**: 支持RAM和SSD混合存储，最高可节省75%成本，扩展至50TB
- **性能优化**: 基于AWS Graviton实例，扩展速度提升40%
- **Smart Client Handoffs**: 消除计划事件期间的应用中断
- **Redis Data Integration (RDI)**: 实时数据同步和转换功能

### 15:00-20:00 Redis在生成式AI中的应用
- **AI生态系统集成**: 与30多个顶级AI框架集成
- **客户案例**: OpenAI、RelevanceAI等公司的应用实践
- **Redis Lane Cache**: 语义缓存产品，性能提升15倍，成本降低90%
- **Asurion案例**: 客户服务应用响应时间改善50%，网站参与度提升4倍

### 20:00-25:00 Sky书签功能技术挑战
- **业务规模**: Peacock拥有4100万美国用户，2024年NFL外卡赛创造流媒体记录
- **技术挑战**: 每分钟数百万次写入，每次页面加载数百万次读取
- **原有架构问题**: 
  - Cassandra成本高昂且难以管理
  - 无法满足书签保留期扩展需求
  - 缺乏缓存层，所有操作直接访问数据库

### 25:00-30:00 Redis Cloud解决方案架构
- **架构重设计**: 
  - 双Redis集群设计：String集群处理高频写入，Sorted Set集群处理数据排序
  - 热数据和冷数据分离策略
  - 书签在Redis中保留至少10分钟后转入长期存储
- **数据结构选择**:
  - String数据结构：支持重写入，O(1)时间复杂度
  - Sorted Set：提供有序视图，类似排行榜功能

### 30:00-35:00 实施过程与成果
- **实施阶段**:
  - 概念验证：功能测试、负载测试、延迟基准测试
  - 写入减少20-40倍的累积率测试
  - AWS PrivateLink支持实现生产就绪
- **显著成果**:
  - 写入压力减少20倍
  - 数据库迁移至AWS Keyspaces成功解锁
  - 零生产事故记录
  - 为NFL独家赛事做好扩展准备

### 35:00-40:00 未来应用与Genepi AI平台
- **并发管理服务(ConMan)**: 控制用户同时流媒体数量，计划集成Redis Cloud
- **Genepi AI平台架构**:
  - 多用途GenAI平台，支持开发和生产工作负载
  - 供应商和云提供商无关的解决方案
  - 集成Redis Lane Cache作为语义缓存服务
  - 结合AWS Kendra、Knowledge Base、OpenSearch等服务
- **向量数据库选择**: Redis(3-10毫秒)vs OpenSearch(10-100毫秒)，根据租户需求选择

### 40:00-41:30 合作伙伴关系与总结
- **Redis社区支持**: 从开源社区开始，获得架构指导和技术支持
- **AWS合作**: 通过AWS Marketplace简化采购流程，PrivateLink支持增强安全性
- **未来展望**: 继续探索个性化推荐、特征存储等更多Redis应用场景