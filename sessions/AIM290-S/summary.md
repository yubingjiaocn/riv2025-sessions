# AWS re:Invent 2025 Intel-AWS AI推理平台技术会议总结

## 会议概述

本次技术会议重点探讨了如何利用Intel CPU在AWS平台上构建快速、成本高效且具有主权性的AI推理平台。会议由Intel的Diego主持，汇集了Intel VP Caitlin Anderson、AWS公共部门企业技术总监Mickey、以及来自Deloitte、e& Enterprise和Articul8的客户代表。

会议强调了Intel与AWS长达18年的深度合作关系，特别是在AI推理工作负载方面的创新。演讲者们展示了如何通过Intel Xeon 6处理器和AWS EC2 8i实例，为企业提供相比GPU更具成本效益的AI推理解决方案，同时保持高性能和数据主权要求。

## 详细时间线与关键要点

### 0:00-5:00 会议开场与议程介绍
- Diego介绍会议主题：使用Intel CPU构建快速、成本高效的主权AI推理平台
- 介绍演讲嘉宾阵容：Intel VP Caitlin Anderson、AWS的Mickey、Deloitte的Bob Simmons、e& Enterprise的Amit Gupta、Articul8的Renato
- 会议分为四个部分：Intel-AWS合作关系、EC2 Intel实例推理分析、主权推理平台开发、AI创新案例

### 5:00-15:00 Intel-AWS合作关系深度解析
- Caitlin Anderson介绍Intel与AWS近20年的合作历程
- 强调合作涵盖硬件基础设施、软件优化和设备生态系统
- AWS运行超过400个Intel EC2实例类型
- 播放CEO Lip-Bu和AWS VP Dave Brown的合作视频
- 重点介绍第8代Intel实例，性能提升20%，推理模型性能提升40%
- 新增Instance Bandwidth Configuration (IBC)功能和Flex变体选项

### 15:00-25:00 Intel AI战略与生态系统方法
- 强调开放生态系统创新理念，投资x86生态系统
- 介绍与Adobe、SAP、Arqit等ISV合作伙伴的深度集成
- 解释为什么CPU适合AI推理工作负载：企业AI规模化刚刚开始，推理工作负载将显著增长
- 展示Xeon 6处理器的实时推理演示
- Mickey介绍AWS与Intel的多年多亿美元战略协议

### 25:00-35:00 AWS EC2 8i实例技术特性
- 介绍定制Xeon 6芯片的独特优势：20%计算性能提升，40%推理性能提升
- 详解Advanced Matrix Extension (AMX)技术，优化矩阵乘法运算
- 覆盖M、C、R系列实例家族，提供flex定价选项
- 已在美国和西班牙区域推出，计划扩展到更多AWS区域
- 举例阿联酋技术创新研究院使用该技术开发Falcon大语言模型

### 35:00-42:00 Deloitte客户案例分享
- Bob Simmons介绍在CPU上运行LLM和SLM的实践经验
- 重点解决成本效率和规模化部署挑战
- 三阶段测试结果：56%运维成本降低，压缩模型运行速度提升2倍
- 压缩后模型保持98.5%准确率（从81.7%降至80.7%）
- 展示CPU在并发用户场景下的性能表现
- 目标应用场景：安全要求高、需要本地部署、多智能体系统

### 42:00-47:00 e& Enterprise主权AI平台解决方案
- Amit Gupta介绍"SLM in a Box"解决方案
- 解决三大挑战：成本控制、基础设施管理、数据主权
- 利用Intel AI企业推理软件和8i实例构建阿联酋本土化AI服务
- 强调开源架构的成本效益和灵活性
- 平台优势：降低复杂性、快速价值实现、自动扩展、成本效益、安全设计、主权保护

### 47:00-49:00 Articul8 AI创新平台展示
- Renato介绍垂直集成AI平台，专注企业数据洞察
- 智能模型路由技术，运行时自主选择最优模型
- 领域特定模型相比通用模型准确率提升25%以上
- 支持本地部署或AWS VPC部署
- 在AWS Marketplace推出表格理解智能体
- 会议总结：推荐EC2 8i实例，强调开放可信AI方法，邀请生态合作