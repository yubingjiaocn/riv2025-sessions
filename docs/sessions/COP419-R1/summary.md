# AWS re:Invent 2025 - 使用 FOCUS 进行高级多云成本报告

## 会议概述

本次技术分享会由 AWS 高级技术客户经理 Justin Marks 和 AWS 成本与使用报告产品经理 Jason 共同主讲,主题聚焦于如何使用 FOCUS (FinOps Open Cost and Usage Specification) 规范实现跨云平台的成本数据标准化和分析。

会议首先指出了传统多云成本管理面临的核心挑战:每当企业采用新的云服务提供商或 SaaS 平台时,都需要重新学习如何收集、规范化、分析和可视化成本数据。这种重复性工作不仅耗时,还容易导致数据不一致。为解决这一痛点,FinOps 基金会推出了 FOCUS 开放规范,旨在为不同云服务提供商的成本数据提供统一的标准格式。

演讲者详细介绍了 AWS 如何通过 Data Exports 平台支持 FOCUS 1.0 和最新发布的 FOCUS 1.2 规范。FOCUS 1.2 新增了 14 个列,包括容量预留管理、发票 ID 对账、SaaS 提供商定价支持等功能,并开始支持小时、日和月度时间粒度。会议通过实际演示展示了如何使用 Amazon Athena 查询 FOCUS 数据,如何计算不同成本指标(如 Billed Cost、List Cost、Contracted Cost 和 Effective Cost),以及如何使用正则表达式和 JSON 提取技术处理标签数据,最终实现跨账户、跨云平台的成本分布分析。

## 详细时间轴与关键要点

### 开场与背景介绍 (00:00 - 05:30)
- **00:00** - 会议开始,演讲者通过现场调查了解听众背景:约四分之一的听众职位包含 FinOps,半数听众意外承担了成本分配工作
- **01:15** - Justin Marks 自我介绍为 AWS 高级技术客户经理,Jason 介绍为 AWS 成本与使用报告产品经理
- **01:45** - 提出多云成本管理的核心问题:每次采用新云平台都需要重新解决数据收集、规范化、分析和可视化四大挑战
- **03:30** - 介绍传统成本管理流程:从 AWS 开始,然后添加 SaaS 平台,再扩展到其他云平台,每次都需要重复相同的工作

### FOCUS 规范介绍 (05:30 - 10:45)
- **05:30** - Jason 介绍 FOCUS (FinOps Open Cost and Usage Specification) 的诞生背景:由 FinOps 基金会组织,多家企业共同制定的开放规范
- **06:15** - FOCUS 数据流程说明:从数据生成器(云服务商、SaaS 提供商、数据中心)获取数据,导入 FinOps 工具平台进行分析和可视化
- **07:30** - 现场调查 FOCUS 使用情况:约半数听众了解 FOCUS 规范,少数已创建报告,极少数实现了多云数据整合
- **08:45** - 介绍 AWS Data Exports 平台支持的四种数据类型:CUR 2.0、FOCUS、成本优化建议和碳排放数据

### FOCUS 1.0 与 1.2 版本对比 (10:45 - 14:30)
- **10:45** - FOCUS 1.0 包含 48 列:43 列来自规范本身,5 列为 AWS 自定义列
- **11:30** - FOCUS 1.2 新增功能介绍:14 个新列,包括容量预留 ID 和状态、发票 ID、定价货币列(支持 SaaS 提供商的代币和虚拟货币)
- **12:45** - FOCUS 1.2 新增账户结构分类,帮助识别使用来自管理账户还是成员账户
- **13:30** - FOCUS 1.2 开始支持小时、日和月度时间粒度(1.0 仅支持小时级)

### CUR 2.0 与 FOCUS 的关系 (14:30 - 18:00)
- **14:30** - Justin 解释 CUR 2.0 与 FOCUS 的列映射关系:部分列一对一映射(如账户信息、计费周期、服务名称、资源 ID 和标签)
- **15:45** - 说明某些列相关但不完全映射(如 Blended Cost 和 Line Item Type)
- **16:30** - 介绍 FOCUS 独有的新列:Effective Cost(相当于 Cost Explorer 的净摊销视图)和 Service Category(自动分类存储、计算等服务)
- **17:15** - 展示 AWS 提供的 5 个自定义列(以 x_ 前缀标识),包括成本类别、操作和使用类型

### 架构设计演示 (18:00 - 22:30)
- **18:00** - 展示 FinOps 账户架构:在独立的 FinOps 账户中进行分析,而非在主付款账户中运行
- **19:00** - 数据流程说明:从主付款账户的 S3 存储桶复制 FOCUS 数据到 FinOps 账户
- **19:45** - 使用 AWS Glue 进行数据爬取和目录化,使用 Amazon Athena 进行查询
- **20:30** - 多云数据集成方案:使用 AWS AppFlow 连接器、Lambda 函数或提供商直接推送数据到 S3
- **21:15** - 创建 Athena 统一视图,将所有云平台数据联合查询
- **22:00** - 可视化选项:Amazon Managed Grafana、QuickSight 或其他 BI 工具;也可使用 Redshift 替代 Athena

### Athena 实操演示 - 统一视图创建 (22:30 - 28:00)
- **22:30** - 进入 Athena 控制台,展示 focus_samples 数据库中的多个表
- **23:15** - 介绍统一视图借鉴自 Cloud Intelligence Dashboards 的 FOCUS 仪表板
- **24:00** - 解释视图结构:使用 UNION ALL 联合多个数据源,对不存在的列使用 NULL 填充
- **25:00** - 展示 AWS FOCUS 1.0 数据查询:选择所有列(除自定义列),将 tags 从 map 类型转换为 JSON 格式
- **26:15** - 展示 Azure 样本数据联合:对缺失的列(如 availability_zone)使用 NULL,进行时间戳格式转换
- **27:00** - 展示 FinOps Foundation 样本数据:使用 COALESCE 处理 NULL 值,避免计算错误

### 成本列详解与计算 (28:00 - 33:45)
- **28:00** - Jason 介绍四种标准化成本列的应用场景
- **28:45** - Billed Cost:查询发票总金额,使用 SUM(billed_cost) 即可获得与发票匹配的金额
- **29:30** - FOCUS 1.2 的 Invoice ID 列可用于按发票 ID 分组对账
- **30:15** - List Cost:表示无折扣和承诺购买的按需成本
- **30:45** - Contracted Cost:包含折扣但不包含承诺购买的成本
- **31:30** - Effective Cost:摊销成本,包含所有折扣和承诺购买的降价影响
- **32:15** - 计算节省金额:List Cost - Contracted Cost = 折扣节省;Contracted Cost - Effective Cost = 承诺购买节省
- **33:00** - 重要提示:必须添加 charge_category = 'Usage' 过滤器,避免重复计算购买记录

### 成本计算实操演示 (33:45 - 38:30)
- **33:45** - 演示查询 Billed Cost 总和
- **34:30** - 演示查询 List Cost、Contracted Cost 和 Effective Cost
- **35:15** - 修正查询错误(Contracted Cost 拼写错误)
- **36:00** - 展示查询结果:List Cost $5,130,Effective Cost $4,300,折扣节省 $537,总节省率 16%
- **37:30** - Jason 强调所有查询都向后兼容 FOCUS 1.2 数据集

### CUR 与 FOCUS 的摊销成本对比 (38:30 - 44:00)
- **38:30** - Justin 演示如何在 CUR 2.0 中计算摊销成本(相当于 FOCUS 的 Effective Cost)
- **39:15** - 从 Cost and Usage Query Library 复制 9 行 CASE 语句来计算摊销成本
- **40:30** - 展示 CUR 查询结果:该付款账户的摊销成本为 $22,835
- **41:15** - 演示计算净摊销成本(Net Amortized):使用 COALESCE 处理 NULL 值,优先使用 net_ 前缀列
- **42:30** - 对比 FOCUS 查询:仅需 SELECT effective_cost,无需复杂的 CASE 语句
- **43:15** - FOCUS 查询结果显示多个云平台账户的成本,包括 AWS 的 $22,835 和其他提供商数据

### 标签提取与跨云分析 (44:00 - 54:00)
- **44:00** - 场景设定:管理层要求追踪 foo、bar 应用在不同账户和云平台的分布情况
- **45:00** - 首先查询基础成本数据:按提供商、账户名称和有效成本分组
- **46:00** - 识别需要从标签中提取环境(environment)和应用(application)信息
- **46:45** - 查询 tags 列的不同值,发现标签键不一致:env vs environment,app vs application vs project
- **47:30** - 介绍两种提取方法:JSON_EXTRACT 和正则表达式(REGEXP_EXTRACT)
- **48:15** - 演示 JSON_EXTRACT:使用 JSON_EXTRACT(tags, '$.env') 提取环境标签
- **49:00** - 使用 COALESCE 处理多个可能的标签键:COALESCE(JSON_EXTRACT(tags, '$.env'), JSON_EXTRACT(tags, '$.environment'))
- **50:00** - 演示 REGEXP_EXTRACT:使用正则表达式模式匹配多种标签键变体,捕获更多数据
- **51:15** - 对比结果:REGEXP_EXTRACT 捕获的值比 JSON_EXTRACT 更多,且不会添加双引号
- **52:30** - 同时提取环境和应用标签,展示所有环境-应用组合
- **53:30** - 使用 WITH 语句创建临时表,准备进行成本分布分析

### 成本分布计算 (54:00 - 结束)
- **54:00** - 将成本数据与标签提取结果合并
- **54:45** - 展示查询结果:按提供商、账户、环境和应用分组的有效成本
- **55:30** - 演示完成,强调所有查询示例将在会后分享

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


总结要点:
- FOCUS 规范解决了多云成本数据标准化难题
- AWS Data Exports 支持 FOCUS 1.0 和 1.2,提供统一的成本数据格式
- 四种成本列(Billed、List、Contracted、Effective)满足不同分析需求
- 使用 Athena + Glue 可轻松实现多云数据整合与分析
- 标签提取技术(JSON_EXTRACT 和 REGEXP_EXTRACT)是实现精细化成本分配的关键