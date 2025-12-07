# AWS re:Invent 2025 - 高级RAG架构会议总结

## 会议概述

本次会议是AWS re:Invent 2025的400级技术讲座，由AWS解决方案架构师Vivek Mittal和首席解决方案架构师Pallavi Nargund主讲。两位讲师均来自AWS的AI/ML专家组，专注于使用检索增强生成(RAG)技术构建应用程序。会议的核心目标是帮助已经熟悉RAG架构的开发者和架构师解决在生产环境中遇到的准确性问题。

会议采用代码演示为主的形式，通过Jupyter Notebook展示了如何使用Amazon Bedrock Knowledge Bases实现高级RAG技术。讲师使用了一个虚构的金融分析公司Octank的10K报告作为示例数据集，该数据集完全由LLM生成。通过这个实际案例，演示了从基础RAG到自我修正代理RAG的完整演进过程，展示了如何通过查询分解、查询扩展等技术显著提升RAG系统的检索质量和响应准确性。

会议强调了RAG准确性的重要性，特别是在企业数据应用和自主AI系统（如AI代理）查询RAG架构的场景下。讲师指出，随着文档复杂度增加、文档数量超过10,000份，以及用户查询模式变得更加复杂时，标准RAG架构往往无法满足需求，这时就需要采用高级RAG技术来增强检索和生成质量。

## 详细时间线与关键要点

00:00 - 开场介绍
- Vivek Mittal自我介绍：AWS解决方案架构师，在AWS工作3.5年，来自坦帕，专注于RAG应用构建
- Pallavi Nargund自我介绍：AWS首席解决方案架构师，IT行业25年经验，AWS工作7.5年，专注于SageMaker和Bedrock

02:30 - 观众背景调查
- 大部分观众熟悉RAG架构
- 部分观众已将RAG架构部署到生产环境
- 许多观众正在为RAG准确性问题而困扰

03:45 - 会议议程说明
- 这是400级代码演示会议，不会过多使用PowerPoint
- 将简要介绍Amazon Bedrock Knowledge Bases
- 重点讨论高级RAG技术并进行代码演练
- 会后讲师将在会场外回答问题，也可通过LinkedIn联系

05:20 - RAG架构重要性说明
- 企业数据被用于生成式AI应用决策
- 用户概念已扩展：不仅是人类用户，还包括自主系统和AI代理
- 提高检索质量和响应质量至关重要

06:15 - RAG三大组件回顾
- 数据摄取(Ingestion)
- 检索(Retrieval)
- 生成(Generation)
- 本次会议聚焦非结构化数据（文档、图像、视频或混合类型）

07:30 - Amazon Bedrock Knowledge Bases介绍
- 端到端RAG工作流的托管服务
- 支持多种数据源：S3（主要）、SharePoint、Confluence等
- 集成嵌入模型、分块策略、向量存储和LLM

09:00 - 标准RAG vs 高级RAG
- 标准RAG（也称朴素RAG）：适用于文档量较小、文档结构简单的场景
- 当文档数量超过10,000份、文档复杂度高、用户查询复杂时，需要高级RAG技术

10:45 - 高级RAG架构模式
- 条件分支(Conditional Branching)：根据查询类型选择不同的向量存储
  - 示例：客户支持场景中，产品问题查询产品向量存储，退货政策问题查询政策向量存储
- 并行分支(Parallel Branching)：从多个向量存储获取数据并综合
  - 示例：制造业场景中，错误代码查询同时获取根本原因、修复步骤和库存信息

13:20 - 查询重构技术
- 将复杂查询分解为多个子查询
- 对所有子查询执行向量存储检索
- 对检索结果进行排序和汇总
- Amazon Bedrock Knowledge Bases提供编排功能支持此技术

15:00 - 代码演示环境设置
- 使用Jupyter Notebook进行演示
- 示例场景：虚构金融分析公司Octank的10K报告分析
- 数据完全由LLM生成（合成数据）
- 预先配置了S3存储桶和Knowledge Base（避免2-5分钟的创建时间）
- 使用DynamoDB存储术语词汇表（公司专有缩写）

17:30 - 依赖库和配置
- 安装boto3、OpenSearch等必要库
- 使用Claude Haiku 3.5作为生成模型
- 配置AWS凭证和会话

19:00 - Knowledge Base创建代码说明
- 指定Knowledge Base名称和描述
- 配置S3存储桶作为数据源
- 使用bedrock create_knowledge_base API
- 选择Titan Embedding模型
- 配置固定大小分块策略
- 支持多种向量存储：OpenSearch（默认）、Aurora PostgreSQL等
- 支持多种分块策略：固定分块、语义分块、层次分块

22:15 - 数据摄取流程
- 上传Octank 10K文档到S3
- 启动同步作业进行数据摄取
- 首次运行摄取所有文档，后续运行仅摄取增量更新

24:00 - 基础RAG测试
- 测试问题1：HTM投资组合的公允价值是多少？
- 测试问题2：Octank Financial的主要业务部门有哪些？
- 测试问题3：Octank Financial有多少员工？
- 结果：所有问题都得到正确回答
- 原因：HTM在文档中有明确定义，标准RAG可以正确检索

26:30 - 复杂查询测试失败
- 测试问题1：什么是Octank Tower？举报人丑闻如何影响公司形象？
  - 结果：找到举报人信息，但未找到Octank Tower信息
  - 原因：Octank Tower信息存在于文档中，但未被检索到相关上下文
- 测试问题2：提供DCM列表和区域办公室数量
  - 结果：无法识别DCM缩写
  - 原因：DCM是公司专有缩写，文档中未明确定义

29:00 - 查询分解技术演示
- 配置编排功能：query_transformation类型设置为query_decomposition
- 无需编写额外代码，Knowledge Bases自动处理查询分解
- 重新测试Octank Tower问题
- 结果：成功识别并回答了Octank Tower和举报人丑闻两部分内容
- 但DCM问题仍无法解决（因为不是多部分问题，而是术语识别问题）

32:45 - 查询扩展技术演示
- 使用Strands Agent创建代理工具
- 定义lookup_term工具查询DynamoDB术语词汇表
- 代理系统提示：使用工具扩展查询中的术语定义
- 使用Claude Haiku 3.5作为代理模型
- 执行查询扩展流程：
  1. 识别查询中的DCM术语
  2. 调用lookup_term工具查询DynamoDB
  3. 获取定义：DCM = Disclosure Committee Members（披露委员会成员）
  4. 使用扩展后的查询检索文档
- 结果：成功返回三位披露委员会成员的信息

36:20 - 自我修正代理RAG架构介绍
- 问题：无法根据用户偏好预先确定使用哪种技术
- 解决方案：使用代理方法自动选择合适的技术
- 架构流程：
  1. 用户问题提交给中央代理
  2. 从数据源检索上下文
  3. 分析上下文相关性
  4. 根据相关性选择策略（查询扩展、查询分解或组合）
  5. 生成响应
  6. 检查响应相关性、完整性和事实准确性
  7. 如果不满足要求，循环回到策略选择步骤
  8. 达到最大阈值或获得满意答案后返回结果

38:50 - 自我修正RAG工具定义
- 工具1：retrieve_documents - 使用Knowledge Base retrieve API仅检索上下文
  - 适用场景：使用自定义LLM而非Knowledge Base提供的模型
- 工具2：retrieve_and_generate - 标准RAG，检索并生成响应
- 工具3：decompose_and_generate - 查询分解技术
- 工具4：query_expansion_agent - 使用Strands Agent实现查询扩展
  - 使用lookup_term工具查询术语词汇表
- 工具5：evaluate_response_quality - 评估响应质量
  - 使用Claude Sonnet 3.5（更强的推理模型）
  - 评估维度：相关性、事实准确性、完整性

42:00 - 模型选择策略
- 基础RAG使用Claude Haiku 3.5（更轻量、更快）
- 质量评估使用Claude Sonnet 3.5（更强推理能力、更多参数）
- 根据用例选择合适的模型

注：会议在此处字幕截断，但已涵盖核心技术内容和演示