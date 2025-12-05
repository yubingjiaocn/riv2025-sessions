# AWS re:Invent 2025 技术会议总结：使用 CloudFront 和 WAF 管理机器人与人类流量

## 会议概述

本次 300 级别的技术深度会议由 AWS 边缘服务专家 Itav Arditi 和初创企业解决方案架构师 Nick McCord 主讲，重点探讨如何利用 Amazon CloudFront 和 AWS WAF 来区分和管理机器人流量与真实用户流量。

演讲者通过构建一个宠物领养平台作为实际案例，展示了如何应对恶意机器人攻击的挑战。根据 2024 年 ASPCA 报告，美国每年有 580 万只猫狗在救助站和收容所中等待领养，而该平台旨在聚合这些数据帮助宠物找到家。然而，平台很快遭遇了恶意机器人的攻击——竞争对手使用自动化工具批量抓取数据并提交虚假领养申请，严重影响了平台运营。

会议通过多个阶段的实时演示，展示了从基础的 WAF 防护到高级的边缘计算解决方案的完整演进过程。演讲者不仅分享了技术实现细节，还提供了可扫描的二维码让观众实时体验不同防护阶段的效果。整个解决方案强调了渐进式防护策略：从简单阻断到智能分流，再到利用 CloudFront Functions 实现精细化的流量控制和数据收集，最终在保护真实用户体验的同时，有效降低了恶意流量的影响并获取了攻击者的行为数据用于持续优化防护策略。

## 详细时间线与关键要点

### 开场与背景介绍 (00:00 - 05:30)

00:00 - 01:30 - 会议开场与讲师介绍
- Itav Arditi：AWS 边缘服务专家，拥有 10 年边缘服务客户经验
- Nick McCord：初创企业解决方案架构师，专注于全球化部署服务
- 会议定位为 300 级别深度技术分享

01:30 - 03:00 - 会议议程说明
- 包含代码演示和架构图讲解
- 提供实时演示展示配置变更的实际效果
- 会议录制，Q&A 环节安排在会后 15 分钟

03:00 - 05:30 - 流量类型分类
- 人类用户：产品的目标受众
- 良性机器人：搜索引擎爬虫、索引工具等对业务有益的自动化工具
- 恶意机器人：DDoS 攻击、内容窃取、IP 复制等威胁
- AI 机器人：新兴趋势，介于良性和恶性之间，需要特殊处理

### AWS 边缘服务架构基础 (05:30 - 12:00)

05:30 - 07:00 - CloudFront 基础介绍
- 全球超过 700 个接入点 (PoPs)
- 支持缓存内容和 API 加速
- 提供边缘计算能力：CloudFront Functions 和 Lambda@Edge

07:00 - 09:30 - 请求处理流程的四个阶段
- Viewer Request：请求到达 CloudFront 缓存前，先经过 WAF 规则评估
- Origin Request：缓存未命中时，CloudFront 代表用户向源站请求内容
- Origin Response：源站响应并填充 CloudFront 缓存
- Viewer Response：从缓存返回内容给用户，降低延迟和成本

09:30 - 12:00 - 日志和监控能力
- 标准访问日志：通过 CloudWatch、Kinesis Firehose 和 S3 存储
- 实时日志：使用 Kinesis Data Stream，秒级延迟
- 支持采样和行为过滤以优化成本

### WAF 防护机制详解 (12:00 - 17:00)

12:00 - 14:00 - WAF 核心组件
- Protection Pack (原 Web ACL)：规则的容器和框架
- 支持多种受保护资源：API 端点、Cognito 用户池等 HTTP 可访问服务
- 规则 (Rule)：最小单元，包含业务逻辑和操作动作

14:00 - 17:00 - 规则执行机制
- 规则按优先级顺序执行
- 终止性规则 (Block/Allow) 会停止后续规则评估
- 规则组 (Rule Group)：可跨多个 Protection Pack 复用
- AWS 托管规则组：IP 信誉列表、OWASP Top 10 核心规则集等
- 强调 WAF 需要持续评估和更新，不是"一次配置永久有效"

### 案例场景：宠物领养平台 (17:00 - 22:00)

17:00 - 19:30 - 问题背景
- 2024 年美国有 580 万只猫狗在收容所等待领养
- 平台聚合救助站数据，提供更全面的领养信息
- 演示界面：搜索功能、维护等级筛选、年龄限制、机器人切换开关

19:30 - 22:00 - 遭遇的攻击
- 大量虚假领养申请涌入
- 领养者信息呈数字递增模式，明显为自动化攻击
- 竞争对手试图窃取数据用于商业目的
- 三个核心 KPI：网站流量、申请审核时间、领养完成时间

### 第一阶段：启用基础 WAF 防护 (22:00 - 30:00)

22:00 - 24:30 - 基线架构
- S3 存储宠物图片
- CloudFront 缓存层
- Application Load Balancer + Lambda 处理领养请求
- DynamoDB 存储领养申请数据
- 初始状态：无 WAF 防护，机器人和人类流量无法区分

24:30 - 27:00 - 实施的 WAF 规则
- 速率限制 (Rate Limiting)：基于时间窗口、URI、IP、请求头等维度
- JA3/JA4 指纹识别：基于 SSL/TLS 连接特征的哈希值，捕获请求操纵行为
- Bot Control 托管规则组：分为 Common 和 Targeted 两种级别，通过标签识别爬虫、扫描器、SEO 工具

27:00 - 30:00 - 控制台演示与效果
- 在 CloudFront 分配中关联 WAF
- 将规则动作从 Count 改为 Block
- 演示结果：人类用户正常访问，机器人收到 403 错误
- 意外发现：机器人检测到被阻断后加大攻击力度，请求量反而上升
- KPI 影响：流量增加（负面）、审核时间增加、领养时间未改善

### 第二阶段：智能缓存分流策略 (30:00 - 40:00)

30:00 - 32:30 - 策略调整思路
- 从终止性动作 (Block) 改为非终止性动作 (Count)
- 添加自定义请求头标识机器人流量
- 利用缓存策略为机器人提供受限内容视图

32:30 - 35:00 - 架构变更
- WAF 检测到机器人后添加 X-Is-Bot: true 头
- 缓存策略根据该头部将机器人重定向到特定缓存内容
- 机器人只能看到有限的宠物子集，降低数据价值

35:00 - 37:30 - 控制台配置演示
- 创建自定义缓存策略，包含查询字符串和自定义头部
- AWS WAF 自动为添加的头部加上 X-Amazon-WAF- 前缀
- 在行为设置中应用机器人缓存策略
- 将 WAF 规则动作改为 Count + 自定义请求头

37:30 - 40:00 - 效果验证
- 人类用户：可以看到所有动物（仓鼠、兔子等）
- 机器人：只能看到固定的有限宠物列表
- KPI 改善：流量恢复正常、审核时间降低、大部分宠物的领养时间缩短

### 第三阶段：CloudFront Functions 高级定制 (40:00 - 55:00)

40:00 - 42:00 - 新问题识别
- 机器人虽然只看到有限内容，但会重复攻击同一批宠物
- 需要更精细的控制和数据收集能力

42:00 - 45:00 - CloudFront Functions 基础
- 轻量级边缘计算，运行在 WAF 之后、源站之前
- 使用 JavaScript 编写
- 支持变量、函数、原生方法（split、toLowerCase 等）
- 支持 Buffer、Crypto 等高级功能
- 支持异步操作（Promise、async/await）
- console.log 自动发送到 CloudWatch Logs (us-east-1)

45:00 - 48:00 - 返回值控制逻辑
- 返回 Request 对象：代理请求到源站
- 返回 Response 对象：终止请求，跳过源站
- 可用于边缘快速阻断

48:00 - 50:00 - Event 对象结构
- Context：分配元数据（请求 ID、分配 ID、事件类型）
- Viewer：客户端设备信息和 IP 地址
- Request：可修改的查询字符串、头部、Cookie
- Response：可修改的状态码、头部、Cookie、响应体

50:00 - 52:00 - 源站修改功能
- 导入 cf 辅助模块：import cf from 'cloudfront'
- updateRequestOrigin()：覆盖源站参数（URL、头部、TLS 配置）
- selectRequestOriginById()：使用预配置的源站 ID
- requestOriginGroups()：原生故障转移机制，自动重试备用源站

52:00 - 55:00 - 流量路由器架构
- 在 WAF 和源站之间插入 CloudFront Function
- WAF 添加机器人标识头部
- Function 读取头部并修改源站路由
- 对 1% 的机器人流量实施缓存破坏（Cache Busting）
- 其余 99% 机器人流量继续使用缓存

### 第三阶段实施演示 (55:00 - 65:00)

55:00 - 57:00 - 函数关联配置
- 在 CloudFront 行为设置中选择 Viewer Request 钩子
- 关联预先创建的 CloudFront Function
- 四个可用钩子：Viewer Request、Origin Request、Origin Response、Viewer Response

57:00 - 60:00 - 代码实现详解
javascript
// 提取请求和头部
const request = event.request;
const headers = request.headers;

// 检测机器人函数
function isBotDetected(headers) {
  return headers['x-amazon-waf-is-bot']?.value === 'true';
}

// 仅对机器人执行
if (isBotDetected(headers)) {
  // 1% 流量缓存破坏
  const random = Math.random() * 100;
  if (random < 1) {
    // 随机化头部值以破坏缓存
    request.headers['cache-key'] = { value: Math.random().toString() };
  }
  
  // 路由到机器人专用源站
  cf.selectRequestOriginById('bot-origin-id');
}


60:00 - 62:00 - 源站配置
- 在 CloudFront 分配的源站标签中预配置机器人源站
- 使用 Lambda Function URL 作为机器人源站
- 通过 ID 在 Function 中引用

62:00 - 65:00 - 效果演示
- 人类用户：正常搜索所有宠物
- 机器人：只看到"机器人宠物"
- 网络面板显示大部分响应来自 CloudFront 缓存
- 管理面板显示少量日志（仅 1% 流量到达源站）
- 收集的元数据：路由、IP、User-Agent、JA3 指纹

65:00 - 67:00 - CloudWatch 指标分析
- 缓存命中率略有下降（因 1% 缓存破坏）
- 引入新的 Lambda 调用指标（机器人源站）
- 仅 4 次 Lambda 调用，证明 99% 流量被缓存
- 成本影响极小，可调整百分比（如 0.5%）

### 第四阶段：图片请求追踪 (67:00 - 75:00)

67:00 - 69:00 - 进一步优化目标
- 不仅响应不同内容，还要收集图片渲染数据
- 关联 API 请求和图片请求，识别机器人行为模式

69:00 - 71:00 - 静态资源路由函数
- 在静态 PNG 路径行为上添加 CloudFront Function
- 函数逻辑极简：异步 console.log + 返回原始图片
- 机器人无感知，但后台记录所有元数据

71:00 - 73:00 - 代码实现
javascript
async function handler(event) {
  const request = event.request;
  
  // 异步记录日志
  console.log(JSON.stringify({
    uri: request.uri,
    clientIp: event.viewer.ip,
    userAgent: request.headers['user-agent']?.value,
    // 其他业务相关元数据
  }));
  
  // 返回原始请求，继续处理
  return request;
}


73:00 - 75:00 - 数据关联价值
- 记录相同的元数据（User-Agent、客户端 IP）
- 可关联搜索请求和图片请求
- 识别机器人的完整行为链路
- 为持续优化防护策略提供数据支持

### 总结与关键要点 (75:00 - 结束)

核心策略演进：
1. 基础阻断 → 反而激发更多攻击
2. 智能分流 → 降低数据价值，减少攻击动力
3. 边缘计算 → 精细控制 + 数据收集
4. 全链路追踪 → 深入理解攻击行为

技术亮点：
- WAF 与 CloudFront Functions 的协同工作
- 非终止性动作比简单阻断更有效
- 缓存策略作为流量控制工具
- 边缘计算实现低成本、高效率的定制化防护
- 通过少量流量采样获取关键情报

最佳实践：
- WAF 需要持续迭代，不是一次性配置
- 平衡安全性和成本（1% 采样策略）
- 保护真实用户体验的同时收集攻击数据
- 利用边缘计算能力实现复杂业务逻辑