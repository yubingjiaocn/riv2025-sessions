# AWS re:Invent 2025 DEV309 会议总结

## 会议概述

本次会议主题为"使用AI编码助手构建无服务器应用"，由AWS开发者倡导者Kuna Yosh和无服务器开发者体验首席产品经理Shridar Pande主讲。会议展示了如何利用Kiro CLI（前身为Amazon Q developer CLI）这一AI助手工具，从零开始构建一个完整的无服务器图像生成应用。

演讲者强调了开发者体验中的两个关键循环：内循环（本地开发环境中的快速迭代）和外循环（代码推送到生产环境的CI/CD流程）。通过AI助手的帮助，开发者可以显著提升这两个循环的效率。整个演示过程中，演讲者没有手写任何代码，完全通过与AI助手对话来完成应用的前后端开发、部署和测试。

会议还介绍了MCP（Model Context Protocol）服务器的概念，这是一种标准化协议，允许为AI助手添加专门的工具和能力。通过启用AWS无服务器MCP服务器，AI助手获得了关于无服务器最佳实践、部署模式和运维监控的专业知识，使其能够更智能地辅助开发工作。

## 详细时间线

00:00:00 - 会议开场
- 介绍演讲者：Kuna Yosh（AWS开发者倡导者）和Shridar Pande（无服务器开发者体验首席产品经理）
- 说明这是一个代码演示会议，将展示如何使用AI编码助手构建无服务器应用

00:02:30 - 开发者体验概念讲解
- 解释内循环（inner loop）：本地开发环境中的编码、测试、调试快速迭代
- 解释外循环（outer loop）：代码推送后的CI/CD、部署、监控等流程
- 强调两个循环的重要性和相互关系

00:04:15 - 介绍Kiro CLI工具
- Kiro CLI是前Amazon Q developer CLI的新品牌名称
- 这是一个命令行AI助手工具，可以访问大语言模型
- 支持通过MCP服务器添加额外功能
- 可以在终端或IDE中使用

00:06:00 - 应用架构介绍
- 将构建一个图像生成应用
- 后端：API Gateway + Lambda函数（Node.js）+ Bedrock（Titan图像生成模型）+ S3存储
- 前端：React + Vite，部署在Amplify Hosting
- 可观测性：CloudWatch Application Signals、X-Ray、PowerTools用于结构化日志

00:08:30 - 开始构建后端
- 展示Kiro IDE界面（演讲者的首选IDE，但强调可以使用任何IDE）
- 项目初始状态：只有空文件夹和预装的Vite React前端

00:10:00 - 首次尝试：不使用MCP服务器
- 查看已配置但未启用的MCP服务器列表
- 提示AI创建SAM项目，包含Node.js 22、HTTP API和两个Lambda函数
- AI建议运行一系列CLI命令来创建项目
- 演讲者取消执行，准备启用MCP服务器后再试

00:12:45 - 启用MCP服务器
- 启用AWS Serverless MCP服务器
- Shridar解释该服务器的功能：提供无服务器专业知识，涵盖最佳实践、部署、运维监控等
- 还启用了AWS文档MCP服务器和AWS知识MCP服务器
- 列出可用的无服务器工具，显示现在可以使用SAM init等专门工具

00:15:20 - 使用MCP工具创建项目
- 再次提示创建SAM项目，这次AI使用SAM init工具而非CLI命令
- AI自动创建项目结构、Lambda函数、运行SAM build和SAM validate
- 创建变更日志（changelog）文件以跟踪所有更改
- 强调使用变更日志帮助追踪AI所做的所有操作

00:19:00 - 部署应用
- 手动运行sam deploy --guided进行首次部署
- 配置堆栈名称、区域（US West 2）等参数
- 等待CloudFormation部署完成

00:21:30 - 测试已部署的API
- 演讲者承认从不记得curl命令的确切语法
- 提示AI从CloudFormation堆栈获取API端点并测试
- AI自动查找正确的堆栈名称、获取端点并执行测试
- 两个端点都成功返回静态JSON响应

00:24:00 - 添加S3存储功能
- 提示AI添加S3存储桶到SAM模板
- 更新post-generate函数创建占位符对象
- 更新get-images函数列出最近25个对象并返回预签名URL
- 强调使用预签名URL而非公开存储桶的安全最佳实践
- 要求配置最小权限IAM策略

00:27:15 - 部署和测试S3功能
- AI自动运行SAM build和SAM deploy工具
- 在CloudFormation控制台确认部署进度
- 验证S3存储桶已创建
- 测试API端点，确认返回预签名URL

00:30:00 - 介绍Steering Files（引导文件）
- 展示全局steering file配置
- 解释steering files用于控制AI助手的行为
- 示例规则：更新README、不创建额外markdown文件、使用特定commit消息格式、遵循JS Doc等
- 创建项目特定的steering file，设置US West 2区域、目录结构、Node.js版本、Lambda超时时间等
- 项目级steering file会覆盖全局设置

00:34:30 - 集成Bedrock图像生成
- 提示AI将占位符替换为Bedrock Titan Image Generator V2
- 提供模型ID以节省时间（否则AI会通过API查找）
- 要求使用正确的请求格式，生成PNG并存储到S3
- 添加环境变量以便在测试时绕过Bedrock
- 设置更长的Lambda超时时间（覆盖steering file中的30秒默认值）
- 强调提示词要详细具体，不要害怕写长提示

00:38:00 - 部署Bedrock集成
- AI更新Lambda函数代码以调用Bedrock
- 添加必要的IAM权限
- 更新package.json添加Bedrock Runtime依赖
- 运行SAM build和SAM deploy
- 执行git commit记录更改

00:41:00 - 测试图像生成
- 征集观众建议生成内容
- 尝试生成"Las Vegas in winter"（拉斯维加斯的冬天）
- AI调用API，成功生成图像
- 获取预签名URL并在浏览器中验证图像
- 发现仍在列出测试文本文件

00:43:30 - 清理测试文件
- 提示AI从S3存储桶删除文本文件（故意不指定具体文件或存储桶）
- AI正确识别并删除测试文件
- 验证API不再返回文本文件

00:45:00 - 构建前端应用
- 展示预创建的空白Vite React应用
- 提示AI创建单页应用，包含：文本输入框、调用post-generate的按钮、调用get-images并显示图像的画廊
- 要求创建环境文件配置API URL
- 跳过身份验证（演示目的）

00:48:00 - 测试前端应用
- AI快速生成前端代码和CSS样式
- 执行git commit
- 在浏览器中查看前端应用
- 测试生成"reinvent expo hall"图像
- 成功生成并显示图像（虽然结果更像re:Inforce会议）

00:50:30 - 讨论迭代改进
- 说明可以继续迭代改进前端外观
- 提到可以提供设计图或Figma模板让AI实现
- 强调使用具体上下文（如图像）可以获得更好的结果

00:52:00 - 演示控制台到IDE的无缝过渡
- Shridar解释从控制台过渡到本地IDE的传统困难
- 介绍"Open in VS Code"一键功能
- 在Lambda控制台创建新函数
- 点击"Open in VS Code"按钮
- VS Code自动打开，下载代码，配置所有依赖和工具
- 强调这消除了手动复制代码、配置凭证等摩擦

00:55:00 - 会议结束
- 总结演示内容：完全通过AI助手构建了完整的无服务器应用
- 强调零手写代码完成前后端开发
- 展示了MCP服务器、steering files等高级功能的价值