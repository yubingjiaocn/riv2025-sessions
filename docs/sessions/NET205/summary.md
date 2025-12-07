# AWS re:Invent 2025 - AWS Interconnect 会议总结

## 一、会议概述

本次会议介绍了AWS与Google Cloud合作推出的全新服务——AWS Interconnect，这是一项革命性的多云连接解决方案。会议由AWS网络专家解决方案架构师Alex、AWS Direct Connect和AWS Interconnect高级产品经理Santiago，以及Google Cloud互连产品高级产品经理Judy共同主讲。

AWS Interconnect旨在解决多云网络连接中长期存在的复杂性问题。传统上，客户需要通过VPN连接、在托管设施中进行路由、使用第三方网络结构或部署覆盖解决方案来实现跨云连接，这些方法都存在可扩展性差、管理开销大、故障点多、支持和故障排除困难等挑战。AWS Interconnect通过提供一个简单的附件对象，将AWS Direct Connect Gateway与Google Cloud Router直接连接，彻底简化了这一过程。

该服务的核心理念是"应该像VPC对等连接一样简单"——客户无需关心底层的路由器、BGP配置、VLAN或物理连接，只需通过API创建和接受连接即可。更重要的是，AWS将该服务的技术规范以Apache 2许可开源，旨在建立一个行业标准，让所有云提供商都能采用相同的互连方式，为客户提供一致的多云连接体验。

## 二、详细时间线与关键要点

### **00:00 - 会议开场与介绍**
- 会议主持人介绍：Alex（AWS网络专家解决方案架构师）、Santiago（AWS Direct Connect和Interconnect高级产品经理）、Judy（Google Cloud互连产品高级产品经理）
- 说明这是200级会议，但会涉及400级的路由内容
- 提醒会议录制并将发布到YouTube

### **02:30 - AWS网络基础架构回顾**
- Amazon VPC：区域级构造（与Google Cloud的全球VPC不同）
- 子网：绑定到可用区，支持IPv4、IPv6和双栈
- VPC对等连接：用于小规模VPC间通信
- AWS Transit Gateway：区域路由中心
- AWS Cloud WAN：全球网络服务，支持网络分段（类似Layer 3 VPN和VRF）

### **05:45 - 混合连接选项介绍**
- Site-to-Site VPN：可终止于Virtual Private Gateway、Transit Gateway或Cloud WAN
- 支持IPsec协议，最近推出了大带宽隧道（最高5 Gbps）
- 支持ECMP（等价多路径）实现流量分配

### **07:20 - AWS Direct Connect详解**
- 专用物理连接，通过Direct Connect设施建立
- Direct Connect Gateway：全球构造，允许跨区域连接
- 支持Private Virtual Interface（连接VPC）、Transit Virtual Interface（连接Transit Gateway或Cloud WAN）和Public Virtual Interface（连接AWS公共端点）
- 可实现三个9或四个9的高可用性架构

### **10:15 - 多云连接的传统方法与挑战**
- **方法1**：Site-to-Site VPN连接到其他云（管理数千个VPN连接极具挑战性）
- **方法2**：通过托管设施使用Direct Connect和其他云服务商的类似服务进行路由
- **方法3**：使用第三方网络结构
- **方法4**：基于设备的覆盖解决方案

### **12:40 - 多云连接面临的核心挑战**
- 可扩展性问题
- 管理开销大
- 额外的故障点
- 支持和故障排除复杂（需要同时联系多个云提供商和第三方）
- 全球覆盖一致性难以保证
- 地理位置对齐困难

### **15:30 - AWS Interconnect愿景与解决方案**
- **核心理念**：连接应该像VPC附件一样简单，无需关心底层路由器
- **目标架构**：AWS Direct Connect Gateway直接连接到Google Cloud Router
- 在预览版中与Google Cloud合作推出

### **17:50 - AWS Interconnect工作原理（客户视角）**
- **创建流程**：在AWS或Google Cloud控制台请求新的互连
- **接受流程**：在另一个云平台确认请求
- 两个主要操作：创建（Create）和接受（Accept）
- 无需配置BGP、Layer 3连接、VLAN等

### **19:20 - AWS控制台操作演示**
- 选择合作伙伴（Google Cloud）
- 选择AWS区域（自动填充对应的Google Cloud区域）
- 选择连接速度（预览版提供1 Gbps免费连接）
- 选择附加点（Direct Connect Gateway）
- 使用密钥在Google Cloud端激活连接

### **22:10 - 底层架构深度解析**
- 客户看到的是单一连接，但底层在多个不同设备上配置了多个逻辑连接
- 每个互连默认跨越至少两个物理设施的四台不同路由器
- 自动实现最高弹性配置（四个9的可用性）

### **24:35 - 智能容量管理**
- API创建跨提供商的新逻辑对象
- 理解建筑物、路由器、连接和链路聚合组（LAG）
- 确保连接分布在四台不同的路由器上
- 采用"最少利用互连"策略自动分配新连接

### **26:50 - 动态扩展能力**
- 连接可以动态扩展或缩减
- 当容量不足时，系统自动将连接迁移到新的逻辑对象
- 利用大容量池满足客户需求

### **28:30 - 维护协调机制**
- AWS和Google Cloud协调维护窗口
- 避免同时对两侧路由器进行维护
- 确保客户始终保持冗余容量

### **30:15 - 开放规范战略**
- 现有API无法满足服务需求
- 需要确保所有云提供商提供一致的体验
- 以Apache 2许可开源规范（无专利限制）
- 目标：建立行业标准，让所有云提供商都能采用

### **33:40 - 核心功能特性**
- 动态扩展和缩减
- 内置弹性（默认四个9可用性）
- 使用MACsec加密所有物理链路
- MACsec必须安全模式：加密会话未建立时链路不会启动

### **35:20 - 公开预览详情**
- 五个区域可用（更多区域即将推出）
- 预览期间提供1 Gbps免费连接
- 包含CloudWatch Network Synthetic Monitor（每个互连一个合成监控器）
- 支持按需扩展容量

### **37:50 - Google Cloud视角：Cloud Interconnect介绍**
- Cloud Interconnect是Google Cloud的私有连接入口
- 从托管设施（互连PoP）提供服务
- 许多PoP与AWS和其他云提供商共址

### **39:30 - Cross-Cloud Interconnect产品**
- 2023年推出
- 将Google边缘路由器扩展到其他云提供商的边缘路由器
- 客户购买Cross-Cloud Interconnect端口和Direct Connect
- Google代表客户终止交叉连接
- 无需本地机房或物理路由器

### **41:45 - Google Cloud弹性架构**
- 边缘可用性域（EADs）：托管设施内的独立故障域
- 不共享电源、上行链路或故障
- VLAN附件：虚拟化互连为多个VLAN
- Cloud Router：编排路由，具有控制平面冗余

### **43:20 - Cross-Cloud Interconnect的挑战**
- 最小容量为10 Gbps（接口线速）
- 需要现场技术人员部署（有交付周期）
- 客户往往过度购买容量以确保可用性

### **44:50 - 合作伙伴关系的重要性**
- AWS和Google Cloud共享简化基础设施的愿景
- 共同承担支持责任
- 为客户提供一致的体验

### **46:00 - 会议总结**
- AWS Interconnect代表多云连接的范式转变
- 从复杂的多供应商架构转向简单的API驱动附件
- 开放规范确保行业采用和客户信心
- 预览版现已在五个区域推出

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


关键技术术语：
- BGP（Border Gateway Protocol）：边界网关协议
- VPC（Virtual Private Cloud）：虚拟私有云
- ECMP（Equal-Cost Multi-Path）：等价多路径
- MACsec（Media Access Control Security）：媒体访问控制安全
- LAG（Link Aggregation Group）：链路聚合组
- EAD（Edge Availability Domain）：边缘可用性域