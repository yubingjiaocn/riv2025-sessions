# AWS re:Invent 2025 - 使用 AWS Transform 和 Kiro 现代化 .NET Framework 应用程序

## 会议概述

本次代码演示会议由来自斯德哥尔摩的 Alex 和来自伦敦的 Prasad 主讲，重点展示如何使用 AWS 的智能化 AI 工具 AWS Transform 和 Kiro 来现代化传统的 .NET Framework 应用程序。会议采用实时编码的方式，以 Contoso University 这个开源大学管理应用程序为例，演示了从传统 .NET Framework 4.8 应用程序到现代云原生架构的完整迁移过程。

演讲者通过七个步骤的现代化流程，展示了如何将一个依赖 Windows 组件（如 MSMQ、SQL Server、Razor Views）的单体应用程序转换为使用 PostgreSQL、Amazon SQS、React 前端和微服务架构的现代化应用程序，最终部署到 AWS 云平台上。整个过程强调了 AI 辅助开发的强大能力，特别是 Kiro 的规范驱动开发模式。

## 详细时间线与关键要点

### 0:00-5:00 - 会议开场和背景介绍
- 演讲者自我介绍：Alex（斯德哥尔摩）和 Prasad（伦敦）
- 确认听众背景：几乎所有参会者都在管理 .NET Framework 传统应用程序
- 介绍现代化的三个维度：框架现代化、架构现代化、基础设施现代化
- 展示示例应用 Contoso University 的当前架构

### 5:00-15:00 - AWS Transform 服务演示
- 展示 AWS Transform 的全新用户界面（前一天刚更新）
- 演示创建 Windows 现代化作业的流程
- 展示代码发现和评估过程
- 介绍大规模移植功能：可同时转换多个项目
- 展示转换结果：创建新分支，转换 3000 行代码

### 15:00-25:00 - 使用 Kiro 修复编译错误
- 介绍 Kiro AI IDE（几周前正式发布）
- 演示实时编码模式修复构建错误
- 展示 Kiro 自动识别和解决包版本冲突
- 成功将项目从 .NET Framework 4.8 升级到 .NET 8
- 项目现在可以在 macOS 上运行

### 25:00-35:00 - 数据库迁移：SQL Server 到 PostgreSQL
- 创建本地 PostgreSQL 数据库实例
- 使用 Kiro 进行数据库迁移的实时编码
- 解决 datetime2 数据类型兼容性问题
- 修复数据库初始化和种子数据问题
- 成功运行使用 PostgreSQL 的应用程序

### 35:00-45:00 - 规范驱动开发：MSMQ 到 Amazon SQS
- 介绍 Kiro 的规范驱动开发模式
- 演示需求文档自动生成过程
- 展示设计阶段：将通用需求应用到具体项目
- 创建实施计划和任务列表
- 强调规范驱动开发适合复杂的生产级项目

### 45:00-50:00 - 微服务提取和 UI 重构
- 演示通知服务的微服务提取规范
- 展示从单体应用中分离独立可部署的服务
- 介绍 UI 重构：从 Razor Views 迁移到 React
- 展示大规模任务列表：50+ 个表单和 API 的创建
- 说明完整迁移耗时约 4-5 小时（相比手动需要数周）

### 50:00-56:00 - CDK 部署和总结
- 演示使用 CDK 创建 AWS 部署项目
- 展示最终架构：React 前端 + CloudFront，EC2 上的 API，Aurora PostgreSQL
- 总结七步现代化流程的完整成果
- 介绍学习资源：AWS Skill Builder 上的智能化 AI 课程
- 问答环节和会议结束