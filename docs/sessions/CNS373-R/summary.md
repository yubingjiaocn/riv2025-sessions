# AWS re:Invent 2025 会议总结：使用 Amazon Kiro 和 MCP 服务器加速构建无服务器应用

## 会议概述

本次技术分享会由 AWS 的两位解决方案架构师 Sean Kendall 和 Brian Zambrano 主讲，重点介绍了如何使用 Amazon Kiro（原 Amazon Q Developer）和模型上下文协议（MCP）服务器来加速构建无服务器应用程序。

Sean Kendall 是一位专注于无服务器和生成式 AI 的首席解决方案架构师，在 AWS 工作超过六年。Brian Zambrano 同样拥有近七年的 AWS 经验，目前在生成式 AI 创新中心工作，该团队为客户免费构建生成式 AI 概念验证和 MVP 项目。

会议的核心主题是展示如何通过 AI 辅助工具显著提升开发效率。演讲者强调，无服务器架构本身就能让开发者快速构建应用，而结合 AI 工具和 MCP 服务器后，开发速度可以达到"非常非常快"的程度。整个会议采用实际编码演示的形式，构建了一个完整的井字棋游戏后端，展示了从零到部署的全过程。值得注意的是，Amazon Q 品牌已经迁移到 Kiro 品牌，这是从 Code Whisperer 到 Amazon Q Developer 再到 Kiro 的演进过程。

## 详细时间线与关键要点

### **00:00:00 - 会议开场与讲师介绍**
- 周一早晨的 re:Invent 会议开场
- Sean Kendall 自我介绍：AWS 首席解决方案架构师，专注无服务器和生成式 AI，来自加拿大卡尔加里
- Brian Zambrano 介绍：在 AWS 工作近七年，目前在生成式 AI 创新中心工作，为客户免费构建 GenAI MVP

### **00:02:30 - 生成式 AI 创新中心介绍**
- Brian 强调该中心为拥有 AWS 账户团队的客户免费构建生成式 AI 概念验证
- 鼓励观众联系账户团队了解这项服务

### **00:03:15 - 会议主题与互动调查**
- 主题：使用 Kiro 和 MCP 服务器加速构建无服务器应用
- 现场调查：多数观众听说过 Kiro，但使用过的人较少
- 大部分观众正在构建无服务器应用

### **00:04:30 - 会议内容概览**
- 开发工具概述
- 井字棋游戏的目标架构
- 前端已预先构建并部署，包含 OpenAPI 规范
- 提示工程演示
- 实际编码：Sean 使用 Kiro CLI，Brian 使用 Kiro IDE

### **00:06:00 - Amazon Kiro 品牌演变说明**
- 观众提问：会议原名为"使用 Amazon Q 构建无服务器应用"
- 解释：Q 品牌正在迁移到 Kiro
- 演进历程：Code Whisperer → Amazon Q Developer → Kiro
- CLI 命令从 q 变为 kiro-cli

### **00:08:00 - Kiro 两种使用方式介绍**
- **Kiro CLI**：Sean 的首选，可以在终端输入提示词，完全自动化执行，适合"睡前启动，醒来查看结果"的工作流程
- **Kiro IDE**：类似 VS Code 的 IDE 体验，是 VS Code 的分支版本

### **00:09:30 - MCP 服务器概念介绍**
- 现场调查：大多数人听说过 MCP，但使用的人较少
- MCP = Model Context Protocol（模型上下文协议）
- 作用：为 AI 模型提供访问最新信息和执行操作的标准化接口

### **00:11:00 - Kiro IDE 界面详解**
- 左侧有 Kiro 图标（小幽灵）
- 主要功能区：
  - **Specs**：规范驱动开发（Kiro 独有功能）
  - **Agent Steering Docs**：代理引导文档
  - **MCP Server Configuration**：MCP 服务器配置
- 右侧聊天界面：
  - **Vibe Session**：常规聊天模式
  - **Spec-driven Chat**：规范驱动聊天

### **00:12:30 - MCP 服务器工作原理**
- 开发者与 AI 代理交互
- 模型具有训练时的内部知识
- MCP 服务器提供：
  - 最新的外部数据
  - 与第三方 API 的集成能力
  - 访问公司内部 API 的能力
  - 执行操作的能力（如下订单）

### **00:14:45 - MCP 服务器使用场景示例**
- **AWS 最新文档**：访问本周发布的新功能文档
- **实时股票价格**
- **天气数据**
- **任何 API 集成**
- **公司内部 API 和文档**

### **00:16:00 - 本次演示使用的 MCP 服务器**
1. AWS Serverless MCP Server：
   - SAM 集成
   - 本地测试
   - 无服务器指导

2. AWS CDK MCP Server（Sean 的个人偏好）：
   - 使用 Python 编写 CDK 代码
   - 集成 CDK Nag 进行安全检查
   - 自动集成 PowerTools 库
   - 强制安全最佳实践

3. AWS Core MCP Server：
   - 提示词理解和优化
   - 为不擅长提示工程的用户改进输入
   - 包含 MCP 服务器路由器
   - 支持角色（开发者、架构师）

4. AWS Documentation MCP Server：
   - 访问最新 AWS 服务文档
   - 最佳实践、限制、API 信息

5. MCP Server Fetch（Anthropic 提供）：
   - 访问互联网并加载网页
   - 用于获取井字棋游戏的 OpenAPI 规范

### **00:21:00 - 目标架构说明**
- 架构图由 Kiro 自动生成（使用 Diagram MCP Server）
- 前端：CloudFront + S3（已预先构建）
- 后端（本次构建内容）：API Gateway + Lambda + DynamoDB
- 强调无服务器的快速开发优势

### **00:22:30 - 提示工程详解**
Sean 展示了经过数月优化的提示词模板：

核心指令：
- "Build and deploy a working serverless backend"（构建并部署）
- 指定井字棋游戏的 URL
- 使用 fetch MCP 服务器查看网站并获取 OpenAPI 规范

部署指令：
- "Deploy to my default AWS account"（避免 AI 询问部署位置）
- "Test the API"（自动测试部署结果）

特殊要求：
- 处理 CORS 头（AI 经常遗漏的问题）
- 添加标签：project=<name> 和 autodelete=false
- autodelete=false 防止 AWS 内部清理脚本删除资源

额外指导：
- 针对已知失败点的特定指令
- 随着使用经验积累逐步添加

### **00:26:00 - 实际编码演示开始**
- 展示已部署的井字棋游戏前端
- 演示游戏功能：注册玩家、开始游戏、与 AI 对战

### **00:27:30 - Kiro CLI 配置文件详解**
- 配置文件位置：~/.kiro/agents/
- 示例文件：reinvent.json

配置文件结构：
- schema：预设值
- name：代理名称（如 "reinvent"）
- description：代理描述
- prompt：系统提示词（每次构建时的指导）
- mcpServers：MCP 服务器列表
- allowedTools：允许的工具列表
- toolSettings：工具设置（如 bash 超时 300 秒）

### **00:30:00 - 安全设置说明**
- 默认情况下，Kiro 会询问是否执行命令
- 使用 -a 标志可以自动批准所有操作
- **警告**：在敏感环境中应保持手动批准

### **00:31:30 - 添加 MCP 服务器演示**
- 访问 AWS Labs GitHub 页面
- 搜索 "serverless" 找到 AWS Serverless MCP Server
- 复制 JSON 配置
- 粘贴到配置文件的 mcpServers 部分
- 删除环境变量配置（使用默认 AWS 配置文件）

### **00:33:00 - 启动 Kiro CLI**
命令：kiro-cli chat -a --agent reinvent
- chat：聊天模式
- -a：自动批准所有操作
- --agent reinvent：使用 reinvent 代理

### **00:34:00 - MCP 服务器加载确认**
- 系统加载四个 MCP 服务器：
  1. Core MCP Server
  2. Serverless MCP Server
  3. Fetch MCP Server
  4. Documentation MCP Server

### **00:35:00 - 可用命令介绍**
- 输入 / 查看所有命令
- /agent：管理代理
- /experiment：实验性功能

### **00:36:00 - 执行构建提示词**
- 粘贴预先准备的提示词
- Kiro 开始获取网站内容
- 加载 OpenAPI 规范
- 创建待办事项列表（实验性功能）

### **00:37:00 - 实验性功能说明**
- **To-do List**：提供思维链过程，改进应用构建
- **Checkpoints**：保存进度点
- Sean 个人启用所有实验性功能

### **00:38:00 - AI 构建过程开始**
- Kiro 分析需求
- 创建项目结构
- 开始编写代码
- 使用 SAM（Serverless Application Model）
- 自动处理 CORS 配置
- 添加 DynamoDB 表定义

### **00:40:00 - 代码生成过程**
- 生成 Lambda 函数代码
- 创建 API Gateway 配置
- 添加 IAM 角色和权限
- 实现游戏逻辑（井字棋规则）

### **00:42:00 - 部署过程**
- 执行 sam build
- 执行 sam deploy
- 自动创建 CloudFormation 堆栈
- 部署到 AWS 账户

### **00:44:00 - 测试阶段**
- Kiro 自动测试 API 端点
- 验证游戏功能
- 检查 CORS 配置
- 确认所有端点正常工作

### **00:45:00 - 演示完成与交接**
- Sean 的 CLI 构建完成
- 获取 API Gateway URL
- 将 URL 配置到前端
- 准备交接给 Brian 演示 Kiro IDE

### **00:46:00 - Brian 的 Kiro IDE 演示开始**
- 展示 IDE 界面
- 说明与 CLI 的区别
- 演示如何在 IDE 中添加功能

### **00:48:00 - 会议总结与 Q&A**
- 强调无服务器 + AI 工具的开发速度优势
- 提供 GitHub 资源链接
- 回答观众问题

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


## 关键技术要点

- **Kiro 品牌演进**：Code Whisperer → Amazon Q Developer → Kiro
- **两种使用方式**：CLI（自动化）和 IDE（交互式）
- **MCP 服务器**：标准化接口，提供最新数据和操作能力
- **安全性**：CDK Nag 自动检查，CORS 配置需特别注意
- **提示工程**：需要迭代优化，针对常见失败点添加指导
- **实验性功能**：待办事项列表、检查点等增强功能