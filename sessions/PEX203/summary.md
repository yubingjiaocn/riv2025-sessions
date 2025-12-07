# AWS re:Invent 2025 会议总结：使用 Agentic AI 加速工作负载现代化

## 会议概述

本次会议由 Nick O'Brien 和 Keith Groom 主讲，重点介绍了 AWS 如何利用新一代 Agentic AI 技术加速工作负载的迁移和现代化。会议强调了企业面临的创新压力——虽然 84% 的 CEO 认为创新至关重要，但只有 6% 对自己的创新速度感到满意。AWS 推出了一系列 Transform 工具套件，旨在将项目成本降低 50% 以上，显著缩短交付时间。

会议展示了 AWS 内部使用这些技术已完成 10,000 次转换，节省了近 5,000 个开发人员年的工作时间。Thompson Reuters 使用这些工具将技术债务减少了 50%，速度提升了 4 倍，每月转换 150 万行代码。这些工具不仅适用于 AWS 客户，也为咨询合作伙伴提供了变革性的交付实践机会。

Keith 详细介绍了四大核心产品：Transform for Assessments（评估工具）、Transform for VMware（VMware 迁移）、Transform for Full Stack Modernization（全栈 Windows 现代化）和 Transform for Mainframe（大型机现代化）。这些工具通过 Agentic AI 自动化了传统上最复杂和耗时的迁移任务，如依赖关系分析、网络拓扑转换和代码重构。

## 详细时间线

00:00 - 开场介绍
- Nick O'Brien 和 Keith Groom 介绍会议主题：使用 Agentic 技术加速工作负载现代化
- Keith 介绍自己在 AWS 工作 9 年，负责全球合作伙伴迁移工具和服务策略

02:30 - 创新压力与市场需求
- Nick 引用 Jeff Bezos 的"神圣不满足"理论：消费者永远追求更多选择、更低价格和更快速度
- 研究显示 84% 的 CEO 认为创新至关重要，但只有 6% 对创新速度满意
- McKinsey 研究表明，能够快速适应的企业可获得数万亿美元的价值

05:00 - AWS 内部使用案例
- AWS 内部已使用 Agentic 技术完成 10,000 次应用转换
- 节省近 5,000 个开发人员年的时间
- 释放资本用于业务再投资

06:30 - 客户成功案例
- Thompson Reuters：技术债务减少 50%，速度提升 4 倍，每月转换 150 万行代码
- Kalin（2024 年度迁移合作伙伴）与 NetSmart 合作，显著缩短项目周期

08:00 - Keith 开始技术介绍
- 观众调查：大部分是客户，少数是咨询合作伙伴和 ISV 合作伙伴
- 强调这些工具将使项目成本降低 50% 以上，交付速度显著提升

10:00 - 迁移三阶段方法论
- 评估（Assessment）：分析当前环境
- 动员（Mobilize）：构建 Landing Zone 和运营模型
- 迁移（Migrate）：实际迁移工作负载

11:30 - Transform for Assessments
- 传统工具 Migration Evaluator 需要通过销售团队部署
- 新工具直接在 AWS 控制台中使用，15 分钟生成报告
- 支持上传现有清单（RVTools、MPA、CMDB 等）
- 分析 x86 服务器、存储、数据库和许可证
- 通过优化许可证和基础设施实现约 60% 的成本节省
- 包含聊天机器人功能，可与数据交互

16:00 - Transform for VMware
- 从本地 VMware 环境迁移到 EC2 实例
- 消除 VMware 许可成本
- 自动化最复杂的任务：
  - 发现和数据摄取
  - 自动创建迁移波次计划
  - 网络转换和拓扑映射（将硬编码 IP 地址映射到 VPC）
  - 使用 MGN 工具执行 VM 迁移
- 包含人工验证和测试环节

19:30 - 合作伙伴案例：Slalom 和 Vector
- Slalom 帮助澳大利亚能源公司 Vector 完成大规模 VMware 迁移
- 100% 准确率，时间缩短一半

21:00 - Transform for Full Stack Modernization
- 扩展了之前发布的 Transform for .NET
- 支持 .NET Framework 3.5 及更高版本转换到跨平台 .NET 8 或 10
- 通过消除 Windows Server 许可证实现高达 70% 的成本节省
- Windows Server 许可证占 EC2 实例成本的 60%

23:30 - SQL Server 转换
- 将 SQL Server 转换到 Aurora PostgreSQL
- 转换存储过程和业务逻辑
- SQL Server Enterprise 每核心约 4,000 美元
- 消除数千个核心的许可成本

25:00 - 虚拟机容器化
- 将 Windows Server 上的虚拟机迁移到 ECS 或 EC2
- 支持跨平台 .NET，可在 Linux 服务器或容器上运行

27:00 - .NET Web UI 移植
- "苹果到苹果"移植：MVC、Razor、ASP.NET 到 ASP.NET Core
- "苹果到橙子"移植：Web Forms 到 Blazor

28:30 - SQL Server 依赖关系分析
- Agent 提取业务逻辑和存储过程
- 识别 .NET 应用程序之间的依赖关系
- 同时转换到 PostgreSQL 和 .NET Core

29:30 - Experian 案例
- 数据办公室 7 个遗留应用迁移到 .NET 8
- 开发工作量减少 40%
- 转换 687,000 行代码
- 节省 300 个工程小时

32:00 - Transform Custom
- 转换任何代码模式以减少技术债务
- 支持 Java 运行时升级、Node.js 升级等
- 可使用开箱即用的转换或基于自定义数据构建转换
- 今天正式发布
- Agent 可学习并根据更多数据和文档进行转换

35:00 - 产品套件说明
- 目前这些是独立的服务
- 未来将整合为产品套件
- 可实现应用现代化速度提升 80%

36:30 - Composability Initiative（可组合性计划）
- 允许合作伙伴将自己的 Agent 集成到 AWS 工具中
- 支持特定行业和用例的自定义工作流
- 合作伙伴可开发差异化产品
- 现已正式发布

38:00 - Transform for Mainframe
- 分析 IBM z/OS 应用程序（通常是 COBOL）
- 生成技术和业务规则文档
- 代码分解为模块
- 转换到 Java
- 包含内置测试模块
- 解决文档缺失和人才短缺问题

41:00 - Toyota 案例
- 4,000 万行 COBOL 代码
- 数千个遗留程序
- 使用 Transform 分析任务和识别缺失部分
- 结合 Amazon Q 进行文档查询
- 现代化速度提升 50%
- CTO Brian 高度评价

44:00 - Nick 总结：合作伙伴资金支持
- 2015-2016 年大型企业开始大规模迁移（Capital One、GE）
- 客户反馈：成本高、时间长、缺乏技能
- 2020 年 AWS 改变策略，提供资金支持消除成本顾虑
- 推出多个资金计划支持合作伙伴为客户提供评估和迁移服务
- 客户可选择合作伙伴，无承诺，可分阶段进行