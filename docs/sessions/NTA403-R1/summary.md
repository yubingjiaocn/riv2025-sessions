# AWS re:Invent 2025 - 高级RAG架构会议总结

## 会议概述

本次会议是AWS re:Invent 2025的400级技术讲座，由AWS解决方案架构师Vivek Mittal和首席解决方案架构师Pallavi Nargun主讲。两位讲师均来自AWS的AI/ML专家组，专注于使用检索增强生成(RAG)技术构建应用程序。会议的核心目标是帮助已经熟悉RAG架构的开发者和架构师解决在生产环境中遇到的准确性问题。

会议采用代码演示为主的形式，通过Jupyter Notebook展示了如何使用Amazon Bedrock Knowledge Bases实现高级RAG技术。讲师使用了一个虚构的金融分析公司Octank的10K报告作为示例数据集，该数据集完全由LLM生成。会议重点讨论了从基础RAG到自我修正代理RAG的演进过程，展示了如何通过查询分解、查询扩展等技术显著提高RAG系统的检索质量和响应准确性。讲师强调，随着企业级应用变得越来越复杂，特别是当文档数量超过10,000个或涉及专有术语和缩写时，标准RAG往往无法满足需求，这时就需要采用高级RAG技术。

## 详细时间线与关键要点

开场介绍 (0:00-3:30)
- Vivek Mittal自我介绍：AWS解决方案架构师，在AWS工作3.5年，驻Tampa，专注于RAG应用开发
- Pallavi Nargun自我介绍：AWS首席解决方案架构师，IT行业25年经验，AWS工作7.5年，专注于SageMaker和Bedrock
- 现场调查：大部分观众熟悉RAG，部分已将RAG投入生产，许多人正在为RAG准确性问题困扰

会议议程说明 (3:30-5:00)
- 强调这是400级代码实战会议，将直接进入代码演示
- 会议内容：Amazon Bedrock Knowledge Bases概述、高级RAG技术讨论、代码演练
- 讲师表示RAG准确性提升是一门科学和艺术，愿意在会后继续解答问题

RAG准确性的重要性 (5:00-7:00)
- 企业数据被用于生成式AI应用中进行决策
- 用户概念已扩展：不仅是人类用户，还包括自主系统和AI代理
- 强调提高检索质量和响应质量的重要性

RAG架构三大组件 (7:00-9:00)
- 数据摄取(Ingestion)：重点关注非结构化数据（文档、图像、视频）
- 检索(Retrieval)：从向量存储中检索相关chunks
- 生成(Generation)：使用LLM生成最终响应
- 强调数据摄取工作流的重要性，包括分块策略和数据转换

Amazon Bedrock Knowledge Bases介绍 (9:00-12:00)
- 端到端RAG工作流的托管服务
- 简化了嵌入模型、分块策略、向量存储、LLM的选择和集成
- 支持S3作为主要数据源，也支持SharePoint、Confluence等
- 提供完整的配置化解决方案，快速构建RAG应用

标准RAG vs 高级RAG (12:00-16:00)
- 标准RAG（也称naive RAG）：适用于文档量较小、结构简单、无复杂关联的场景
- 高级RAG的应用场景：
  - 文档数量超过10,000个
  - 文档结构复杂且相互关联
  - 包含专有数据和缩写
  - 用户查询模式复杂
- 高级RAG通过增强检索和生成来提高响应质量

高级RAG的两大分支模式 (16:00-20:00)
- **条件分支(Conditional Branching)**：根据查询类型选择不同的向量存储
  - 示例：电商客服场景，产品问题查询产品向量库，退货政策查询政策向量库
- **并行分支(Parallel Branching)**：从多个向量存储获取数据并综合
  - 示例：制造业场景，设备错误代码查询需要同时获取根本原因、修复步骤、零件库存等信息

查询重构技术 (20:00-23:00)
- 查询重构是最常见的高级RAG技术
- 将复杂查询、多部分查询或子查询分解为多个简单查询
- 对所有子查询执行向量搜索，收集相关上下文
- 对结果进行排序和合并，生成最终响应
- Amazon Bedrock Knowledge Bases提供编排功能支持查询重构

代码演示环境设置 (23:00-28:00)
- 使用Jupyter Notebook进行演示
- 示例场景：虚构的金融分析公司Octank的10K报告分析
- 数据完全由LLM生成的合成数据
- 预先配置了S3存储桶和Knowledge Base（避免2-5分钟的创建时间）
- 使用DynamoDB存储术语表（公司专有缩写）

依赖库和配置 (28:00-31:00)
- 安装必要的库：boto3、opensearch、各种框架
- 使用Claude Haiku 3.5作为生成模型
- 配置AWS凭证和会话
- 验证账户和区域连接

Knowledge Base创建流程 (31:00-36:00)
- 指定Knowledge Base名称和描述
- 创建S3存储桶存放10K文档
- 使用bedrock create_knowledge_base API
- 配置参数：
  - 数据源：S3
  - 分块策略：固定大小分块
  - 嵌入模型：Titan Embedding
  - 向量存储：OpenSearch（默认）
- 支持的向量存储：OpenSearch、Aurora PostgreSQL、S3等
- 支持的分块策略：固定分块、语义分块、层次分块

数据摄取和同步 (36:00-38:00)
- 上传Octank 10K文档到S3
- 启动同步作业(sync job)进行数据摄取
- 首次运行摄取所有文档，后续运行仅摄取增量更新
- 演示中跳过执行以节省时间（已预先完成）

基础RAG测试 (38:00-42:00)
- 使用两个API：retrieve（仅检索）和retrieve_and_generate（检索+生成）
- 配置检索参数：默认返回5个结果（最多99个）
- 测试三个基础问题：
  1. HTM投资组合的公允价值是多少？✓ 成功回答
  2. Octank Financial的主要业务部门有哪些？✓ 成功回答
  3. Octank Financial有多少员工？✓ 成功回答
- 基础RAG在简单查询场景下表现良好

基础RAG的局限性 (42:00-47:00)
- 测试更复杂的问题：
  1. "什么是Octank Tower，举报人丑闻如何影响公司形象？"
     - 仅部分回答：找到举报人信息，但未找到Octank Tower信息
     - 文档中确实包含Octank Tower（总部位置），但未被检索到
  2. "提供DCM列表和区域办公室数量"
     - 完全失败：DCM是公司专有缩写，系统无法识别
- 问题根源：相关上下文未被检索到向量存储的结果中

查询分解技术 (47:00-51:00)
- 在检索配置中添加编排配置(orchestration configuration)
- 设置查询转换类型为"query decomposition"
- 无需编写额外代码，Knowledge Bases自动处理查询分解
- 重新测试Octank Tower问题：✓ 成功回答
- 系统自动将复杂问题分解为子问题并综合答案
- 但DCM问题仍然失败：查询分解无法解决专有术语识别问题

查询扩展技术 (51:00-58:00)
- 使用Strands Agent创建术语查找工具
- 定义lookup_term工具查询DynamoDB术语表
- Agent配置：
  - 模型：Claude Haiku 3.5
  - 系统提示：指示Agent使用术语查找工具
  - 工具定义：从术语表获取定义并扩展查询
- 执行流程：
  1. 识别查询中的专有术语（DCM）
  2. 调用lookup_term工具获取定义（Disclosure Committee Members）
  3. 使用扩展后的查询检索文档
- 测试DCM问题：✓ 成功识别并返回三位披露委员会成员

自我修正代理RAG架构 (58:00-1:05:00)
- 问题：无法根据用户查询自动选择合适的技术
- 解决方案：自我修正代理RAG
- 架构流程：
  1. 用户提问 → 中央代理
  2. 从数据源检索上下文
  3. **上下文相关性检查**：判断上下文是否与问题相关
  4. 根据检查结果选择策略：查询扩展、查询分解或组合
  5. 生成响应
  6. **响应相关性检查**：评估响应质量
     - 响应与查询的相关性
     - 响应的完整性
     - 事实准确性
  7. 如果不满足要求，循环回到策略选择步骤
  8. 设置最大循环次数防止无限循环

自我修正RAG的五个工具 (1:05:00-1:12:00)
1. retrieve_documents：使用Knowledge Base retrieve API仅检索上下文
   - 适用于需要使用自定义LLM的场景
2. retrieve_and_generate：基础RAG，检索并生成响应
3. decompose_and_generate：查询分解技术
   - 配置query_transformation为query_decomposition
4. query_expansion_agent：查询扩展代理
   - 使用Strands Agent
   - 工具：lookup_term从DynamoDB获取术语定义
5. evaluate_response_quality：响应质量评估代理
   - 使用Claude Sonnet 3.5（更强的推理能力）
   - 评估相关性、完整性和事实准确性

模型选择策略 (1:12:00-1:13:00)
- 基础RAG使用Claude Haiku 3.5：更轻量、更快速
- 质量检查使用Claude Sonnet 3.5：更强的推理能力、更多参数
- 根据具体用例选择合适的模型

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


注：本总结基于会议字幕转录，涵盖了从基础RAG到高级自我修正代理RAG的完整技术演进路径。