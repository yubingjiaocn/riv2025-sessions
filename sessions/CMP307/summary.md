# AWS re:Invent 2025 - CMP 307: Graviton 最佳性价比解决方案

## 会议概述

本次会议由AWS核心计算产品总监Sudhi Rahman主持，与AWS副总裁兼杰出工程师Ali Saidi以及Atlassian首席工程师Thibaud Delor共同分享了AWS Graviton处理器的发展历程和最新进展。会议重点介绍了刚刚发布的Graviton 5芯片，展示了其在性能、能效和成本优化方面的显著提升。

会议涵盖了Graviton处理器的技术演进、客户成功案例、以及实际部署的最佳实践。特别值得关注的是Atlassian的实际迁移经验，展示了从失败尝试到成功部署的完整过程，为其他企业提供了宝贵的参考。

## 详细时间线与关键要点

### 0:00-5:00 - 开场介绍与Graviton概述
- 会议主题：CMP 307 - Graviton如何为AWS工作负载提供最佳性价比
- 演讲嘉宾介绍：Sudhi Rahman（AWS）、Ali Saidi（AWS）、Thibaud Delor（Atlassian）
- AWS定制芯片战略：超过十年的定制芯片开发经验
- Graviton核心价值：最佳性价比和可持续性优势

### 5:00-10:00 - Graviton发展历程与客户采用情况
- 2018年Graviton 1：建立ARM64软件生态系统
- 2019年Graviton 2：支持通用应用程序
- Graviton 3：每核心性能提升25%，优化视频编码和机器学习
- Graviton 4：核心数量增加50%，支持大规模扩展工作负载
- 客户采用数据：超过90,000个AWS客户使用Graviton
- 全球部署：38个AWS区域提供300多种Graviton实例类型

### 10:00-15:00 - 客户成功案例与性能表现
- ClickHouse：平均性能提升25-30%，某些场景下提升76%
- FreshWorks：Ruby on Rails和Java应用响应时间改善23%
- Cora：从Graviton 3迁移到4后查询服务时间改善20%
- 可持续性收益：Snowflake碳排放减少57%，Adobe和JFrog减少60%
- Amazon内部使用：Prime Day超过40%的计算由Graviton提供支持

### 15:00-25:00 - Graviton 5技术深度解析（Ali Saidi）
- 核心数量翻倍：从Graviton 4的基础上实现核心数量翻倍
- 性能提升：每核心性能提升25%，采用3纳米工艺
- 缓存优化：L3缓存增加5.3倍至192MB，总缓存容量约600MB
- 内存技术：支持DDR5-8800，内存访问延迟降低15%至100纳秒以下
- 连接性：首个支持PCIe Gen 6的CPU，提供约0.5TB/秒的I/O连接

### 25:00-30:00 - 安全性增强与Nitro隔离引擎
- Nitro系统演进：将网络、存储和管理功能转移到专用芯片
- 新技术：Nitro隔离引擎，位于Graviton CPU和Nitro虚拟机管理程序之间
- 开发特色：使用Rust语言编写，从开始就集成形式化验证
- 安全保障：数学证明软件规范与实现的匹配性，确保内存安全

### 30:00-35:00 - 性能基准测试与客户反馈
- EDA工具支持：Siemens Caliber在Graviton 5上性能提升30%
- 机器学习：PyTorch性能提升35%
- Web应用：Grails框架请求处理能力提升32%
- 数据库：MySQL新订单处理能力提升40%
- 客户验证：Snowflake性能提升30%+，Honeycomb延迟降低20-25%

### 35:00-42:00 - Atlassian实际部署经验（Thibaud Delor）
- 公司背景：支持30万客户，数万EC2实例，3000个服务
- 首次尝试失败：Graviton 3迁移遇到并发性能问题
- 成功策略：与AWS专家合作，采用主动基准测试而非微基准测试
- 关键发现：L3缓存命中率与性能强相关，启用透明大页面（THP）
- 部署结果：吞吐量提升30%，延迟降低12%，成本降低25%

### 42:00-44:00 - 最佳实践与资源推荐
- 迁移框架：托管服务最简单，解释型语言开箱即用，编译型语言需重新编译
- 技术资源：GitHub技术指南、T4G免费试用（750小时）
- 开发工具：Q Developer、AWS Transform、新发布的Transform Custom
- 性能分析：APERF工具用于应用程序性能分析
- 部署策略：金丝雀部署或蓝绿部署逐步迁移生产流量