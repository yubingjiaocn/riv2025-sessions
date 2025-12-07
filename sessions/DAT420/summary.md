# AWS re:Invent 2025 数据库迁移会议总结

## 会议概述

本次会议由AWS数据库迁移专家Mike Rvit主讲,重点介绍了AWS在数据库架构转换和迁移领域的最新进展。Mike目前在产品团队负责Schema Conversion与AI集成工作,会议级别为400级(高级技术)。

会议主要聚焦两大重要发布:第一是Schema Conversion服务中新增的生成式AI功能,支持Sybase、SQL Server和Oracle数据库向PostgreSQL的智能转换;第二是Q2在周一发布的Transform服务,这是一个完整的全栈转换解决方案,能够将.NET应用程序和SQL Server数据库一并迁移到PostgreSQL平台。Mike强调这是一次实战演示会议,大部分时间将进行现场编码演示,只有少量幻灯片讲解。

会议采用互动形式,鼓励观众随时提问。Mike特别指出,虽然转换报告可能显示较低的自动转换率(如66%),但这并不意味着迁移困难,因为许多被标记为"困难"的代码(如动态SQL)实际上可以直接转换。他建议用户深入分析具体问题,而不是被表面数字吓退。

## 详细时间线与关键要点

00:00:00 - 会议开场与介绍
- Mike Rvit自我介绍,说明其从数据库迁移专家转到产品团队
- Vlad作为数据库技术负责人协助演示和问答
- 强调会议为400级,假设观众熟悉数据库术语

00:01:30 - 会议内容概览
- 主要内容:Sybase数据库迁移、Schema Conversion中的生成式AI、Q2 Transform服务
- 说明今年内容与去年完全不同,展示过去一年的新功能
- 会议将以现场编码为主,只有3-4张幻灯片

00:03:00 - 转换报告解读
- 展示典型的Schema Conversion报告:数据对象100%,代码对象66%
- 解释百分比的误导性:需要考虑代码总量,而非仅看百分比
- 说明9997/9996错误通常表示工具无法识别,但不一定真的困难
- 动态SQL是常见的误报原因

00:05:45 - Schema Conversion架构介绍
- 源数据库:Sybase、SQL Server、Oracle(生成式AI支持)
- 目标数据库:PostgreSQL
- 数据库可以在任何位置(EC2、本地),只要能通过JDBC连接
- 包含确定性规则引擎(15年以上历史)和新的概率性引擎(使用Bedrock)

00:07:30 - Transform服务介绍
- Q2周一发布的全栈转换解决方案
- 转换.NET应用和SQL Server数据库到PostgreSQL
- 完整流程需要1.5小时(因此无法完整演示)
- 使用Agentic AI模型

00:09:00 - 演示准备:Bob's Used Books应用
- 使用Amazon网站上免费提供的示例应用
- 简单的图书销售应用,包含订单、用户等功能
- 将SQL Server数据库移到外部以便演示

00:11:00 - Transform工作流程开始
- 创建新的迁移作业
- 选择"Windows modernization" > "SQL Server modernization"
- 系统开始检查所需权限和资源

00:13:00 - 先决条件检查
- 强调阅读文档的重要性(虽然工程师通常不喜欢读手册)
- 必须创建包含数据库凭证的AWS Secret
- Secret必须包含特定标签供Transform识别
- 需要配置GitHub仓库连接

00:15:30 - Secret配置要求
- 必须包含:用户名、密码、引擎类型、主机名、端口、数据库名
- 重要提示:当前版本建议使用IP地址而非域名(已知问题)
- 域名可能导致失败,正在调查中

00:17:00 - 连接器配置
- Transform需要创建连接器访问数据库
- 需要创建连接器访问GitHub仓库
- 连接器需要账户授权批准
- 系统在后台创建IAM角色和权限

00:19:00 - 基础设施即代码实践
- Mike强烈推荐使用CloudFormation等工具
- 所有演示环境都通过CloudFormation模板构建
- 演示后只需删除堆栈即可清理所有资源

00:20:30 - 架构展示
- 三个EC2实例:Bastion主机、SQL Server主机、应用主机
- Bastion主机用于SSH隧道访问私有网络中的数据库
- 通过SSH隧道可以使用本地工具连接RDS数据库

00:22:00 - Secret和连接器验证
- 展示Secret的标签配置(project和owner标签)
- 展示Developer Tools中的GitHub连接配置
- Transform使用这些配置连接到资源

00:24:00 - Schema Conversion项目结构
- 创建Profile定义网络和权限
- 创建两个Data Provider(源和目标)
- 创建Project连接源和目标进行分析
- 支持虚拟目标(无需实际PostgreSQL数据库即可分析)

00:26:30 - Schema Conversion界面
- 展示迁移项目界面
- 左侧显示SQL Server源数据库
- 右侧将显示PostgreSQL目标
- 系统进行复杂度分析

00:28:00 - DMS数据迁移配置
- Transform自动创建DMS端点(源和目标)
- 创建迁移任务移动数据
- 演示显示已成功迁移6个表

00:30:00 - Transform作业继续
- 系统找到数据库和GitHub仓库
- 识别main分支(SQL Server版本)
- 开始评估转换复杂度
- 可以同时处理多个数据库和应用

00:32:00 - 迁移波次(Migration Waves)
- 系统根据复杂度组织迁移波次
- 分析应用和数据库之间的依赖关系
- 自动确定迁移顺序

00:33:00 - 切换到Sybase演示
- 由于Transform评估需要20分钟,切换到Sybase演示
- 强调AWS区域选择的重要性(常见支持问题)
- 展示三个支持生成式AI的数据库对:Sybase、SQL Server、Oracle到PostgreSQL

00:35:00 - Sybase项目先决条件
- 需要创建Secret存储数据库凭证
- 需要创建IAM角色授予Schema Conversion读取Secret的权限
- 需要创建S3存储桶(这可能涉及组织内的角色划分问题)
- Transform会自动处理这些,但手动使用Schema Conversion需要预先创建

00:37:00 - Sybase项目展示
- 展示报告:数据对象100%,代码对象66%
- 使用CloudFormation自动构建整个环境
- 已预先转换表结构和迁移数据以节省演示时间

00:38:00 - 会议继续进行
- 准备登录Sybase数据库验证数据
- 演示因时间限制需要在关键步骤之间切换

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


注: 由于提供的字幕在此处中断,完整的会议内容可能还包括Sybase数据库的具体转换演示、生成式AI功能的实际应用,以及Transform服务完成后的结果展示。