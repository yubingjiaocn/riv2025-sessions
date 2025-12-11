# AWS re:Invent 2025 - Amazon EKS Capabilities 会议总结

## 会议概述

本次会议由Amazon EKS服务团队的首席产品经理Jesse Butler和产品经理Sriram Ranganathan主讲，重点介绍了Amazon EKS的全新功能层——EKS Capabilities。这是EKS服务自2017年发布以来首次推出的新功能层，旨在帮助客户从简单的集群管理扩展到大规模的Kubernetes平台工程。

会议深入探讨了现代平台工程的核心挑战：如何在保持Kubernetes强大功能和扩展性的同时，简化复杂的多集群管理和GitOps实践。EKS Capabilities通过提供完全托管的GitOps、基础设施即代码和平台抽象功能，帮助客户减少运维负担，专注于业务价值创造。

## 详细时间线与关键要点

### 0:00-10:00 - 开场介绍与背景设定
- Jesse Butler介绍EKS Capabilities的核心理念
- 引用Alan Kay和Dijkstra关于抽象的经典观点
- 强调Kubernetes作为分布式计算民主化工具的重要性
- 80%的企业在生产环境中使用Kubernetes，另有13%正在试点

### 10:00-20:00 - EKS演进历程与平台工程挑战
- 回顾EKS从2017年托管控制平面到Auto Mode的发展历程
- 分析客户在多集群扩展过程中遇到的运维复杂性问题
- 介绍平台工程团队投资的必要性和常见模式
- 阐述云原生系统的核心特征：声明式配置、持续协调、可编程发现性

### 20:00-30:00 - GitOps理论基础与实践挑战
- 详细解释GitOps的四个核心特征
- 分析自管理GitOps环境在规模化过程中的局限性
- 介绍EKS add-ons到EKS Capabilities的功能演进
- 强调基于开源标准和Kubernetes原生体验的重要性

### 30:00-40:00 - EKS Capabilities架构与Argo CD功能
- Sriram详细介绍EKS Capabilities的技术架构
- 演示Argo CD capability的创建和配置过程
- 展示与AWS Identity Center的集成实现单点登录
- 介绍核心资源：Application、Cluster注册、Repository管理

### 40:00-50:00 - ACK与Kro功能深度解析
- 演示ACK (AWS Controllers for Kubernetes)的基础设施管理能力
- 详细说明IAMRoleSelector的高级权限管理模式
- 介绍Kro (Kube Resource Orchestrator)的平台抽象功能
- 展示Resource Graph Definition (RGD)的自定义API创建能力

### 50:00-58:24 - 设计考虑与最佳实践
- Jesse总结多集群系统设计的Hub-and-Spoke vs Local Cluster模式
- 强调IAM和RBAC权限管理的深度防御策略
- 提供运维模型选择的指导原则
- 介绍相关学习资源和后续会议信息