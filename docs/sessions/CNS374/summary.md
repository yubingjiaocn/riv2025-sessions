# AWS re:Invent 2025 - 使用 Hono 增强 Lambda 功能

## 会议概述

本次会议由来自 AWS 日本公共部门的原型解决方案架构师 John 主讲，重点介绍了如何使用 Hono 框架在 AWS Lambda 上构建 Web 应用和 API。Hono 是一个源自日本的 TypeScript 优先的 Web 框架，为 Lambda 开发带来了类似 Express 的熟悉语法和开发体验。演讲者分享了他在日常原型开发工作中使用 React、TypeScript 和 Hono 的实践经验。

会议主要解决了开发者在 Lambda 上部署 Web 应用时遇到的常见痛点：传统的 API Gateway + 多个单一用途 Lambda 函数的架构对于习惯传统 Web 框架的团队来说较为陌生；Lambda 处理器和事件结构不符合 Web 标准的请求-响应模式；需要从头构建路由和错误处理等通用代码。Hono 通过提供运行时抽象、丰富的生态系统插件以及轻量级的包体积（约 10-12KB）来解决这些问题。

演讲者详细演示了 Hono 的核心优势，包括端到端类型安全的 RPC 调用、自动生成 OpenAPI 文档、以及如何在本地开发和 Lambda 部署之间无缝切换。整个框架设计注重开发者体验，同时保持了对 Lambda 冷启动性能的优化。

## 详细时间线

00:00 - 开场介绍
- 演讲者自我介绍：John，AWS 日本公共部门原型解决方案架构师
- 询问首次参加 re:Invent 的观众
- 介绍 Hono 框架同样来自日本

01:30 - 会议议程
- 为什么选择 Hono 用于 Lambda
- Hono 快速概览及其在 Lambda 上的运行方式
- Hono 的核心优势说明

02:00 - 问题背景
- 提出常见需求："我想在 Lambda 上部署 Web 应用或 API"
- 介绍传统方法的局限性

02:30 - 传统架构方法
- API Gateway + 多个单一用途 Lambda 函数
- 优点：隔离性好，职责清晰
- 缺点：对传统 Web 框架开发者来说不够直观，路由在边缘层，逻辑分散

03:30 - Lambda-lith 模式
- 单个 Lambda 函数处理路由和多个功能
- 通常与 Lambda Function URL 配对使用
- 提供直接的 HTTPS 端点，更简单的架构

04:30 - 现有方案的痛点
- Lambda 处理器和事件结构不符合 Web 标准
- 需要手动构建路由和错误处理等通用代码
- 生态系统支持相对有限

05:30 - Hono 解决方案介绍
- 提供类似 Express 的请求-响应语法
- TypeScript 优先的开发体验
- 展示最小化的 Hono 应用代码示例

06:30 - Hono 基础代码示例
- app.get 和 app.post 的常规 API
- c.json() 返回 JSON 响应
- c.req.json() 解析请求体

07:30 - Hono 与 Lambda 配合的三大理由
- 运行时抽象：一次编写，多处运行
- 丰富的生态系统：大量插件和中间件
- 轻量级：保持代码包体积小，减少冷启动影响

08:30 - 运行时抽象详解
- Hono 支持多种运行时：Node.js、Deno、AWS Lambda 等
- 使用 Node.js 适配器可本地开发和部署到 ECS
- 使用 Lambda 适配器部署到 Lambda
- 无需为不同环境重写代码

09:30 - Lambda 适配代码示例
- 只需两行代码即可将 Hono 应用转换为 Lambda 处理器
- 导入 @hono/aws-lambda 包中的 handle 函数
- 用它包装 Hono 应用

10:30 - 推荐的项目结构
- 三个小文件的架构
- app.ts：编写业务逻辑，导出 Hono 应用
- handler.ts：导入 Hono 应用，导出为 Lambda 处理器
- index.ts：导入 Hono 应用，作为 Node.js 服务器运行

11:30 - 本地开发工作流
- 日常工作中运行 tsx index.ts --watch
- 启动本地开发服务器
- 部署时指向 handler.ts 并打包

12:30 - Hono 生态系统插件
- 文档生成：Hono OpenAPI（从 Zod 生成 OpenAPI schema）
- 端到端类型：Hono Client（也称 Hono RPC）
- 输入验证：Hono Validator
- 认证：多种认证提供商插件
- MCP 服务器：Hono MCP 插件

13:30 - Hono OpenAPI 详解
- 使用 OpenAPIHono 替代普通 Hono
- 使用 app.openapi() 替代 app.get()
- 使用 createRoute 定义路径和 schema
- 在 /doc 端点提供 OpenAPI JSON

15:00 - OpenAPI 规范的用途
- 可用于客户端 SDK 生成器
- 生成文档站点
- 甚至可以提供给 LLM 生成前端
- Schema 始终与服务器保持同步

15:30 - Scalar Hono API Reference 插件
- 添加 app.get('/scalar') 即可
- 提供交互式 UI 查看 OpenAPI
- 可直接调用 API 测试
- 可复制多种语言的代码示例（cURL、Ruby、Node.js、PHP、Python 等）

16:30 - Hono RPC 演示
- 播放视频演示自动补全功能
- 输入 client.hello.get() 时 IDE 提供路径补全
- 这不是猜测而是基于类型契约

17:30 - Hono RPC 工作原理
- Monorepo 结构设计
- Lambda 目录包含服务器端代码
- Frontend 目录包含前端代码
- 从 app.ts 导出 AppType（路由类型）
- client.ts 导入 AppType 并传递给 hc（Hono Client 缩写）

18:30 - 类型安全的优势
- 自动补全基于 TypeScript 类型检查
- 错误的参数或请求在编译时就能捕获
- 无需等到网络调用时才发现错误

19:00 - Hono 的轻量级特性
- 最终包大小取决于代码和依赖
- Hono 基础包约 10-12KB
- 保持冷启动影响最小

19:30 - 与 Lambda Web Adapter 的对比
- 新应用开发且使用 TypeScript：推荐 Hono
- 已有其他语言或框架的应用需要迁移：推荐 Lambda Web Adapter
- 重点在于开发者体验和使用场景

20:30 - 总结要点
- 熟悉的开发体验：类似 Express 的路由和 Web 框架人机工程学
- 可移植性：可轻松迁移到容器或 EC2
- 丰富的生态系统：大量可用插件
- 轻量级：基线包约 12KB，冷启动影响小

21:00 - 结束语
- 鼓励会后尝试 Hono + Lambda
- 提醒完成会议调查
- 感谢参与