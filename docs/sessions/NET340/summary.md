# AWS re:Invent 2025 网络服务更新综合总结

## 会议概述

本次AWS re:Invent 2025的网络专题分会由两位AWS网络专家解决方案架构师Alex和Andrew Graeme主讲，全面介绍了过去一年AWS网络服务的重大创新和功能发布。这是一场300级别的技术深度会议，涵盖了从基础网络架构到高级应用网络的广泛主题。

会议首先回顾了AWS网络的基础架构，包括全球骨干网络（拥有超过900万英里的光纤）、区域和可用区的概念。随后深入探讨了Amazon VPC的核心组件，包括子网、安全组、网络ACL和AWS Network Firewall等安全控制机制。在连接性方面，讲师详细介绍了互联网网关、NAT网关、弹性负载均衡器套件，以及通过AWS PrivateLink连接AWS服务的方法。

会议的重点放在2025年的重大创新上，特别是在VPC安全、应用网络（VPC Lattice）、混合连接和加密方面的突破性进展。讲师通过大量实际架构图和使用场景，展示了如何利用这些新功能构建更安全、更高效、更易管理的云网络架构。

## 详细时间线与关键要点

00:00:00 - 会议开场与基础介绍
- Alex和Andrew介绍自己作为AWS网络专家解决方案架构师的身份
- 说明这是300级别会议，内容将快速且深入
- 提醒观众可以在动画结束后拍照，Q&A环节将在会议结束后进行

00:02:00 - AWS网络基础架构回顾
- AWS全球骨干网络：超过900万英里的光纤基础设施
- 区域、可用区的概念说明
- Amazon VPC作为区域级构造，子网作为可用区级构造
- 支持IPv4、IPv6和双栈配置

00:03:30 - VPC安全机制
- 网络访问控制列表（NACL）：子网级别的无状态防火墙
- 安全组：有状态防火墙过滤
- AWS Network Firewall：提供流量检测、解密和高级过滤控制

00:05:00 - VPC连接性选项
- 互联网连接：Internet Gateway和Egress-only Internet Gateway
- IPv4使用NAT Gateway（区域级高可用构造）
- IPv6使用Egress-only Internet Gateway

00:06:30 - 应用扩展与负载均衡
- 弹性负载均衡器套件：Application Load Balancer、Network Load Balancer、Gateway Load Balancer
- 后续将深入探讨这些部署模型

00:07:30 - AWS服务连接（PrivateLink）
- Gateway Endpoints：连接S3和DynamoDB，无需VPC接口
- Interface Endpoints：在VPC中部署接口，需要DNS更新

00:09:00 - 应用间连接
- PrivateLink支持客户管理的服务
- 支持区域内和跨区域连接
- Amazon VPC Lattice：大规模应用连接的托管服务

00:11:00 - VPC互连选项
- VPC Peering：区域内和跨区域，但扩展性有限
- AWS Transit Gateway：区域路由中心，支持最多5000个VPC
- 基于静态路由，不是动态智能路由器

00:13:00 - 全球动态连接
- AWS Cloud WAN：完全托管的全球网络服务
- 与Transit Gateway的区别：Cloud WAN是全球托管服务，支持动态连接
- 无需管理静态路由，智能附加到核心网络边缘

00:15:00 - 混合连接
- Site-to-Site VPN：基于IPSec的VPN连接
- Direct Connect：三种虚拟接口类型（私有、传输、公共）
- AWS Verified Access：无需VPN的远程访问，集成设备管理和身份验证

00:17:00 - 2025年VPC创新：NAT Gateway区域模式
- 新推出区域级NAT Gateway
- 简化配置和维护
- 无需在单独子网中部署
- 自动扩展到新增可用区
- 提高可扩展性和公网IP管理

00:19:30 - Network Firewall多VPC端点支持
- 支持多个VPC连接到同一个Network Firewall
- 单一防火墙策略控制多个VPC
- 建议按生产/开发环境分离
- 可在策略中引用单独端点实现细粒度分段

00:22:00 - Network Firewall功能增强
- 主动威胁防御：集成AWS威胁情报
- 合作伙伴托管规则：自动更新第三方安全规则
- 控制台和监控功能改进

00:24:00 - Network Firewall Proxy（重大发布）
- 托管代理服务，替代客户自建Squid等代理
- 显式代理配置，无需修改路由表
- 支持多层检测：DNS前检测、请求前检测、请求后检测
- 与PCA集成支持TLS流量检测

00:27:00 - Proxy流量处理流程
- 客户端通过HTTP CONNECT建立代理连接
- 多阶段检测：主机名检测、请求方法检测、响应内容检测
- 支持细粒度控制（如允许GET但不允许POST）
- 需要配置TLS检测才能完全检查加密流量

00:30:00 - Proxy分布式部署
- 支持多VPC端点连接到同一代理
- 适用于完全隔离的VPC环境
- 可与Transit Gateway或Cloud WAN集成
- 集中式VPC部署模式

00:33:00 - VPC Route Server
- 允许VPC内实例通过BGP更新路由表
- 用例：任播、自定义故障转移
- 浮动IP场景：主备实例间自动切换

00:36:00 - Transit Gateway与Network Firewall原生集成
- Network Firewall可直接作为Transit Gateway附件
- 无需创建单独的安全VPC
- 简化部署和维护

00:38:00 - Transit Gateway灵活成本分配
- 支持将数据处理费用分配给源、目标或Transit Gateway所有者
- 便于跨部门成本核算
- 帮助理解工作负载真实成本

00:40:00 - VPC加密控制（重大发布）
- 监控模式：识别不合规资源，允许例外
- VPC Flow Logs新增加密字段：Nitro加密、应用加密
- 强制模式：确保VPC内所有资源支持加密
- 解决"流量是否加密"的疑问

00:44:00 - 应用网络：PrivateLink跨区域支持
- AWS托管服务现支持跨区域PrivateLink
- 在不同区域VPC中创建接口端点
- 组织级别控制跨区域服务访问

00:46:00 - PrivateLink全面支持IPv6
- Gateway Endpoints支持IPv6（S3和DynamoDB）
- Interface Endpoints支持IPv6
- 消除IPv6采用障碍

00:48:00 - Amazon VPC Lattice深度解析
- 专为内部应用间连接设计
- VPC Lattice Services：HTTP/HTTPS应用（第7层）
- VPC Lattice Resources：TCP应用（如数据库）
- Service Network：逻辑边界，连接需要通信的资源

00:52:00 - VPC Lattice关联类型
- Service Associations：服务关联到服务网络
- Resource Associations：资源关联到服务网络
- VPC Associations：VPC关联到服务网络
- Service Network Endpoint Associations：端点关联

00:54:00 - VPC Lattice授权策略
- 基于IAM的细粒度访问控制
- 表达"A可以访问B，但B不能访问C"的意图
- 无数据处理费用，无小时费用

00:57:00 - VPC Lattice资源自定义DNS（新功能）
- 资源创建时定义自定义DNS名称
- 无需管理私有托管区域
- 自动传播到客户端VPC
- 多级控制：资源关联、服务网络、客户端VPC

01:00:00 - 资源网关可配置IP地址
- 默认每个可用区使用/28 CIDR
- 现可指定IP地址数量和具体地址
- 优化IP地址使用

01:02:00 - 服务网络关联vs服务网络端点
- 服务网络关联：类似S3 Gateway Endpoint，仅VPC内访问
- 服务网络端点：类似S3 Interface Endpoint，可从VPC外访问
- 根据访问需求选择

01:04:00 - 本地应用连接到Lattice
- 使用"传输VPC"（非BGP意义）
- 传输VPC具有可路由到本地的IP地址
- 左侧VPC可使用重叠IP（Lattice支持）
- 通过资源配置和自定义DNS实现

01:07:00 - 本地客户端访问Lattice资源
- 服务网络端点提供每个资源/服务的FQDN
- 通过本地DNS配置映射
- 可使用入站解析器端点或托管区域委派
- 支持安全组过滤

01:10:00 - 在服务网络端点前部署防火墙
- 服务网络端点是第3层构造，有ENI
- 可部署防火墙，但建议优先使用授权策略
- 授权策略无额外成本

01:11:00 - 授权策略与SIGV4签名
- 无需SIGV4签名即可使用授权策略
- 未签名流量无法使用Principal ID条件键
- 仍可使用源IP、源VPC、源账户等条件键

01:13:00 - 跨区域服务通信架构
- Lattice当前不支持原生跨区域
- 使用传输VPC提供第3层连接
- 每个区域一个传输VPC，需非重叠IP
- 服务网络端点提供入口，资源配置指向远程服务

01:16:00 - 集中化PrivateLink端点
- 使用Transit Gateway集中管理端点
- VPC Lattice可实现相同功能
- 通过资源自定义DNS自动管理客户端VPC的DNS

01:18:00 - 集中化SaaS提供商访问
- 将SaaS提供商端点作为Lattice资源
- 可检查流向SaaS提供商的流量
- 资源网关是第3层构造，支持防火墙部署

会议结束
- 强调了2025年AWS网络服务的重大创新
- 涵盖从基础设施到应用层的全面更新
- 为构建现代化、安全、可扩展的云网络架构提供了完整解决方案