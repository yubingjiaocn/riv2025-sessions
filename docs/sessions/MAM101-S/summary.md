# AWS re:Invent 2025 - 使用 FSx for ONTAP 优化 Amazon Elastic VMware Service 存储成本

## 会议概述

本次技术会议由 NetApp 产品解决方案架构师 Richard Nichol 主讲，重点介绍如何利用 Amazon FSx for ONTAP 优化 Amazon Elastic VMware Service (EBS) 的存储成本。Richard 拥有 14 年 NetApp 工作经验，其中一半时间专注于云产品，从 FSx for ONTAP 概念阶段就开始参与该项目。

会议涵盖了 EBS 和 FSx for ONTAP 的核心功能特性，详细阐述了两项服务如何协同工作以降低总拥有成本、改善 SLA 性能，并实现与本地环境一致的运维体验。演讲还特别介绍了基于 FSx for ONTAP 的灾难恢复场景和免费的 Workload Factory 工具，为企业 VMware 工作负载迁移到云端提供全面的规划和实施指导。

## 详细时间线与关键要点

### 0:00-5:00 - 会议开场与议程介绍
- 演讲者自我介绍：Richard Nichol，NetApp 产品解决方案架构师
- 14 年 NetApp 工作经验，专注云产品和 FSx for ONTAP
- 会议议程概览：EBS 服务介绍、FSx for ONTAP 功能、成本优化策略、灾难恢复场景、Workload Factory 工具

### 5:00-10:00 - Amazon Elastic VMware Service (EBS) 基础介绍
- EBS 是将 VMware 环境迁移到云端最快最简单的方式
- 提供完整的 VCF 堆栈控制权，保持与本地环境一致的操作方式
- 支持客户自管理或合作伙伴管理两种模式
- 多种使用场景：数据中心关闭、环境扩展、开发测试、灾难恢复、现代化第一步

### 10:00-15:00 - EBS 技术架构与部署
- 自动化部署流程，通过控制台或 API 操作
- 需要提供 VPC、EC2 实例、VCF 订阅、网络 CIDR 配置
- 约 3 小时完成完整 VCF 堆栈部署
- 当前支持 i4i metal 实例，最小 4 节点部署
- 使用 VCF 5.2.1 版本，未来将支持更多实例类型和 VCF 9

### 15:00-20:00 - FSx for ONTAP 服务介绍
- 唯一获得 Amazon EBS 认证的 AWS 原生存储服务
- 完全托管的 AWS 存储服务，提供企业级功能
- 支持文件、块和对象存储的多协议访问
- 高可用性双节点架构，基于快照的数据保护
- 数据安全：静态加密、传输加密、Active Directory 集成、不可变存储

### 20:00-25:00 - FSx for ONTAP 高级功能
- 数据占用空间减少：重复数据删除、压缩、数据分层
- SnapMirror 跨区域复制功能
- FlexClone 即时数据副本技术
- 自主勒索软件保护功能
- 与 EBS 的两种集成方式：补充数据存储和客户端附加存储

### 25:00-30:00 - 成本优化策略
- 计算与存储解耦，避免不必要的 ESXi 主机成本
- 存储效率功能可节省高达 70% 的存储空间
- 灵活的性能扩展选项，支持非破坏性升级
- 随着环境增长，成本节省效果更加显著
- 同时减少 VCF 订阅的核心数量成本

### 30:00-35:00 - VM 备份性能改进与灾难恢复
- 对比传统 VSAN 备份与 FSx for ONTAP 备份方案
- 存储层面的备份处理，减少 ESXi 主机负载
- 即时快照技术消除性能影响
- 灾难恢复场景：最小化 EBS 集群和 FSx for ONTAP 占用空间
- 支持动态扩展和收缩，按需付费模式

### 35:00-38:30 - Workload Factory 工具与总结
- 免费的 TCO 计算器工具，简化成本估算
- 支持最佳实践的自动化部署配置
- 网址：console.workloads.netapp.com
- 关键收益：控制一致性、企业级功能、成本节省
- 会议总结与问答环节安排