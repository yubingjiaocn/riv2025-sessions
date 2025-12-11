# AWS re:Invent 2025 LocalStack 会议总结

## 会议概述

本次会议重点介绍了LocalStack与AWS的合作伙伴关系，以及如何在本地机器上开发和测试AWS服务应用程序。演讲者包括LocalStack团队的Waldemar和AWS无服务器团队的Shridhar。会议展示了AWS Toolkit for VS Code与LocalStack的集成，这一集成于2025年9月正式发布，为开发者提供了统一的本地开发体验。

LocalStack是一个本地AWS沙箱环境，允许开发者在不连接云环境的情况下进行应用程序开发和测试。目前支持超过120个AWS服务，包括Lambda、SQS、DynamoDB、IAM等，并与Terraform、CDK等基础设施代码工具集成。通过与AWS的紧密合作，LocalStack能够实现同日发布新功能，确保开发者能够立即获得AWS最新特性的本地开发体验。

## 详细时间线与关键要点

### 0:00-2:00 开场介绍
- 演讲者进行现场调研，约一半参会者听说过LocalStack
- 介绍会议议程，重点讨论AWS合作伙伴关系

### 2:00-5:00 LocalStack核心概念
- LocalStack定义：本地AWS沙箱环境
- 传统开发流程：本地环境 → 本地测试 → CI/CD测试 → 云端部署
- 核心优势：
  - 即时反馈循环
  - 完全隔离的测试沙箱
  - 增强部署信心
- 支持120+个AWS服务
- 与现有基础设施代码工具集成

### 5:00-7:00 技术实现机制
- 基于Docker容器运行
- 安装CLI后使用LocalStack start命令启动
- 通过设置AWS endpoint URL为localhost进行交互
- 保持AWS创新步伐的方法：
  - ASF（AWS服务器框架）自动化API规范抓取
  - 强大的内部工程团队和开源社区
  - 与AWS的合作伙伴关系实现同日发布

### 7:00-11:00 无服务器开发挑战
- 四大核心挑战：
  1. 云端测试延迟：每次代码变更需要完整的验证-测试-部署周期
  2. 工具间上下文切换：IDE、CLI、资源模拟器间频繁切换
  3. 配置复杂性：本地与云环境配置不一致问题
  4. 集成测试困难：Lambda与DynamoDB、S3、SQS等服务集成测试复杂

### 11:00-14:00 解决方案与集成演示
- AWS Toolkit for VS Code与LocalStack集成特性：
  - 一键LocalStack设置
  - 直接在VS Code中访问模拟资源
  - 本地与云资源间无缝切换
  - 显著加快本地反馈循环
- 3分钟演示视频展示：
  - 创建"LocalStack HelloWorld"SAM应用
  - 使用LocalStack配置文件进行SAM部署
  - API Gateway + Lambda + DynamoDB完整调用链
  - 远程调试功能：设置断点、代码步进调试

### 14:00-17:00 合作伙伴关系与未来展望
- 现有合作成果：
  - Step Functions测试集成
  - TestState API、JSONata支持、Variables功能同日发布
  - Lambda Managed Instances同日发布
- 未来发展方向：
  - 提升模拟器保真度
  - 增强开发者体验功能
  - AI驱动的应用开发支持
  - 安全本地沙箱环境
- 邀请参会者访问1626号展位进行现场演示和反馈