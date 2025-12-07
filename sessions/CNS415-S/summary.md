# AWS re:Invent 2025 LocalStack 会议总结

## 会议概述

本次会议重点介绍了 LocalStack 与 AWS 的合作，展示了如何在本地机器上开发和测试无服务器应用程序。LocalStack 是一个本地 AWS 沙箱环境，允许开发者在不连接云环境的情况下进行应用开发和测试。演讲者强调了传统云开发流程中存在的痛点，包括测试反馈周期长、工具切换频繁、配置复杂以及集成测试困难等问题。

会议的核心亮点是 AWS 与 LocalStack 的深度集成，特别是 AWS Toolkit for VS Code 与 LocalStack 的无缝整合。这一集成于 2025 年 9 月正式发布，为开发者提供了统一的开发体验。通过这种集成，开发者可以在本地环境中快速迭代，使用一键式设置启动 LocalStack，并直接在 IDE 中进行断点调试。LocalStack 目前支持超过 120 个 AWS 服务，并与 Terraform、CDK 等主流基础设施即代码工具完全兼容。

演讲者还展示了 LocalStack 如何通过自动化工具（ASF - AWS Server Framework）、强大的工程团队以及与 AWS 的紧密合作来保持与 AWS 服务的同步更新，甚至实现了同日发布新功能，如 Step Functions 的新特性和 Lambda 托管实例等。

## 详细时间线

0:00 - 0:45 - 开场介绍
- 演讲者欢迎参会者并介绍会议主题
- 现场调查：约半数观众听说过或使用过 LocalStack
- 介绍会议议程，包括 AWS 合作伙伴关系

0:45 - 2:15 - LocalStack 基本概念
- 解释 LocalStack 是本地 AWS 沙箱环境
- 展示传统开发工作流：本地开发 → CI/CD 测试 → 云端部署
- 强调核心优势：即时反馈循环、完全隔离的测试沙箱、自信部署到生产环境

2:15 - 3:30 - 服务支持与工具集成
- LocalStack 支持超过 120 个 AWS 服务（Lambda、SQS、DynamoDB、IAM 等）
- 与主流基础设施即代码工具集成（Terraform、CDK 等）
- 工作原理：通过 Docker 容器运行，使用 CLI 启动，设置 AWS 端点 URL 为 localhost

3:30 - 4:45 - 保持与 AWS 同步的策略
- 三大支柱：
  1. 内部自动化工具（ASF - AWS Server Framework）自动抓取 API 规范
  2. 强大的内部工程团队和开源社区
  3. 与 AWS 的合作伙伴关系，实现同日发布新功能

4:45 - 7:30 - 无服务器开发挑战（Sidar 演讲）
- **挑战一：云端测试速度慢** - 每次代码变更需要完整的验证、测试、部署周期，反馈循环可能长达数小时
- **挑战二：工具间频繁切换** - 在 IDE、CLI 和资源模拟器之间切换造成认知负担
- **挑战三：配置复杂性** - 本地与云端环境配置不一致，导致"在我机器上能运行"的问题
- **挑战四：集成测试困难** - Lambda 与 DynamoDB、S3、SQS 等服务的集成测试设置复杂，开发者被迫在生产环境测试

7:30 - 9:00 - AWS 与 LocalStack 的解决方案
- AWS Toolkit for VS Code 与 LocalStack 直接集成（2025 年 9 月发布）
- 创建统一的开发体验
- 实现本地测试 Lambda 函数与完整 AWS 服务集成
- 消除手动配置服务集成的需求

9:00 - 10:30 - 集成的核心优势
- 一键式 LocalStack 设置，无需复杂的 Docker 命令或配置文件
- 直接在 VS Code IDE 中访问所有模拟资源
- 一键切换本地和云端资源
- 显著加快本地反馈循环：原本需要数分钟的云端测试现在几秒钟即可在本地完成

10:30 - 14:00 - 现场演示（录制视频）
- 创建 SAM（Serverless Application Model）项目 "LocalStack Hello World"
- 使用 sam deploy 命令部署到 LocalStack（指定 profile 为 localstack）
- 部署包含 API Gateway 和 Lambda 函数的应用
- 通过 curl 命令调用本地 API 端点（localhost.localstack.cloud）
- 修改 Lambda 代码并重新部署，展示快速迭代能力
- **核心功能展示**：使用 AWS Toolkit 的远程调试功能，在 Lambda 代码中设置断点，进行实时调试

14:00 - 16:00 - AWS 合作伙伴关系案例
- **Step Functions 集成**：支持测试状态 API、JSON 路径支持和变量等新功能，实现同日发布
- **Lambda 托管实例**：在 re:Invent 期间宣布的新功能，LocalStack 同日支持
- 持续改进与 AWS 的一致性（parity），确保高保真度的本地模拟

16:00 - 17:00 - 未来发展方向
- 持续提升开发者体验
- 增强调试能力和堆栈洞察功能
- IAM 策略调试工具
- AI 辅助开发：LocalStack 提供安全的本地沙箱用于 AI 代理编码

17:00 - 18:00 - 总结与行动号召
- 邀请参会者访问 LocalStack 展位（1626 号）
- 提供现场演示和答疑
- 鼓励通过会议 App 提供反馈
- 感谢参会者并展望本地云开发的未来