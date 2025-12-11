# AWS re:Invent 2025 - STG339: 使用事件驱动SFTP帮助客户现代化托管文件传输

## 会议概述

本次会议由AWS Transfer Family产品管理负责人Smitha Sriram主讲，联合产品经理Suh和首席解决方案架构师Prabir共同呈现。会议重点介绍了如何使用AWS Transfer Family和B2B Data Interchange服务来现代化托管文件传输(MFT)和EDI工作流程。

演讲者首先分析了当前MFT和EDI领域的趋势，包括对安全性、治理、简化管理的需求，以及自动化、AI就绪和实时洞察的新兴需求。随后深入介绍了AWS Transfer Family的核心功能特性，包括服务器、连接器和Web应用程序等组件。会议最后通过一个完整的保险理赔处理系统演示，展示了如何构建基于代理AI的现代化云原生MFT解决方案。

## 详细时间线与关键要点

### 0:00-5:00 开场与背景介绍
- 会议开场，介绍演讲者团队
- 调查听众对SFTP、MFT、AS2、EDI等技术的使用情况
- 介绍会议议程：MFT和EDI概述、趋势分析、功能深入讲解、实际演示

### 5:00-15:00 托管文件传输业务价值与趋势
- 阐述MFT在不同行业的应用场景：支付对账、医疗理赔、数据集销售、内部流程自动化
- 介绍MFT的四大支柱：行业标准协议支持、身份验证与访问控制、处理与自动化、强大的审计功能
- 分析当前六大趋势：安全性、治理工具、简化管理、自动化、AI就绪、实时洞察

### 15:00-20:00 AWS Transfer Family服务介绍
- 介绍AWS Transfer Family在2018年re:Invent发布，已有7年客户服务经验
- 强调服务的完全托管、高可用性、实时扩展特性
- 介绍基于事件驱动的架构设计，与Amazon EventBridge集成
- 展示AWS B2B Data Interchange服务，支持X12文档的自动化翻译和验证

### 20:00-25:00 客户成功案例
- FICO案例：全球信用评分和分析领域领导者，通过迁移到AWS Transfer Family消除基础设施开销，降低TCO
- BMW集团案例：利用Transfer Family将生产线摄像头数据传输到S3，支持AI和分析处理1.3PB数据
- 合作伙伴案例：ScaleCapacity帮助洛杉矶市节省成本，Bizcloud Experts帮助供应链客户年节省超过100万美元

### 25:00-35:00 Transfer Family服务器功能详解
- 支持SFTP、FTP、FTPS、AS2协议的完全托管端点
- 网络控制选项：公共端点、VPC端点、面向互联网的VPC端点
- IPv6双栈支持，可同时支持IPv4和IPv6客户端
- 三种身份验证模式：服务托管、AWS Directory Services集成、自定义身份提供商
- 多方法身份验证支持，动态切换IdP选项

### 35:00-40:00 存储集成与连接器功能
- 直接集成Amazon EFS和Amazon S3，支持S3访问点
- 新增支持S3访问点与FSX for NetApp ONTAP集成
- SFTP连接器功能：作为完全托管的SFTP客户端连接远程服务器
- 支持文件传输、检索、目录列表、远程文件操作（移动、删除、重命名）
- VPC连接器支持，可连接私有SFTP服务器

### 40:00-45:00 Transfer Family Web应用程序
- 为非技术用户提供托管Web UI，通过IAM Identity Center进行身份验证
- 使用S3访问授权实现细粒度访问控制
- 支持公司品牌定制：徽标、图标、页面标题
- 符合HIPAA、FedRAMP、PCI等合规标准
- 支持VPC端点，提供私有网络访问选项

### 45:00-50:00 B2B Data Interchange与架构模式
- 展示Transfer Family与B2Bi结合的典型EDI处理架构
- 文件通过SFTP/AS2传输到S3，B2Bi监听事件进行验证和转换
- 支持四个区域：美国东部、美国西部、欧洲（都柏林）等
- 与EventBridge集成实现后处理自动化

### 50:00-54:30 现代化MFT演示与总结
- 演示基于代理AI的保险理赔处理系统
- 展示完整工作流：安全文件传输、恶意软件扫描、智能处理、Web界面访问
- 使用Terraform模块进行基础设施即代码部署
- 介绍STRANDS开源SDK用于构建AI代理
- 提供资源链接：用户指南、网站、实践研讨会等