# AWS re:Invent 2025 - 使用AI加速故障排除：OpenSearch中的自然语言查询与语义搜索

## 会议概述

本次会议是一个300级别的技术演示，由AWS解决方案架构师Ulli（来自柏林）和Rueben Jimenez主讲，专注于CloudOps和可观测性优化。会议展示了如何利用AI技术加速故障排除过程，特别是通过Amazon OpenSearch Service实现更快的根因分析和问题缓解。

演讲者使用了一个基于OpenTelemetry演示应用的多租户SaaS架构作为案例，该架构部署在Amazon EKS上，包含10个租户（以动物名称标识）和共享服务。整个系统通过OpenTelemetry收集器将日志、指标和追踪数据发送到Amazon OpenSearch Service进行存储和分析。会议涵盖了三个主要AI用例：自然语言查询生成、语义日志搜索，以及使用模型上下文协议(MCP)的AI代理自动化故障排除。

## 详细时间线与关键要点

### 0:00-5:00 - 会议介绍与架构概述
- 介绍演讲者背景和会议目标
- 展示基于OpenTelemetry的多租户SaaS演示应用
- 说明架构包含Amazon EKS、OpenSearch Service、OpenSearch Ingestion等组件
- 强调这是一个实用的代码演示会议，所有材料将通过GitHub Gist提供

### 5:00-10:00 - 问题场景设置
- 演示应用出现故障：用户无法完成购买流程
- 使用kubectl命令检查Kubernetes集群状态
- 通过port-forward访问应用，重现504网关超时错误
- 确认问题影响所有租户的结账功能

### 10:00-20:00 - 自然语言查询演示
- Rueben展示OpenSearch Dashboards界面
- 使用AI提示查询日志："寻找可能的速率限制问题"
- AI自动生成PPL查询语句并识别关键问题
- 发现共享命名空间中的shipping-rate-limiter服务出现"Rate limit exceeded"错误
- 通过可视化确认eagle租户产生过多流量，造成"嘈杂邻居"问题

### 20:00-35:00 - 语义搜索技术深入
- Ulli解释语义搜索与传统词汇搜索的区别
- 介绍Amazon Titan Text Embeddings V2模型的使用
- 展示日志采样技术：每秒每服务仅处理10条日志以控制成本
- 配置OpenSearch Ingestion管道实现日志采样
- 通过Dev Tools建立OpenSearch与Amazon Bedrock的连接
- 创建向量嵌入管道和索引模板
- 演示语义搜索："Something is taking too long"成功找到相关日志

### 35:00-45:00 - MCP代理自动化解决方案
- Rueben介绍模型上下文协议(MCP)和Kiro CLI的使用
- 展示Python编写的MCP服务器配置
- 通过自然语言提示："查找超出速率限制的日志"
- AI代理自动识别问题并提供修复建议
- 执行自动扩容：将shipping服务从1个副本扩展到5个副本
- 验证修复效果：应用恢复正常，用户可以成功完成购买

### 45:00-46:24 - 总结与问答
- 提供GitHub Gist链接包含所有代码和文档
- 回答观众关于跨区域连接和Dev Tools的技术问题
- 强调填写会议反馈的重要性