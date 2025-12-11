# AWS re:Invent 2025 ECS 会议总结

## 会议概述

本次会议是一个300级别的技术分享，主要介绍了Amazon ECS（Elastic Container Service）的核心功能、容量配置策略、安全合规以及成本优化。会议由AWS ECS工程总监Mats Lanner和产品经理Alex主讲，并邀请了来自QRT（Qube Research and Technologies）的Ruben分享实际应用案例。

会议重点讨论了ECS的三种计算选项：传统EC2、Fargate和新推出的ECS Managed Instances。特别强调了ECS作为AWS原生容器编排服务的优势，包括无需管理控制平面、按需付费模式、提升开发敏捷性以及内置AWS安全最佳实践。QRT的案例展示了如何从小规模应用成长为运行数万个服务的大规模容器化工作负载。

## 详细时间线与关键要点

### 0:00-5:00 会议开场与ECS概述
- 介绍演讲嘉宾：Mats Lanner（ECS工程总监）、Alex（Fargate产品经理）、Ruben（QRT量化技术专家）
- ECS定义：专为AWS构建的容器编排器，核心原则是承担尽可能多的运维工作
- ECS四大支柱：大规模容器启动、按需付费、提升速度和敏捷性、体现AWS安全运维最佳实践

### 5:00-10:00 ECS规模与客户选择
- 客户每周在ECS上启动约30亿个任务
- 65%的新AWS容器客户选择ECS，其中大多数使用Fargate
- Prime Day期间每天启动1800万个Fargate任务
- 客户选择ECS的三大原因：简化运维、安全性、高效率

### 10:00-20:00 容量配置选项对比
- **Fargate**：完全托管数据平面，只需考虑CPU和内存，提供任务隔离，按运行时间付费
- **EC2**：完全控制实例类型和配置，支持所有EC2购买模式，但需要管理AMI和补丁
- **ECS Managed Instances**（新功能）：平衡托管体验和控制能力，实例在用户账户中但完全由AWS管理

### 20:00-25:00 ECS Managed Instances详细介绍
- 实例生命周期完全由AWS控制，约两周后自动替换
- 支持实例类型选择和GPU工作负载
- 改进的成本优化：更快的扩容和智能任务迁移
- 支持特权容器和eBPF代理
- 可使用EC2事件窗口控制维护时间

### 25:00-35:00 安全与合规
- 共享责任模型：AWS负责控制平面和基础设施，用户负责应用层
- **Fargate隔离**：每个任务运行在独立EC2实例上，实例不重用
- **Managed Instances**：多任务共享实例，通过bin packing优化利用率
- 安全最佳实践：减少攻击面、定期补丁、VPC网络模式
- 使用Bottlerocket作为容器操作系统，最小化包集合

### 35:00-45:00 成本优化策略
- **硬件选择**：支持Intel、AMD和Graviton处理器
- **购买选项**：按需、储蓄计划、Spot实例（最高80%折扣）
- **Fargate优化**：100%利用率、Seekable OCI快速启动、Compute Optimizer建议
- **Managed Instances优化**：主动任务压缩、容器镜像缓存、实例重用
- 短期任务（<2分钟）建议使用Managed Instances以降低成本

### 45:00-54:30 QRT客户案例分享
- **公司背景**：全球系统性资产管理公司，使用数据驱动的自动化投资策略
- **架构演进**：从本地部署到容器化Python工作负载，选择Fargate+ECS
- **选择原因**：小团队专注业务、serverless理念、从小规模开始、合规安全要求
- **系统架构**：QCU（计算单元）+ Head Node（逻辑服务器），使用gRPC通信，Cloud Map服务发现
- **规模增长**：实现100倍增长，目前运行数万个服务
- **多账户架构**：跨账户VPC、专用账户分离、基于CloudWatch的可观测性
- **未来计划**：测试Managed Instances支持GPU和大内存需求，考虑多区域部署