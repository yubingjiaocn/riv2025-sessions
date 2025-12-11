# AWS re:Invent 2025 STG419 会议总结

## 会议概述

本次会议由AWS解决方案架构师Matt Boyd和Prabir Sekhri主讲，主题为"现代化托管文件传输和自动化文件处理"。会议采用实时编码演示的形式，展示了如何使用AWS Transfer Family、GuardDuty恶意软件扫描、Amazon Bedrock代理AI等服务构建现代化的文件传输系统。

演讲者以保险理赔处理系统为用例，演示了从传统SFTP服务器迁移到云原生架构的完整过程。整个解决方案采用事件驱动架构，使用Terraform进行基础设施即代码部署，并集成了AI代理来自动化原本需要人工处理的文件分析任务。

## 详细时间线与关键要点

### 00:00-05:00 会议开场与概述
- Matt Boyd介绍会议形式，强调将进行实时编码演示而非PPT展示
- 介绍托管文件传输(MFT)的定义：在已知业务伙伴或实体之间安全交换和处理文件
- 说明MFT在金融、物流、分析等各行业的重要性
- 概述现代MFT系统的构建模块：Transfer Family、GuardDuty恶意软件扫描、代理AI工作流、EventBridge事件驱动架构

### 05:00-10:00 AWS Transfer Family服务介绍
- 介绍Transfer Family的三个主要组件：
  - 文件传输服务器：支持SFTP、FTPS、AS2协议
  - SFTP连接器：托管的SFTP客户端API
  - Web应用程序：为S3提供基于Web的安全访问界面
- 强调Transfer Family与Amazon EventBridge的集成，支持事件驱动架构

### 10:00-15:00 用例介绍：保险理赔处理系统现代化
- Prabir介绍传统保险理赔处理的三个阶段：
  - 摄取阶段：通过SFTP接收文件
  - 提取阶段：使用基础OCR技术
  - 分析阶段：人工处理，容易出错且不可扩展
- 展示现代化架构的四个阶段：安全基础、恶意软件保护、AI代理处理、用户界面

### 15:00-25:00 第一阶段：构建安全的Transfer Family服务器
- Matt开始实时编码演示，部署Transfer Family服务器
- 展示自定义身份提供商(IDP)解决方案的Terraform配置
- 演示用户认证配置，包括DynamoDB表中的身份提供商和用户配置
- 成功测试SFTP连接和文件上传功能

### 25:00-35:00 第二阶段：实施恶意软件扫描
- Prabir介绍GuardDuty恶意软件扫描的工作原理
- 展示事件驱动架构：EventBridge监听GuardDuty事件，通过SQS队列触发Lambda函数
- 演示文件路由逻辑：清洁文件移至清洁桶，恶意文件移至隔离桶
- 使用EICAR测试文件验证恶意软件检测功能

### 35:00-45:00 第三阶段：AI代理工作流
- 介绍Amazon Bedrock Agent Core和Strands SDK框架
- 展示四个专门的AI代理：
  - 实体检测代理：从PDF提取文本
  - 验证代理：比较文本与图像的一致性
  - 摘要代理：总结所有发现
  - 数据库代理：将实体存储到DynamoDB
- 演示两个理赔案例的处理结果，展示AI代理识别欺诈的能力

### 45:00-52:00 第四阶段：Transfer Family Web应用程序
- Matt介绍Transfer Family Web应用程序与IAM Identity Center和S3 Access Grants的集成
- 展示alpha版本的Terraform模块，简化Web应用程序部署和权限配置
- 演示理赔审核员通过Web界面访问处理后的理赔文件
- 总结完整的现代化文件传输解决方案架构

### 52:00 会议总结
- Prabir介绍Transfer Family Terraform模块已有超过10,000次下载
- 提供GitHub仓库链接和公开路线图信息
- 鼓励社区贡献和反馈