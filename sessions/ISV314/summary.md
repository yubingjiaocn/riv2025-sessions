# AWS re:Invent 2025 会议总结：从代码到市场 - 在 AWS Marketplace 上构建和发布 AI Agent

## 一、会议概述

本次 AWS re:Invent 2025 分会场由 Kevin Kennedy（高级 Marketplace 解决方案架构师，负责 APJ 区域）和 Doug Baya（高级合作伙伴解决方案架构师）共同主讲，主题为"从代码到市场"（Code to Market）。会议重点演示了如何构建 AI Agent 并将其发布到 AWS Marketplace 的完整流程。

会议分为两个主要部分：首先，Doug 详细展示了如何使用 Amazon Bedrock Agent Core 从本地开发环境将 AI Agent 部署到云端运行时环境。他使用 Strans Agent 开源 SDK 构建了一个具有多工具调用能力的智能代理，并通过简单的四行代码改造将其容器化并部署到 Agent Core Runtime。其次，Kevin 介绍了 AWS Marketplace 的产品发布模式，重点讲解了两种 AI Agent 交付方式：基于容器的部署（部署到买家账户）和基于 API 的 SaaS 模式（运行在卖家账户）。

整个演示强调了 AWS 提供的无服务器、托管式基础设施如何帮助开发者专注于业务逻辑而非运维管理，以及如何通过 Marketplace 将产品推向全球数百万潜在客户。会议展示了从本地开发到生产部署再到商业化的完整路径，为 ISV（独立软件供应商）提供了清晰的上市指南。

## 二、详细时间线与关键要点

### **开场介绍 (00:00 - 02:30)**
- **00:00** - Kevin Kennedy 和 Doug Baya 自我介绍，说明会议主题为演示如何构建 AI Agent 并在 AWS Marketplace 上发布
- **01:15** - 会议议程概览：介绍 Bedrock Agent Core、本地到云端部署演示、AWS Marketplace 介绍、交付模型讲解、集成演示

### **Amazon Bedrock Agent Core 介绍 (02:30 - 08:45)**
- **02:30** - Doug 开始介绍 Agent Core，进行现场调查：多数听众听说过 Agent Core，少数已在生产环境部署
- **03:20** - Agent Core 定义：提供部署、运行和扩展 Agentic 架构的基础设施服务集合
- **04:10** - 模块化设计：包括 Runtime（核心计算部分）、Gateway（工具扩展，支持 MCP 协议和 Lambda）、Identity（安全认证）、Memory（对话一致性）
- **05:30** - 架构图讲解：Agent Core Runtime 为中心，周边包含 Browser、Gateway、Memory 等工具，可连接任意模型
- **06:45** - AWS Agentic 能力产品组合：从即用型应用（顶层）到 Agent Core 服务层（中层）再到底层 GPU/加速器访问
- **07:50** - Agent Core Runtime 特性：无服务器、微虚拟机会话隔离、支持任意编程语言和框架、自动扩展

### **Strans Agent SDK 介绍 (08:45 - 10:30)**
- **08:45** - 介绍 Strans Agent 开源 SDK：采用模型驱动方法，用少量代码构建智能代理
- **09:30** - 核心优势：Agent 能自动识别并调用合适的工具，无需显式编程逻辑（if-then 语句）

### **本地 Agent 开发演示 (10:30 - 16:20)**
- **10:30** - Doug 切换到代码演示，展示本地运行的 Agent 应用
- **11:00** - 代码结构讲解：导入 Strans Agent、定义工具（天气查询、财务建议、AWS 账单查询、计算器、文件读取器）
- **12:15** - 工具装饰器：使用 @tool 装饰器将普通 Python 函数转换为 Agent 可调用工具
- **13:00** - Agent 初始化：使用 Bedrock 模型（Anthropic Claude 3.7），传入多个工具
- **13:45** - Kevin 提问确认：Agent 在本地运行，但通过 API 调用远程 Bedrock 模型
- **14:30** - 实时测试：询问"我的 AWS 支出是多少"，Agent 自动选择正确工具并返回结果
- **15:20** - 第二次测试：询问"给我一些财务建议"，Agent 再次正确识别并调用财务建议工具

### **从本地到 Agent Core 的迁移 (16:20 - 25:40)**
- **16:20** - Doug 开始演示如何将本地 Agent 转换为 Agent Core 兼容版本
- **16:50** - 复制代码文件，创建 hosted_agent.py
- **17:20** - 第一步：导入 from bedrock_agent_core.runtime import BedrockApp
- **18:00** - 第二步：初始化应用 app = BedrockApp()
- **18:40** - 第三步：使用 @app.entry_point 装饰器标记入口函数
- **19:30** - 第四步：添加 app.run() 启动应用，移除本地 Streamlit 相关代码
- **20:15** - 强调：仅用四行代码完成从本地到云端的转换
- **20:45** - 检查 requirements.txt：包含 bedrock-agent-core-starter-toolkit（提供 CLI 和 SDK 快速部署工具）
- **21:30** - 执行 agent-core configure 命令配置部署
- **22:00** - 配置过程：自动创建 IAM 角色、ECR 仓库、检测 requirements 文件、选择认证方式（默认 IAM）
- **23:20** - 配置完成后生成 Dockerfile 和 bedrock-agent-config.json 配置文件
- **24:00** - 执行 agent-core launch 命令：自动打包 Docker、推送到 ECR、部署到 Agent Core Runtime
- **25:10** - Kevin 提问：不使用 Agent Core 的替代方案是什么？Doug 回答：可自行部署到 EC2、EKS、ECS，但需自行管理基础设施

### **Agent Core 部署测试 (25:40 - 29:30)**
- **25:40** - 确认 Agent Core 为无服务器架构，自动扩展，无需管理基础设施
- **26:20** - 部署完成，执行 agent-core invoke 命令测试
- **27:00** - 构造 JSON 请求：{"prompt": "Can you give me some financial advice?"}
- **27:40** - Kevin 确认：现在调用的是部署在 Agent Core Runtime 中的容器化 Agent
- **28:10** - 测试成功，返回财务建议结果
- **28:40** - 在 AWS 控制台查看已部署的 Agent，名称为 hosted_agent
- **29:10** - 介绍 agent-core destroy 命令可清理所有资源

### **AWS Marketplace 介绍 (29:30 - 33:00)**
- **29:30** - Kevin 接手，开始介绍 AWS Marketplace
- **30:00** - 现场调查：多数人了解 Marketplace，少数人实际发布或购买过产品
- **30:40** - Marketplace 愿景：成为客户查找、购买和部署第三方软件、专业服务和数据的最佳平台
- **31:20** - 关键数据：超过 30,000 个可交易产品、70+ 个类别、2025 年 7 月新增 AI Agent 和工具类别
- **32:00** - 超过 300 万订阅、每年数百万访问者

### **AI Agent 交付模型 (33:00 - 37:30)**
- **33:00** - 介绍不同产品类型：AMI、容器、机器学习模型（部署到买家账户）vs SaaS 产品（运行在卖家账户）
- **34:20** - 重点：容器现可部署到 Agent Core Runtime；API 基于 SaaS 的 AI Agent 和工具
- **35:10** - 两种模型都支持预付费合同和按使用付费定价
- **36:00** - Doug 提问：如何选择定价模型？Kevin 回答：首先决定部署位置（买家 vs 卖家账户），然后根据买家偏好选择合同或按需付费

### **容器产品发布演示 (37:30 - 45:00)**
- **37:30** - 讲解部署流程：创建 Marketplace 列表 → 将私有 ECR 仓库中的容器复制到 Marketplace ECR → 发布
- **38:20** - 切换到代码演示，展示 JSON 配置文件
- **39:00** - JSON 内容：Logo、类别、产品标题、长描述、亮点
- **39:50** - 关键：Dimensions（维度）：定义产品定价，示例中设置 Standard 和 Premium 两个查询级别
- **41:00** - 创建 Marketplace ECR 仓库名称，设置价格
- **41:40** - 生成并执行 AWS Marketplace Catalog API 命令
- **42:20** - 返回 Change Set ID 和 ARN，确认语法正确
- **42:50** - 在控制台查看：三个新列表请求处于审核中（约 10-15 分钟）
- **43:40** - 展示之前创建的已发布产品示例

### **Marketplace 产品详情页 (45:00 - 48:30)**
- **45:00** - 展示产品详情页：包含产品描述、定价信息、使用说明
- **46:00** - 买家订阅流程：点击"Subscribe"按钮 → 接受条款 → 配置部署选项
- **47:00** - 部署配置：选择 AWS 区域、Agent Core Runtime 版本、IAM 角色、网络设置
- **47:50** - 部署完成后，买家可在自己的账户中看到运行的 Agent

### **计量和许可集成 (48:30 - 55:00)**
- **48:30** - Kevin 介绍两种定价模型：**合同定价**（预付费，基于 AWS License Manager）和**按使用付费**（基于 AWS Marketplace Metering Service）
- **49:30** - 切换到代码演示，展示计量集成代码
- **50:00** - 导入 boto3 和 Marketplace Metering Service 客户端
- **50:40** - 在 Agent 处理函数中添加计量逻辑：根据查询类型（Standard/Premium）调用 meter_usage() API
- **51:30** - 计量参数：产品代码、时间戳、维度（Standard/Premium）、数量
- **52:20** - 演示 License Manager 集成：调用 checkout_license() 检查许可证权限
- **53:10** - 根据许可证类型（Basic/Advanced）限制功能访问
- **54:00** - 强调：计量和许可检查应在实际使用前进行，确保合规性

### **SaaS 产品模型介绍 (55:00 - 58:30)**
- **55:00** - 介绍 API 基于 SaaS 的 AI Agent 产品模型
- **55:40** - 与容器模型的区别：Agent 运行在卖家账户，买家通过 API 端点访问
- **56:30** - 适用场景：希望保留基础设施控制权、提供托管服务
- **57:20** - 同样支持合同和按使用付费定价
- **58:00** - 计量方式相同：使用 Marketplace Metering Service API

### **总结与后续步骤 (58:30 - 60:00)**
- **58:30** - Kevin 总结：演示了从本地开发到 Agent Core 部署再到 Marketplace 发布的完整流程
- **59:00** - 关键要点：四行代码迁移到 Agent Core、两种交付模型（容器 vs SaaS）、灵活的定价选项
- **59:30** - 后续步骤：访问 AWS Marketplace 文档、使用 Agent Core Starter Toolkit、联系 AWS 团队获取支持
- **59:50** - 会议结束，开放问答环节

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


备注：本总结基于会议字幕转录，涵盖了从 AI Agent 本地开发、Agent Core 部署、到 AWS Marketplace 商业化的完整技术路径。