# AWS re:Invent 2025 分会场总结：Amazon 如何在 AWS 上驱动 AI 创新

## 会议概览

本次分会场由 AWS 技术总监 Paul Roberts 主持,深入展示了 Amazon 各业务部门如何利用 AWS 服务实现大规模 AI 创新。会议聚焦三大核心业务:Amazon.com 电商平台、Zoox 自动驾驶汽车和 Prime Video 流媒体服务。这些业务都在 AWS 基础设施上运行,展示了从生成式 AI 购物助手到自动驾驶技术,再到体育直播 AI 分析的全方位创新应用。

会议的核心主题是"AI 原生开发"和"智能体(Agent)驱动的生产力革命"。Amazon.com 高级副总裁 Dave Treadwell 透露,通过部署超过 21,000 个 AI 智能体,Amazon 在 2025 年实现了超过 20 亿美元的成本节约。Zoox 联合创始人兼 CTO Jesse Levinson 展示了如何利用数万个 GPU 和 AWS 服务训练自动驾驶模型,而 Prime Video 副总裁 Eric Orm 则演示了 AI 如何革新体育直播体验,提供前所未有的实时预测和数据可视化功能。

整场会议强调了一个关键信息:Amazon 内部使用的所有 AWS 服务和技术都对外部客户开放,包括 Amazon Bedrock、SageMaker、Trainium/Inferentia 芯片、ECS 等核心服务。这不仅展示了 AWS 的技术实力,也为客户提供了可复制的创新路径。

## 详细时间线与关键要点

### 开场与 Prime Day 规模展示
[00:00 - 08:30]
- Paul Roberts 介绍会议主题,强调这是一次"幕后揭秘"的独家分享
- Amazon Prime 拥有超过 2 亿会员,去年配送了 90 亿个当日或次日达包裹
- Prime Day 期间的技术规模:
  - 40% 的 Amazon.com 流量由 Graviton 实例处理
  - ElastiCache 每日处理 1.5 千万亿次请求
  - EBS 每天传输 1 EB(百亿亿字节)数据
  - DynamoDB 响应时间低于 10 毫秒
  - CloudFront 处理超过 3 万亿次 HTTP 请求
  - AWS Outposts 向 7,000 个仓库机器人发送 5.24 亿条指令

### Amazon Rufus 生成式 AI 购物助手演示
[08:30 - 15:45]
- Rufus 是 Amazon 的生成式 AI 购物助手,基于自定义 LLM 训练
- 技术架构:
  - 使用 vLLM 在 Trainium 实例上通过 Amazon ECS 托管
  - 采用连续批处理(Continuous Batching)技术降低首字符延迟
  - 应用负载均衡器使用"最少未完成请求"算法,吞吐量提升 5 倍
  - 结合 Amazon Bedrock(Nova 和 Claude Sonnet 模型)实现智能体功能
- Prime Day 期间性能指标:
  - 扩展至超过 80,000 个 Trainium 和 Inferentia 芯片
  - 平均每分钟处理 300 万个 token
  - 响应延迟低于 1 毫秒
  - 相比传统方案成本降低 4.5 倍,能效提升 54%
- 业务影响:使用 Rufus 的客户完成购买的可能性提高 60%

### Amazon.com 电商基础架构与 AI 原生开发
[15:45 - 30:20]
- Dave Treadwell(Amazon 电商基础高级副总裁)介绍团队规模:
  - 管理数亿行代码和数十万个微服务
  - 每秒处理数亿次微服务间请求
  - 支持全球数亿日活用户
- **地址配送智能体案例**:
  - 自动识别配送地址类型(商业地址、邮政信箱、公寓或独栋住宅)
  - 爬取政府网站等数据源,结合 S3 和 DynamoDB 存储的数据
  - 成果:首次配送缺陷率降低 74.4%,节省 2,500 小时人工时间
- **AI 原生开发革命**:
  - 推出 Spec Studio 工具:将现有代码转换为规范(Spec),再由 Amazon Q Developer(Qiro)生成新代码
  - Spec Studio 月度采用率增长超过 100%,已创建超过 15,000 个规范
  - 试点团队开发速度提升 4.5 倍(部署频率增加 4.5 倍)
  - 2026 年目标:75% 的 Amazon.com 团队采用 AI 原生开发
- **智能体部署规模**:
  - 截至演讲时已部署超过 21,000 个 AI 智能体
  - 2025 年通过 AI 和智能体实现超过 20 亿美元成本节约
  - 使用的核心服务:Bedrock、Agent Core、Qiro、QuickSight

### Zoox 自动驾驶技术架构
[30:20 - 45:50]
- Jesse Levinson(Zoox 联合创始人兼 CTO)介绍车辆设计理念:
  - 从零设计的双向对称自动驾驶车辆,无方向盘和踏板
  - 360 度传感器覆盖,4 轮转向系统
  - 已在拉斯维加斯和旧金山推出公共服务,计划扩展至奥斯汀、迈阿密等城市
- **AI 技术栈三大核心**:
  - **感知(Perception)**:融合摄像头、激光雷达、毫米波雷达、热成像和麦克风数据
  - **预测(Prediction)**:概率性预测其他道路使用者的行为
  - **运动规划(Motion Planning)**:实时决策加速、变道或减速
- **仿真与训练基础设施**:
  - 使用 Amazon S3 作为 PB 级传感器数据的真实来源
  - 基于扩散模型的机器学习生成数字孪生城市环境
  - 数万个 GPU 运行大规模仿真和模型验证
  - 每次左转需要分析数百万种场景组合
- **AWS 服务应用**:
  - **SageMaker HyperPod**:用于大规模分布式训练,支持弹性故障恢复
  - **EC2 Capacity Blocks**:按需获取最新 GPU(P5/P6 实例)处理突发 ML 工作负载
  - **数万个推理优化 GPU**:执行软件版本安全验证(Clearance Runs)
  - **FSX**:支持大规模模型训练的文件系统
  - 核心服务:EKS、MSK、DynamoDB、S3、ElastiCache 支撑车队运营后端
- 技术优化:
  - 使用 SLURM 开源调度器优先处理关键工作负载
  - 数据本地化策略降低传输成本和延迟
  - 智能 GPU 采购平衡成本与性能

### Prime Video 体育直播 AI 创新
[45:50 - 58:30]
- Eric Orm(Prime Video 体育直播与工程副总裁)介绍服务规模:
  - 全球数百万并发流媒体传输
  - 多区域高可用架构确保"功能零"(可用性是最重要的功能)
- **Thursday Night Football(周四橄榄球之夜)Prime Insights 功能**:
  - **Defensive Alerts**:开球前预测谁会突袭四分卫
  - **Pressure Alerts**:开球后预测谁会干扰四分卫
  - **Coverage ID**:预测防守是人盯人还是区域防守
  - **Pocket Health**:显示四分卫受到的压力和决策能力
  - **End of Game Sweep**:根据剩余时间和预测回合数计算获胜路径
- **技术架构**:
  - 现场使用 ECS Anywhere 在转播车内部署容器化模型,实现超低延迟
  - AWS Systems Manager 管理边缘设备
  - 实时处理数百个追踪传感器数据、比赛数据和视频帧
  - 标注数千场历史比赛生成数百万数据点训练模型
- **NASCAR Burn Bar(燃油条)创新**:
  - 实时预测和可视化所有赛车的燃油消耗(赛车本身没有油表)
  - 摄取车辆遥测、位置、油门、转速等数据,每秒数千个数据点
  - 架构:ECS/Fargate 持续客户端 → Kinesis 流式传输 → Flink 处理 → DynamoDB 和 API 输出
  - **开发周期仅 3 个月**
- **NBA 直播创新**:
  - **Event Detection Classification(EDC)系统**:自动标记和分类每个比赛时刻
  - 使用 Amazon SageMaker 和 Amazon Bedrock(Claude 模型)
  - 功能:Rapid Recap(2 分钟精彩回放)、Key Moments(实时关键时刻浏览)
  - 已标记数亿个时刻,支持全球个性化观看体验
  - 13,000 平方英尺双层演播室,配备 2,300 块 LED 屏幕(30 亿像素)
  - AWS 实时传输球员追踪数据、统计和预测到演播室

### 总结与展望
[58:30 - 60:00]
- Paul Roberts 总结:Amazon 在 AWS 上的创新涵盖 Alexa、设备业务、仓储机器人、Amazon Kuiper 卫星互联网等更多领域
- 强调所有 Amazon 内部使用的 AWS 服务都对客户开放
- 邀请与会者参观 Caesars Forum 的"One Amazon Lane"展区,体验 Zoox 自动驾驶车辆
- 重申 Andy Jassy 在主题演讲中的理念:"这仍然是第一天(Day One)"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


核心技术服务清单:
Amazon Bedrock、Amazon Q Developer(Qiro)、SageMaker HyperPod、Trainium/Inferentia、ECS/ECS Anywhere、S3、DynamoDB、ElastiCache、EKS、Kinesis、Flink、EC2 Capacity Blocks、FSX、CloudFront、Graviton、AWS Outposts、Systems Manager