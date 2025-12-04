# AWS re:Invent 2025 数据分析创新会议总结

## 会议概述

本次会议由AWS分析产品组合负责人Skinuk Bahare和Neil Mukharji主讲,Netflix工程经理Anjali作为特邀嘉宾分享实践经验。会议聚焦数据处理领域的最新创新,涵盖AWS Glue、EMR、Athena和Redshift等核心服务。

这些数据处理服务已经获得了广泛的客户信任,每周执行超过3亿次Redshift Serverless查询、10亿次Athena查询和3亿个EMR Serverless Spark作业,处理超过100 PB的S3数据。AWS继续在价格性能方面投入创新,最新的AWS Spark性能比开源Spark快4.5倍,使用Spark 4.0时性能提升可达5.4倍。

本次会议重点介绍了四大创新主题:AI代理在数据处理中的应用、Apache Iceberg v3支持、易用性改进(包括SageMaker Notebooks和无服务器Airflow)以及企业级数据治理与安全功能。Netflix的案例研究展示了EMR在大规模生产环境中的实际应用,验证了这些创新的价值。

## 详细时间线与关键要点

[00:00 - 02:30] 会议开场与议程介绍
- 主讲人介绍:Skinuk Bahare(AWS分析产品负责人)、Neil Mukharji和Netflix工程经理Anjali
- 会议主题:数据处理创新,包括AI代理、Iceberg支持和易用性改进
- 议程预告:最新创新、Iceberg功能、Netflix实践案例分享

[02:30 - 05:00] 数据处理服务概览
- AWS数据处理服务介绍:Glue ETL(无服务器数据集成)、EMR(自2009年以来的开源数据处理)、Athena(交互式查询服务)
- 规模数据:每周3亿+次Redshift Serverless查询、10亿+次Athena查询、3亿个EMR Serverless Spark作业
- S3作为数据湖的核心:存储EB级Parquet数据,每秒2500万+次请求

[05:00 - 07:30] 价格性能优化
- AWS Spark性能比开源Spark快4.5倍
- 写入性能提升2倍,使用Spark 4.0时读取性能提升5.4倍
- 更快的执行速度意味着更好的SLA达成和更低的成本

[07:30 - 10:00] 四大创新主题
- Iceberg已成为构建数据湖的标准,支持跨引擎查询
- AI代理解决数据工程中的复杂问题
- 易用性改进
- 数据治理:细粒度访问控制和身份传播

[10:00 - 15:00] AI代理用于Spark版本升级
- 解决Spark版本升级的难题(从版本x.y升级到p.q)
- 挑战:代码升级和数据一致性验证,传统方式需要6-12个月
- AI代理工作流程:
  1. 读取项目结构并生成升级计划
  2. 自动执行计划、处理错误、修改代码(迭代过程)
  3. 进行数据质量检查(模式、列类型、数据大小匹配)
- 用户保持完全控制,可配置守护栏
- FINRA正在使用此升级代理

[15:00 - 17:30] Iceberg v3支持
- 基于Iceberg 1.10版本的最新表格式
- 支持删除向量(deletion vectors)和行级血缘(row lineage)
- 在EMR Spark runtime 7.12中可用,同样适用于Glue和Athena
- 优势:减少写入放大问题,消除小文件删除问题,提高数据湖管理效率

[17:30 - 19:00] EMR Spark 4.0发布
- 支持最新的Iceberg版本
- 比开源Spark快5.4倍
- 帮助实现SLA目标或降低管道运营成本

[19:00 - 21:00] Iceberg物化视图
- 允许在SQL中定义视图,自动加速Spark引擎查询
- 与Iceberg API兼容,可从Athena、EMR Spark或Glue查询
- 支持增量刷新,无需配置复杂的ETL管道和触发器
- 视图定义存储在Glue数据目录中

[21:00 - 25:00] SageMaker Notebooks易用性功能
- SageMaker Studio成为所有数据处理和AI/ML的统一前端UI
- 新的现代化笔记本体验,配备专用AI代理
- 支持SQL、Python和Spark,可无缝从Python扩展到Spark处理大数据集
- 后端使用Athena for Apache Spark,采用EMR 7.12运行时(比开源快4.7倍)
- 无服务器架构,秒级启动和扩展

[25:00 - 28:00] Spark Connect架构
- 新的客户端-服务器架构,分离客户端应用和远程Spark驱动程序
- 在笔记本中输入Spark代码时,看似本地运行,实际在后端大规模集群上执行
- 可以像调试Python变量一样调试Spark变量
- 统一的编写、执行和调试体验

[28:00 - 31:00] AI代理功能演示
- AI代理嵌入在笔记本界面右侧
- 理解数据目录和业务元数据
- 可生成正确方言的SQL(Spark SQL或Athena SQL)、Python代码和PySpark代码
- 可生成完整的执行计划和填充单元格的笔记本
- 演示:查询表、可视化数据、自动生成Python可视化代码

[31:00 - 34:00] 无服务器Managed Airflow
- 完全无服务器部署模式的Managed Airflow
- UI为SageMaker Unified Studio,可在单一界面中创建和管理工作流
- 增强的安全模型:每个工作流可指定独立的IAM角色
- 按使用付费

[34:00 - 36:00] 无服务器Airflow对比
- 预配置模式:固定基础设施、始终运行、有容量限制、需要管理环境
- 无服务器模式:无基础设施、按使用付费、无限容量、完全托管
- 安全性:预配置模式整个环境共享安全模型;无服务器模式工作流级别安全,每个工作流可有独立权限配置

[36:00 - 38:00] 可视化ETL的一键调度器
- 直接从SageMaker Unified Studio简化ETL流程和查询
- 可创建、修改和监控调度
- 后端集成Amazon EventBridge Scheduler

[38:00 - 39:30] 简化SageMaker Unified Studio入门
- 从现有服务(Athena控制台、S3表、Redshift控制台)一键进入
- 自动创建默认工作区,整个过程约1分钟
- 无需配置IAM Identity Center,使用现有控制台的IAM角色

[39:30 - 43:00] EMR Serverless无服务器存储
- 行业首创:完全消除Spark工作负载的本地磁盘配置
- 根据基准测试可降低高达20%的成本
- 传统问题:Spark worker本地磁盘存储shuffle数据,磁盘空间不足导致作业失败,磁盘IO受限导致性能下降,拖尾任务导致扩展效率低
- 无服务器存储:将shuffle卸载到高性能存储层,永不耗尽磁盘空间,作业不会失败或变慢,Spark可更灵活地按阶段需求扩展

[43:00 - 46:00] 数据访问控制需求
- 跨多种格式的一致数据访问控制:Iceberg、Delta Lake、Hudi、Parquet、CSV、JSON
- 粗粒度访问控制:保护S3位置和表
- 细粒度访问控制:列级、行级和单元格级安全

[46:00 - 48:00] S3位置的粗粒度访问
- 推荐使用S3 Access Grants
- 类似SQL的权限:对S3存储桶、前缀和对象的读写权限
- 工作流程:提交作业时,引擎查询S3 Access Grants获取范围限定的凭证
- EMR 6.15+和Glue 5.0+支持,适用于所有表格式

[48:00 - 50:00] 表级粗粒度访问控制
- 最常见场景:授予用户访问特定表的权限
- 无性能开销(仅元数据过滤)
- 完整的读写支持
- 工作流程:管理员在Lake Formation中授予权限,作业提交时通过Glue Catalog重定向到Lake Formation获取范围限定的凭证
- EMR 7.9+和Glue 5.0+支持,支持Iceberg、Delta和Hudi表的区域写入

[50:00 - 53:00] 细粒度访问控制
- 列级、行级和单元格级安全
- 支持审计跟踪以满足合规要求
- 工作流程:管理员在Lake Formation中设置细粒度权限,引擎启用Lake Formation,作业提交时与Lake Formation通信获取范围限定的凭证
- EMR 7.7+支持所有部署模式的读取,Glue 5.0+支持
- EMR 7.12和Glue 5.1支持写入(Iceberg、Delta、Hudi)
- 独特架构:分离系统驱动程序和用户驱动程序,确保无法通过Spark代码绕过安全控制

[53:00 - 56:00] 可信身份传播
- 企业客户需求:用户通过Active Directory、Okta等身份提供商认证,身份需传播到各服务
- 端到端用户操作追踪
- 通过IAM Identity Center实现:启用单点登录,实现端到端数据访问可追溯性,基于用户身份的细粒度权限
- 支持SageMaker Unified Studio的交互式会话和作业
- EMR 7.11+所有部署模式支持,Glue 5也支持

[56:00 - 58:00] 可信身份传播工作流程示例
- 两个用户(Charlie和L)访问不同的S3表
- 登录SageMaker Studio时通过IAM Identity Center认证,从Active Directory/Okta联合身份
- 身份和授权传递到EMR(提交作业或启动交互式会话时)
- 与Lake Formation通信授予访问权限

[58:00 - 61:00] Netflix案例:公司背景
- Anjali领导Netflix大数据分析平台团队
- 负责:S3数据仓库中的数据管理、Iceberg表维护、治理安全、访问引擎(Spark为主要工作负载)、其他引擎(Druid、Snowflake、LanceDB)、编排技术
- Netflix是娱乐公司,但几乎所有决策都是数据驱动的
- 用户界面决策(推荐内容、封面艺术)和内部决策(实例类型选择)都基于数据

[61:00 - 63:00] Netflix业务扩展
- 传统业务:流媒体视频点播
- 新业务:广告计划、直播内容(NFL圣诞节比赛)、Netflix House、播客
- 所有新业务导致数据仓库中数据量不断增加,需要更多洞察

[63:00 - 66:00] Netflix Spark历程
- 7年前开始存储和计算分离,这一决策获得成功
- 从开源Spark分叉,针对Netflix规模、性能和各种用例进行超优化和定制
- 运营多个Hadoop集群
- 规模数据:11,000个独特工作流、250,000个作业、超过EB级数据仓库、约8,500个R7节点
- 用例:数据洞察、ETL、大规模分析、推荐等

[66:00 - 69:00] Netflix面临的挑战
- 安全性:数据仓库最初默认开放,新业务(如广告)需要保护敏感数据,当前Hadoop/YARN平台难以实现所需的安全性和隔离
- 技术采用:大规模迁移(Scala、Python版本、Spark)耗时长
- 运营开销:大量非差异化的繁重工作,希望减轻团队负担
- 专用硬件支持有限:Gen AI用例需要GPU支持
- 易用性和调试:当前环境使用和调试较困难

[69:00 - 71:00] 为什么选择Amazon EMR
- 提供隔离和改进的安全性
- 频繁发布(每90天/每季度),包含新的Iceberg、Python、Scala支持
- 减少运营开销,支持自动扩展
- 支持GPU
- 与AWS服务(S3、IAM等)良好集成

[71:00 - 73:30] Netflix测试方法
- 选择EMR on EC2:接近当前运营方式,希望逐步过渡到托管服务,仍需调整配置
- 测试内容:
  1. 功能兼容性(Netflix定制化Spark功能)
  2. 性能(TPCDS基准测试和实际用户工作流)
  3. 规模(模拟生产运行、饱和度测试)
  4. 运营复杂性
  5. 成本

[73:30 - 76:00] Netflix性能测试结果
- P90性能提升:PySpark获得最大收益,其次是SQL和Scala
- 资源消耗:PySpark在P90时vCore消耗减少最多,其次是SQL和Scala
- vCPU消耗与成本直接相关,资源使用越少越好
- 注意:Netflix平台已经过超优化,能看到这些收益非常显著

[76:00 - 80:00] Netflix POC评估要点
- 面向未来:AWS在该领域持续投资,路线图强大,持续创新
- 安全性:EMR的安全性和隔离性非常好
- 成本结构:具有竞争力且透明
- 用户体验:良好,支持笔记本集成
- 运营负担:作为托管服务将减少运营负担
- 性能和规模:性能结果已分享,规模测试结果与当前平台相当或更好
- 可扩展性:通过Bootstrap操作等方式实现

[80:00 - 结束] 总结
- 会议涵盖了AWS数据处理服务的全面创新
- 从AI代理自动化到企业级安全,再到Netflix的实际验证
- 展示了AWS在数据分析领域的持续投资和创新能力