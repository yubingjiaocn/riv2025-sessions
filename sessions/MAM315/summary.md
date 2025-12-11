# AWS re:Invent 2025：企业软件许可与优化会议总结

## 会议概述

本次会议由AWS的Microsoft许可专家Christine Megit主持，与同事GianPaolo和Valerie共同探讨了在AWS上进行企业软件许可和优化的策略，重点关注Microsoft许可。会议介绍了AWS的优化与许可评估(OLA)项目、自带许可(BYOL)与许可包含模式的对比，以及新推出的许可包含优化CPU功能。演讲者强调Microsoft许可的复杂性，并提供了实用的成本优化解决方案和最佳实践。

会议面向已在AWS上运行工作负载的客户、正在考虑云迁移的企业以及合作伙伴。通过数据驱动的方法和机器学习工具，帮助客户实现平均20%的EC2计算成本节省，同时简化许可管理流程。

## 详细时间线与关键要点

### 0:00-5:00 会议开场与介绍
- Christine Megit介绍团队成员和会议议程
- 强调Microsoft许可复杂性，客户经常遇到的挑战
- 概述会议将涵盖的主要主题：OLA项目、BYOL、许可包含选项和新功能

### 5:00-15:00 优化与许可评估(OLA)项目介绍
- Valerie Rosenfield详细介绍OLA项目的核心价值
- OLA是AWS提供的免费数据驱动评估服务
- 解决三个关键问题：环境清单、业务案例评估、迁移规划
- 客户通过OLA实现36%的成本降低，迁移速度提升34%

### 15:00-25:00 Microsoft许可分析与工具
- 介绍支持的发现工具：AWS Migration Evaluator、Cloudamize、modelizeIT
- 展示实际客户案例：医疗保健客户节省500万美元
- 详细分析Windows和SQL Server足迹优化策略
- 强调在Microsoft EA续约前6-12个月进行评估的重要性

### 25:00-35:00 自带许可(BYOL)详解
- Christine详细解释License Mobility权益要求
- SQL Server BYOL的核心模型和服务器CAL模型
- 2019年10月1日后对非License Mobility产品的限制
- Windows Server BYOL需要专用主机和特定版本要求

### 35:00-45:00 许可包含选项与新功能
- Windows Server和SQL Server许可包含的优势
- 新推出的Amazon EC2 SQL Server高可用性功能
- 许可包含优化CPU功能的详细介绍
- AWS License Manager工具的使用建议

### 45:00-52:00 优化CPU功能演示
- GianPaolo现场演示如何使用优化CPU功能
- 展示禁用超线程和调整vCPU数量的过程
- 介绍AWS Compute Optimizer的机器学习驱动分析
- 强调测试和监控的重要性，推荐7000-8000 IOPS/CPU比率

### 52:00-57:00 实施指南与总结
- Valerie介绍如何开始使用这些优化功能
- 展示初步客户节省数据：平均20%的EC2成本节省
- 介绍AWS Transform工具的未来发展方向
- 提供多个QR码链接到相关资源和文档