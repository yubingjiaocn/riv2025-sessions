# AWS re:Invent 2025 - 高监管环境中的安全AI代理与交付效率

## 会议概述

本次技术分享会由AWS巴西解决方案架构师Amanda Quinto主持，重点探讨了在高监管环境中如何安全高效地部署AI代理和生成式AI工作负载。会议邀请了两位重要客户代表：来自巴西最大合作金融系统之一Sicoob的IT执行官Edson Lisboa，以及荷兰赌场Holland Casino的Andries Krijtenburg。

会议围绕三个核心主题展开：首先介绍全球高监管环境的现状和AWS的应对策略，包括合规性、治理、法律隐私和风险管理四大支柱；其次深入探讨如何使用Amazon EKS运行AI工作负载，Sicoob分享了他们在严格金融监管下的实践经验；最后重点介绍Amazon Bedrock AgentCore服务，Holland Casino展示了如何构建和部署AI代理来满足监管要求。

## 详细时间线与关键要点

### 0:00-10:00 开场介绍与高监管环境概述
- Amanda Quinto介绍演讲者背景和议程安排
- 全球AI监管现状：超过1000项AI法规覆盖69个国家
- 欧盟AI法案、巴西LGPD等地区性法规要求
- 四大监管支柱：合规治理、法律隐私、控制和风险管理

### 10:00-20:00 分层监管框架与AWS生成式AI技术栈
- 分层监管方法：应用层、监管层、负责任AI层、合规标准层、技术框架层
- NIST AI框架600、OWASP LLM安全模式、AWS Well-Architected框架
- AWS生成式AI三层架构：Q系列应用、Amazon Bedrock、基础设施层
- 模型选择策略：根据用例选择合适模型，避免对单一模型过度依赖

### 20:00-30:00 Amazon EKS在AI工作负载中的应用
- 三种推理部署方式：Amazon Bedrock、SageMaker、Amazon EKS
- EKS优势：灾难恢复、可扩展性、成本可预测性、开源生态系统
- Kubernetes在AI工作负载中的成熟度提升
- 适用场景：已有Kubernetes经验的团队

### 30:00-40:00 Sicoob案例分享 - 公司背景与监管要求
- Sicoob简介：巴西最大合作金融系统之一，覆盖2500个城市
- 服务900万用户，98%交易通过数字渠道完成
- 四大不可妥协原则：安全性、可扩展性、高效成本管理、多LLM模型支持
- 使用的开源模型：Llama、Mistral、PHI 4、DeepSeek R1、Granite

### 40:00-50:00 Sicoob技术架构详解
- 基于Amazon EKS的核心架构
- 关键开源工具：Karpenter（GPU实例自动扩缩容）、KEDA（Pod扩缩容）
- LiteLLM（模型管理）、vLLM（推理优化引擎）
- 成本优化策略：按需付费、Spot实例使用
- GPU实例管理最佳实践：专用AMI、Amazon S3模型存储

### 50:00-55:00 Sicoob业务成果展示
- Sisbr Code AI：内部开发助手，服务1500名开发者
- 后台自动化：8个数字机器人，节省40万人工小时
- 投资顾问：基于用户画像的个性化投资建议
- Sisbr AI：核心银行智能助手，支持文档交互和信贷决策

### 55:00-62:00 Amazon Bedrock AgentCore与Holland Casino案例
- Bedrock合规认证：ISO 42001（首个获得此认证的云服务商）
- 数据隐私保证：客户数据不用于模型改进，区域数据隔离
- AgentCore三大高监管环境特性：会话隔离、身份管理、沙箱环境
- Holland Casino监管挑战：荷兰博彩管理局严格监管，违规将面临关闭风险
- 使用Strands Agents构建管理层自助服务代理
- 部署策略：从简单架构开始，逐步建立信心和能力