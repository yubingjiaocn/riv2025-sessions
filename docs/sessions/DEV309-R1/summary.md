# DEV309: 使用AI编码助手构建无服务器应用程序

## 会议概述

本次会议由AWS开发者倡导者Gunnar Grosch和无服务器开发者体验首席产品经理Shridhar Pandey主讲，展示了如何使用AI编码助手（特别是Kiro CLI）构建完整的无服务器应用程序。会议采用代码演示形式，从零开始构建了一个图像生成应用程序，包含前端和后端，演示了AI助手在无服务器开发中的实际应用。

演讲者强调了无服务器开发者体验的两个循环：内循环（本地开发环境中的快速迭代）和外循环（从代码推送到生产的完整流程）。整个演示过程中，演讲者没有手写任何代码，完全依靠AI助手和MCP服务器来完成应用程序的构建、部署和测试。

## 详细时间线与关键要点

### 0:00-5:00 会议介绍与背景设置
- 介绍演讲者和会议主题DEV309
- 解释无服务器开发者体验的内循环和外循环概念
- 介绍将要使用的AI工具Kiro CLI（原Amazon Queue developer CLI）

### 5:00-10:00 应用架构概述
- 展示要构建的图像生成应用程序架构
- 后端：API Gateway + Lambda函数（Node.js）+ Bedrock Titan Image Generator v2 + S3存储
- 前端：React + Vite + Amplify Hosting
- 可观测性：CloudWatch Application Signals、X-Ray、Power Tools

### 10:00-15:00 MCP服务器配置与初始项目创建
- 演示Kiro CLI的MCP服务器配置
- 启用AWS Serverless MCP服务器，提供专业的无服务器开发工具
- 使用AI助手创建SAM项目，包含HTTP API和两个Lambda函数
- 展示AI助手如何自动运行sam init、sam build、sam validate命令

### 15:00-25:00 后端API开发与部署
- 完成初始SAM项目的创建和构建
- 手动部署应用程序到AWS（sam deploy --guided）
- 使用AI助手获取API端点并测试功能
- 演示如何让AI助手自动测试部署的API端点

### 25:00-35:00 添加S3存储功能
- 使用AI助手向SAM模板添加S3存储桶
- 更新Lambda函数以支持文件上传和预签名URL生成
- 实现最少权限IAM策略
- 重新构建和部署应用程序
- 测试S3集成功能

### 35:00-40:00 引导文件（Steering Files）配置
- 演示如何创建全局和项目特定的引导文件
- 展示如何通过引导文件控制AI助手的行为
- 设置代码风格、安全规则、提交消息格式等偏好

### 40:00-45:00 集成Bedrock图像生成
- 更新Lambda函数以使用Bedrock Titan Image Generator v2
- 配置正确的IAM权限和环境变量
- 设置更长的Lambda超时时间
- 部署并测试实际的图像生成功能
- 成功生成"Las Vegas in winter"主题图像

### 45:00-50:00 前端开发
- 使用AI助手创建React前端应用
- 实现单页面应用，包含文本输入、生成按钮和图像画廊
- 配置环境变量和API调用
- 演示完整的端到端图像生成流程

### 50:00-55:00 控制台集成与可观测性
- 展示AWS控制台的"在VS Code中打开"功能
- 添加AWS Lambda Power Tools进行应用程序监控
- 配置结构化日志、追踪和自定义指标
- 启用CloudWatch Application Signals进行APM监控

### 55:00-58:30 总结与资源分享
- 强调整个过程中零手写代码的成就
- 突出分步骤、可控的开发方法
- 分享相关资源：Kiro CLI文档、MCP服务器、Serverless Land等
- 感谢参会者并结束演示