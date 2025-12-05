# AWS re:Invent 2025 DEV309 会议总结

## 会议概述

本次会议是一场代码实操演示(Code Talk),主题为使用AI编码助手构建无服务器应用程序。演讲者Gunnar Grosch(AWS开发者倡导者)和Shridar Pande(无服务器开发者体验首席产品经理)展示了如何利用Kiro CLI(原Amazon Q Developer CLI)结合MCP服务器来快速构建一个完整的图像生成应用。

整个演示采用渐进式开发方法,从零开始构建了一个包含前后端的完整应用。后端使用AWS SAM(Serverless Application Model)、Lambda函数、API Gateway、Amazon Bedrock的Titan图像生成模型和S3存储。前端使用React和Vite构建,并通过AWS Amplify托管。演示强调了AI助手如何通过理解开发者意图、自动执行命令、生成代码和处理部署来加速开发流程,同时保持最佳实践如最小权限IAM策略和安全的预签名URL访问。

会议还介绍了开发者体验的内循环(本地快速迭代)和外循环(CI/CD和生产部署)概念,以及如何使用steering files来控制AI助手的行为,使其符合项目特定的编码标准和工作流程。整个演示过程中没有手动编写任何代码,完全依靠AI助手通过自然语言提示完成开发任务。

## 详细时间线

00:00:00 - 会议开场
- Gunnar Grosch和Shridar Pande介绍自己和会议主题
- 说明这是一场代码实操会议,将展示如何使用AI编码助手构建无服务器应用

00:01:30 - 开发者体验概念介绍
- 解释内循环(Inner Loop):本地开发环境中的快速迭代,包括编写代码、本地测试和调试
- 解释外循环(Outer Loop):从本地推送代码到生产环境,包括CI/CD管道、部署和监控

00:02:45 - Kiro CLI工具介绍
- 介绍Kiro CLI(原Amazon Q Developer CLI)作为主要AI助手工具
- 说明该工具可在终端中使用,能访问大语言模型并通过MCP服务器扩展能力

00:03:30 - 应用架构说明
- 展示将要构建的图像生成应用架构
- 后端:API Gateway + Lambda函数(Node.js) + Amazon Bedrock(Titan图像生成V2模型) + S3存储
- 前端:React + Vite,通过Amplify托管
- 可观测性:CloudWatch Application Signals、X-Ray和Lambda Powertools

00:05:00 - 开始构建 - 初始项目状态
- 展示项目初始状态:空文件夹和预安装的Vite React前端框架
- 打开Kiro CLI并展示已配置但未启用的MCP服务器

00:06:15 - 首次尝试创建SAM项目(未使用MCP服务器)
- 提示AI创建新的SAM项目,包含Node.js 22、HTTP API和两个Lambda函数
- Kiro建议运行一系列CLI命令,但演示者取消以展示MCP服务器的差异

00:07:30 - 启用AWS Serverless MCP服务器
- Shridar解释AWS Serverless MCP服务器的功能:结合AI辅助编码和无服务器专业知识
- 该服务器提供部署、监控、事件源映射配置等专用工具
- 还启用了AWS文档和AWS知识MCP服务器

00:09:00 - 使用MCP服务器创建SAM项目
- 再次提示创建SAM项目,这次Kiro使用SAM init工具而非原始CLI命令
- AI自动创建项目结构、Lambda函数、运行SAM build和SAM validate
- 创建变更日志(changelog)以跟踪所有更改

00:12:00 - 首次部署
- 手动运行sam deploy --guided命令部署应用
- 命名堆栈为"image-gen-december-1st",部署到us-west-2区域

00:14:00 - 测试已部署的API
- 使用Kiro CLI获取API端点并测试两个端点
- AI自动查找CloudFormation堆栈名称并执行curl命令测试API
- 验证两个端点都返回正确的JSON响应

00:16:30 - 添加S3存储功能
- 提示AI添加S3存储桶到SAM模板
- 更新post-generate端点创建占位符对象
- 更新get-images端点列出25个最新对象并返回预签名URL
- 强调使用预签名URL而非公开存储桶以保持安全性
- AI自动更新IAM策略遵循最小权限原则

00:19:00 - 部署S3更新
- Kiro自动运行SAM build和SAM deploy工具
- 在CloudFormation控制台验证S3存储桶已创建
- 更新变更日志记录所有更改

00:21:00 - 测试S3集成
- 提示AI测试更新后的端点
- 验证post-generate创建测试文本文件
- 验证get-images返回对象ID和有效的预签名URL

00:22:30 - Steering Files介绍
- 展示全局steering file配置,用于控制AI助手行为
- 包含规则如:更新README、不创建额外markdown文件、Git提交规范、单元测试标准、代码风格等
- 创建项目特定的steering file,定义区域(us-west-2)、目录结构、Node.js版本、Lambda超时等

00:25:00 - 集成Amazon Bedrock图像生成
- 提示AI将占位符生成替换为Titan Image Generator V2
- 指定模型ID、请求格式、PNG输出
- 添加环境变量以便在测试时绕过Bedrock
- 设置更长的Lambda超时(覆盖steering file中的30秒默认值)
- 配置Bedrock和S3的最小权限IAM策略

00:27:30 - 部署Bedrock集成
- AI更新Lambda函数代码调用Bedrock Runtime
- 更新package.json添加必要依赖
- 自动运行SAM build和SAM deploy
- 执行Git提交记录更改

00:29:00 - 测试图像生成
- 提示生成"Las Vegas in winter"图像
- API成功调用Bedrock并返回预签名URL
- 在浏览器中验证生成的图像

00:30:30 - 删除测试文本文件
- 使用模糊提示"删除S3存储桶中的文本文件"
- AI正确识别存储桶和文件并执行删除操作

00:31:30 - 构建React前端
- 展示预创建的空白Vite React应用
- 提示AI创建单页应用,包含:文本输入框、调用post-generate的按钮、调用get-images并显示图像的画廊
- 添加环境文件配置API URL
- AI在单个提示下生成完整的前端代码和CSS样式

00:34:00 - 测试前端应用
- 在浏览器中打开前端应用
- 输入提示"reinvent expo hall"生成图像
- 成功显示生成的图像,验证前后端集成

00:35:30 - 讨论迭代改进
- 说明可以继续迭代改进前端外观
- 可以提供设计图或Figma模板让AI实现特定设计
- 强调使用具体上下文(如图像)可以获得更好的结果

00:36:30 - 从控制台到IDE的工作流
- Shridar介绍从AWS控制台过渡到本地IDE的挑战
- 展示Lambda控制台的"Open in VS Code"一键功能
- 演示如何通过一次点击在VS Code中打开Lambda函数,自动配置所有依赖和工具

00:38:00 - 在VS Code中使用AI助手
- 在VS Code中打开Lambda函数后,可以直接使用AI助手
- 展示如何在IDE中继续开发和修改代码
- 强调无缝的工作流程转换

00:39:00 - 总结与最佳实践
- 强调渐进式开发方法:逐步添加功能而非一次性构建所有内容
- 建议在提示中提供详细和具体的信息
- 使用steering files控制AI行为并保持一致性
- 利用变更日志跟踪AI所做的所有更改
- 整个演示过程中未手动编写任何代码,完全依靠AI助手

00:40:00 - 会议结束
- 回答观众问题
- 提供资源链接供进一步学习