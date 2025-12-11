# AWS re:Invent 2025 - 使用Amazon SageMaker AI简化AI模型开发生命周期

## 会议概述

本次技术分享会重点介绍了如何使用Amazon SageMaker AI来简化AI模型开发生命周期，并实现AI工作流的监控和生命周期管理。会议由AWS高级产品经理Khushboo Srivastava主持，她负责Amazon SageMaker Studio产品并在AWS工作超过6年。同时参与分享的还有来自意大利米兰的AWS高级全球专业解决方案架构师Bruno Pistone，他专注于模型训练和大语言模型定制，以及来自加拿大金融科技公司KOHO的高级架构师Manikandan Paramasivan。

会议深入探讨了生成式AI快速发展带来的商业变革，IDC预测到2028年全球生成式AI支出将达到2020亿美元，年复合增长率达29%。高盛预测生成式AI可使全球GDP增长7%或近7万亿美元。会议详细介绍了SageMaker Studio作为端到端ML开发平台的核心功能，包括多种IDE选择、数据准备、模型训练、部署和监控等完整工作流程。

## 详细时间线与关键要点

### 00:00-05:00 开场介绍与市场趋势
- 三位演讲者自我介绍，包括各自的背景和专业领域
- 生成式AI市场预测：IDC预测2028年全球支出达2020亿美元
- 高盛预测：生成式AI可推动全球GDP增长7%，提升生产力1.5个百分点
- 企业采用现状：89%企业正在推进生成式AI项目，92%计划到2027年增加投资

### 05:00-10:00 企业面临的挑战
- 分散且不连接的ML工具显著增加上市时间
- 团队成员之间的孤立影响生产力和协作效率
- AI和ML项目治理随规模扩展变得复杂
- 基础设施的可用性和管理对训练和微调至关重要
- 传统ML工作流与生成式AI工作流的相似性分析

### 10:00-15:00 Amazon SageMaker Studio介绍
- SageMaker Studio作为专门构建的端到端ML开发平台
- 提供多种IDE选择：Studio、JupyterLab、基于VS Code的Code Editor
- 支持数据准备、模型选择、训练、评估和部署的完整流程
- 内置EMR连接支持大规模Spark工作流
- 基础模型中心提供预构建模型和自定义训练选项

### 15:00-25:00 实际演示 - 数据准备与训练
- Bruno演示完整的ML项目流程
- 平台管理员角色：创建私有网络环境和HyperPod EKS集群
- 数据科学家角色：使用JupyterLab进行数据准备和模型开发
- 演示Qwen3-4B模型的工具调用能力改进
- 数据格式化为适合模型的提示样式

### 25:00-35:00 训练工作负载与监控
- 定义训练参数：学习率、epochs等
- 使用HyperPod EKS的PyTorch作业配置
- 通过kubectl部署分布式训练工作负载
- MLflow集成实现训练指标跟踪
- SageMaker Studio中的集群监控和GPU利用率分析

### 35:00-45:00 模型部署与推理
- 模型部署到Amazon S3和HyperPod集群
- 使用LMI容器进行推理端点配置
- 演示推理端点的创建和服务状态监控
- 模型推理测试：验证改进的推理能力
- 展示模型在"思考"标签中的推理过程

### 45:00-50:00 SageMaker AI功能深度解析
- 数据准备的多种方式：交互式Notebook、EMR集成、SageMaker Processing
- 生成式AI的定制技术：持续预训练、监督微调、偏好对齐
- 训练基础设施选择：HyperPod自管理集群 vs SageMaker Training Jobs
- HyperPod Recipes：为开源模型提供预配置参数集
- Amazon Nova模型定制支持

### 50:00-55:00 最新功能发布
- 远程IDE访问：本地VS Code连接到SageMaker Studio
- 可信身份传播：AWS Identity Center集成实现细粒度访问控制
- HyperPod上的IDE和Notebook：Amazon SageMaker Spaces插件
- MIG配置文件支持GPU共享和资源优化
- 统一治理和可观测性功能

### 55:00-59:30 KOHO客户案例与总结
- KOHO公司背景：加拿大金融科技公司，200万客户
- 成本优化：从年费150万美元降至2.6万美元，节省98%
- 性能提升：实时欺诈检测延迟从50毫秒降至15毫秒
- 架构展示：完整的端到端ML平台，包括Airflow MLOps管道
- 多用例扩展：从欺诈检测扩展到信贷、营销和GenAI应用