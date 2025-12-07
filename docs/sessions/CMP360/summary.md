# AWS re:Invent 2025 - Graviton 5 技术分享会总结

## 会议概览

本次AWS re:Invent 2025最后一天的技术分享会深入介绍了AWS Graviton处理器系列的最新进展，重点发布了第五代Graviton 5芯片。演讲者首先回顾了AWS在定制芯片领域超过10年的创新历程，包括六代Nitro卡、五代Graviton芯片以及用于机器学习的Trainium和Inferentia系列。目前Graviton已在全球38个区域提供超过300种实例类型，服务超过90,000家客户，涵盖从小型企业到大型企业的各类工作负载。

Graviton 5代表了重大技术突破，在单代产品中实现了核心数量翻倍（从96核增至192核），采用3nm工艺制造，单核性能提升25%。该芯片采用ARM Neoverse V3核心，配备更大的分支预测器和高级预取器，L3缓存增加5.3倍至192MB，总缓存超过600MB。Graviton 5还是AWS数据中心首款支持PCIe Gen 6的CPU，提供高达500GB的IO连接能力，并支持DDR5-8800内存，内存延迟降低15%至100纳秒以下。在安全性方面，Graviton 5引入了用Rust编写的Nitro隔离引擎，采用形式化验证技术，为云计算安全树立了新标准。

性能测试显示，Graviton 5相比Graviton 4在各类工作负载中实现了显著提升：机器学习工作负载提升35%，Java Web应用（Grails）提升32%，内部单体应用提升47%，Nginx提升27%，数据库（HammerDB）提升40%。客户实测数据同样令人印象深刻，Snowflake虚拟数据仓库性能提升超过30%，Honeycomb延迟降低20-25%，SAP HANA在线事务处理查询性能提升35-60%。会议还详细介绍了迁移到Graviton的最佳实践，包括软件兼容性、容器化、CI/CD工具支持以及针对不同编程语言和工作负载的优化建议。

## 详细时间线与关键要点

00:00 - 开场介绍
- 感谢参会者坚持到大会最后一天
- 介绍会议议程：Graviton演进历程、Graviton 5深度解析、迁移最佳实践

02:30 - AWS芯片创新历程
- AWS在芯片领域拥有超过10年的创新经验
- 已推出六代Nitro卡、五代Graviton芯片、Trainium和Inferentia机器学习芯片
- 已出货数百万颗芯片

03:45 - 为什么选择Graviton
- Graviton在EC2中提供最佳性价比
- AWS在芯片和整个技术栈上进行创新
- 全球38个区域提供超过300种Graviton实例
- 超过90,000家客户使用Graviton

05:20 - Graviton发展历程
- 2018年：Graviton 1，16核，适用于横向扩展微服务
- 2019年：Graviton 2，64核，相比其他EC2实例性价比提升40%
- 2021年：Graviton 3，支持计算密集型、内存密集型工作负载
- 2023年：Graviton 4，支持大型数据库和电子设计自动化应用
- 2025年：Graviton 5发布

07:15 - Graviton 4实例类型
- 提供计算、内存和存储密集型实例
- 内存范围：384GB至3TB
- 本地存储：45TB至120TB
- 网络带宽：最高600Gbps
- EBS性能：720,000 IOPS，150Gbps带宽

09:00 - Graviton服务器架构
- AWS设计芯片、Nitro SSD、Nitro卡、固件和虚拟化程序
- 全栈优化提供可预测的性能、可靠性、安全性和能效

10:30 - 客户成功案例（Graviton 4）
- ClickHouse：某些查询性能提升76%
- Freshworks：平均响应时间改善23%
- Quora：Web服务器性能提升20%

11:45 - 碳排放降低
- Adobe：CO2排放减少41%
- JFrog：碳足迹减少60%
- Snowflake：每虚拟仓库信用的碳排放降低57%

12:30 - 机器学习应用
- Mobileye：吞吐量提升2倍，成本降低
- Sprinklr：推理和搜索工作负载延迟降低30%

13:15 - AWS内部服务采用
- Redshift Serverless：超过90%运行在Graviton上
- Amazon MSK、Aurora、RDS：超过60%运行在Graviton上
- EC2总体：过去两年超过50%的CPU容量为Graviton

14:30 - Graviton 5核心特性
- 核心数翻倍：从96核增至192核
- 采用3nm工艺
- 单核性能提升25%
- 使用ARM Neoverse V3核心

16:00 - 内存系统升级
- L3缓存增加5.3倍至192MB
- 总缓存超过600MB
- 支持DDR5-8800
- 内存延迟降低15%至100纳秒以下

18:20 - IO和架构改进
- 首款支持PCIe Gen 6的CPU
- 提供500TB IO连接能力
- 单芯片192核设计，延迟降低33%
- 保留NUMA架构，96核亲和本地缓存和内存控制器

20:00 - M9G实例发布
- 第九代实例，基于Graviton 5
- 性能比Graviton 4提升最高25%
- 最节能的CPU
- EC2中最佳性价比

21:30 - 安全性增强
- Graviton 2：首款支持DDR加密
- Graviton 4：首款支持PCIe加密，增加CPU认证
- Graviton 5：引入Nitro隔离引擎

23:45 - Nitro隔离引擎
- 位于Graviton CPU和Nitro虚拟化程序之间
- 使用Rust编写，消除内存安全问题
- 采用形式化验证技术
- 证明内存安全、机密性和完整性

27:30 - 形式化验证解释
- 通过数学逻辑证明系统行为
- 覆盖所有可能输入和可达状态
- 证明虚拟机生命周期管理的核心功能

30:00 - 芯片设计流程
- 使用极坐标图可视化工作负载特征
- 硅前设计过程面临10,000倍速度减慢
- 在实验室运行工作负载并在预硅环境中测试

32:45 - EDA工具支持
- Siemens Caliber宣布支持Graviton
- 在Graviton 5上性能额外提升30%
- Synopsys扩展工具支持：VCS、Prime Time、Fusion Compiler
- 性能提升：Fusion Compiler和Prime Time提升35%，VCS提升40%

35:20 - Graviton 5性能测试
- 机器学习（PyTorch）：性能提升35%
- Java Web应用（Grails）：每秒请求数提升32%
- 内部单体应用：性能提升47%
- Nginx：性能提升27%
- 数据库（HammerDB）：性能提升40%

38:00 - 客户测试结果
- Snowflake：虚拟数据仓库性能提升超过30%
- Honeycomb：延迟降低20-25%，或每核吞吐量提升36%
- Airbnb：性能比其他架构高25%
- SAP HANA：在线事务处理查询性能提升35-60%

40:30 - 迁移最佳实践概述
- 目标：使迁移过程简单、低风险
- 90%的应用无需代码更改即可运行
- 提供指南、工具和资源

41:45 - 操作系统支持
- 主流Linux发行版均支持：Amazon Linux 2023、Red Hat、SUSE、Ubuntu
- 社区Linux：AlmaLinux、Alpine
- 所有系统提供官方ARM64构建和定期安全更新

43:00 - 容器和无服务器支持
- Amazon ECS和EKS支持Graviton
- Docker Hub支持多架构镜像
- 可使用docker buildx构建
- Lambda和Fargate支持Graviton
- Bottlerocket容器优化Linux发行版

44:30 - CI/CD工具支持
- 托管服务：AWS CodeBuild、CircleCI、GitHub提供ARM64环境
- 混合模式：GitHub Actions、GitLab Runners支持Graviton
- Jenkins代理可部署在Graviton上

45:45 - 合作伙伴认证软件
- 涵盖可观测性、数据库、安全、分析和DevOps
- 商业软件可在Graviton上无功能差异运行

46:30 - AWS托管服务
- DocumentDB、Aurora、RDS、ElastiCache、MemoryDB支持Graviton
- ECS、EKS、Lambda、Fargate支持Graviton
- EMR支持在Graviton上运行Spark
- SageMaker支持Graviton推理工作负载

48:00 - 迁移步骤
1. 学习Graviton：查阅GitHub上的AWS Graviton技术指南
2. 清点软件栈：确认开源和商业库、代理的ARM64支持
3. 规划工作负载转换：获取/创建ARM64镜像，进行测试
4. 部署：更新基础设施即代码，使用蓝绿部署

51:00 - AWS Application Transformation
- 新推出的Graviton模块（早期访问）
- 可识别不兼容库
- 可重新编译或升级到ARM兼容版本
- 由AI代理驱动，持续学习改进

52:30 - Graviton节省仪表板
- 计算当前使用Graviton的节省
- 模拟迁移到Graviton的潜在节省

53:15 - 工作负载特定建议：Spark
- 设置shuffle分区大小小于200MB
- 基准测试和优化设置可获得高达80%性能提升
- 使用EMR默认设置
- 升级到Spark 3和Java 17可获得40%性能提升

54:30 - C/C++优化
- 为ARM64原生编译
- 使用ARM特定编译标志
- 重建原生库，避免x86特定代码
- 利用SVE向量化

55:15 - Python优化
- 使用ARM64原生Python库
- 确保数学库经过ARM优化

55:45 - 容器最佳实践
- 构建ARM64原生镜像
- 使用docker buildx构建多架构镜像
- 验证所有依赖项支持ARM64

56:30 - Java优化
- 为ARM重建原生库
- 使用最新JDK
- Graviton在高CPU利用率下性能优异，可以"运行得更热"

57:15 - 机器学习建议
- 适用场景：自动语音识别、情感分析、推荐系统、聊天机器人
- 使用ARM64原生机器学习框架
- 使用AWS深度学习容器简化部署

58:00 - 会议结束