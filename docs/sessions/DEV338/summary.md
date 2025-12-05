# AWS re:Invent 2025 会议总结：使用 CDK 和 Grafana 实现安全的 Amazon ECS 可观测性

## 会议概述

本次技术分享由 Chiku 主讲,主题为"使用 CDK 和 Grafana 实现安全的 Amazon ECS 可观测性"。演讲源于一个实际业务场景:在一家医疗初创公司工作时,非技术人员难以通过 CloudWatch 查看应用程序日志和运行状态,无法实时了解患者注册、医生互动等业务流程。为解决这一痛点,演讲者探索了开源解决方案,最终选择了 Loki 和 Grafana 组合,既能补充 CloudWatch 功能,又能提供实时洞察和直观的交互式仪表板。

演讲者进一步扩展了这个解决方案,构建了完整的可观测性框架,涵盖日志、指标和追踪三大支柱。整个架构采用基础设施即代码(IaC)方法,使用 AWS CDK 进行开发和部署,大幅缩短了开发时间和上线周期。该方案强调安全优先、开源灵活性和供应商独立性,通过 OpenTelemetry(OTEL)标准实现了一次插桩、多处发送的能力,可以将遥测数据发送到 AWS X-Ray、Amazon Managed Prometheus 等多个目标。

整个架构设计包括公有子网和私有子网的网络隔离、AWS Client VPN 安全连接、ECS 任务的 Sidecar 容器模式、以及与 DynamoDB、SQS 等 AWS 服务的集成。演讲还展示了实际的错误追踪演示,通过模拟 404 错误展现了如何利用 Grafana 和 Application Signals 快速定位问题根源。

## 详细时间线与关键要点

[00:00 - 01:30] 开场与背景介绍
- 演讲者 Chiku 介绍会议主题:使用 CDK 和 Grafana 实现安全的 Amazon ECS 可观测性
- 说明演讲动机:2024年6月与 CTO 讨论的实际业务问题

[01:30 - 03:45] 问题场景描述
- 医疗初创公司的非技术人员无法有效使用 CloudWatch 查看应用日志
- 需要实时查看患者注册、医生互动等业务流程
- 非技术用户频繁需要技术团队协助理解系统状态

[03:45 - 05:20] 解决方案选型
- 选择 Loki 和 Grafana 作为核心工具
- 设计目标:补充 CloudWatch、提供实时洞察、美观的交互式仪表板
- 强调供应商独立性和开源灵活性

[05:20 - 06:30] 方案扩展与架构演进
- 从单纯的日志查看扩展到完整的可观测性框架
- 添加指标(Metrics)和追踪(Traces)功能
- 采用 AWS CDK 实现基础设施即代码,缩短开发和部署时间

[06:30 - 08:00] 架构概览
- 展示高层架构图
- 涉及组件:AWS Client VPN、Amazon Prometheus、X-Ray、Application Signals
- 演讲者自我介绍:全栈工程师、AWS 认证专家、认证厨师

[08:00 - 09:30] 会议议程
- 可观测性详解(AWS 方式)
- 三大核心支柱:安全、CDK、Grafana
- 应用演示
- 后续行动与资源

[09:30 - 12:00] 可观测性基础概念
- 定义:从外部观察系统内部运行状态的能力
- 三大支柱:日志(Logs)、指标(Metrics)、追踪(Traces)
- 日志:记录发生了什么(带时间戳的文本记录)
- 指标:记录发生了多少次(定量测量)
- 追踪:记录如何发生(请求在系统中的完整流转路径)

[12:00 - 14:30] OpenTelemetry 介绍
- OpenTelemetry(OTEL):遥测数据的标准化框架
- 核心优势:一次插桩,多处发送
- 可发送到 AWS X-Ray、Amazon Managed Prometheus 或第三方服务
- CNCF 第二大热门项目(仅次于 Kubernetes)
- 社区驱动的开源项目

[14:30 - 16:30] AWS Distro for OpenTelemetry (ADOT)
- AWS 支持的安全、生产就绪的 OTEL 发行版
- 在 ECS Fargate 上作为 Sidecar 容器运行
- 在 Lambda 上作为 Lambda Layer 运行
- 支持自动插桩,只需添加少量代码片段
- 自动收集追踪、指标并关联数据

[16:30 - 20:00] 架构详细设计 - 用户层
- 公有子网:用户通过公网 URL 访问登录应用
- 私有子网:运行 Grafana 和 Loki
- 登录应用包含两个 Sidecar 容器:
  - ADOT Collector:收集追踪和指标发送到 AWS 服务
  - Fluent Bit(FireLens):收集日志发送到 Loki
- 应用与 AWS SQS 和 DynamoDB 交互

[20:00 - 22:30] 架构详细设计 - 开发者层
- 授权用户(开发者)通过 AWS Client VPN 连接私有子网
- 安全访问 ECS 上的 Grafana 和 Loki 实例
- 使用 EFS 和 S3 实现持久化存储

[22:30 - 25:00] 安全优先方法
- AWS Client VPN:提供加密隧道连接到私有子网
- 网络隔离:公有子网和私有子网分离
- 安全组:实施最小权限原则
- IAM 角色:确保服务间访问权限最小化

[25:00 - 27:30] 可观测性安全层
- 第一层:ADOT Sidecar 通过 IAM 角色安全地将数据发送到 X-Ray 和 Prometheus
- 第二层:应用通过 localhost:4317 访问 ADOT Collector
- 关键优势:连接不离开容器网络,无外部网络交互风险

[27:30 - 29:00] FireLens Sidecar 配置示例
- 展示 ECS 任务定义中的 Sidecar 配置
- 使用私有 Route 53 网络访问 Loki
- 只能在连接到 VPC 时访问,确保安全性

[29:00 - 31:30] AWS CDK 与基础设施即代码
- 代码化管理资源,提高开发效率
- 依赖共享:展示如何在 CDK 中共享资源
- 避免循环依赖
- ECR 扫描:推送时自动扫描容器镜像漏洞

[31:30 - 33:00] EFS 访问点示例
- 创建 EFS 访问点并附加权限
- 在 Loki 任务定义中导入并使用访问点作为存储

[33:00 - 35:00] GitHub 集成与 CI/CD
- GitHub 作为源代码仓库
- 强调使用 OIDC 而非访问密钥(Access Keys)
- OIDC 提供仓库特定的角色和权限
- 集成 CI/CD 流水线,代码推送后自动运行测试
- 实现自动化部署和集中管理

[35:00 - 37:30] 应用演示 - 自动插桩
- 导入 OpenTelemetry 包
- 添加详细日志以便实时查看
- 展示自动插桩代码片段
- 仅需少量代码即可自动收集 SQS 和 DynamoDB 的详细指标和追踪

[37:30 - 40:00] 应用演示 - 自定义指标
- 除了自动插桩的预定义指标,还可以添加自定义指标
- 示例:捕获消息队列统计和成功计数
- 在 Grafana 中查看 Amazon Managed Prometheus 数据
- 展示自定义指标的实时结果

[40:00 - 42:30] 应用演示 - 追踪查看
- 两种查看追踪的方式:
  1. CloudWatch Application Signals
  2. Grafana 仪表板(通过 Application Signals 插件)
- 可以深入查看每个追踪的详细元数据

[42:30 - 46:00] 错误模拟演示 - 404 错误
- 创建 DynamoDB 记录(主键:ID 和 timestamp)
- 故意使用错误的查询参数(timestamp: "latest")触发 404 错误
- 在 Grafana Application Signals 中观察到红色错误指示
- 点击错误可查看详细的 404 错误信息

[46:00 - 48:30] 错误分析 - 追踪视图
- 追踪视图显示错误从 DynamoDB GetItem 调用开始
- 登录应用正常工作,但 GetItem 请求失败
- 清晰展示错误的根本原因和传播路径

[48:30 - 50:00] 错误分析 - 指标视图
- 指标显示登录应用正常工作
- 黄色线条表示 GetItem 请求出现问题
- 显示"Not Found"状态(404 错误)和成功状态的对比
- 指标和追踪结合提供完整的问题视图

[50:00 - 52:00] 经验总结
- 安全优先:从设计之初就内置安全,而非事后补救
- 使用 OpenTelemetry:AWS 已宣布弃用 X-Ray Daemon,转向 OTEL
- OTEL 在开源社区获得广泛支持,实现供应商独立性
- 自动化一切:使用 CDK 和 GitHub(或 GitLab、Bitbucket)实现自动化

[52:00 - 53:30] 资源与联系方式
- 项目源于两部分技术文章
- GitHub 仓库链接和 Medium 文章链接
- LinkedIn 联系方式:Chiku
- 提醒填写移动应用上的调查问卷
- 会后可在后方答疑