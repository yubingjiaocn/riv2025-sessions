# AWS re:Invent 2025 - AIM414: 如何使用NKI优化LLM

## 会议概述

本次技术会议由AWS Annapurna Labs团队的解决方案架构师Scott Perry和Sadaf主讲，重点介绍了如何使用Neuron Kernel Interface (NKI)优化大语言模型在AWS Trainium加速器上的性能。会议采用实时编程演示的形式，展示了从基础性能基准测试到通过NKI内核实现显著性能提升的完整过程。

演讲者首先介绍了AWS机器学习加速器的发展历程，从第一代Inferentia到最新的Trainium3（会议前一天刚发布），以及Neuron SDK的架构和工具链。随后深入讲解了NKI作为Python领域特定语言的特点，它能够直接生成Neuron ISA指令，为性能工程师提供了前所未有的底层硬件访问能力。

## 详细时间线与关键要点

### 00:00-05:00 会议开场与背景介绍
- Scott Perry和Sadaf自我介绍，来自AWS Annapurna Labs团队
- 说明这是一个代码实战会议，将进行实时编程演示
- 介绍AWS机器学习加速器的发展历程：从2019年的Inferentia1到最新的Trainium3

### 05:00-10:00 Trainium架构深度解析
- 详细介绍Neuron Core内部架构：四个专用计算引擎（张量引擎、向量引擎、标量引擎、通用计算引擎）
- 解释三层内存层次结构：片上SRAM（SBUF/PSUM）、HBM、主机内存
- 介绍屋顶线模型（Roofline Model）和算术强度概念

### 10:00-15:00 性能优化策略与NKI介绍
- 讲解如何从内存绑定转向计算绑定的优化策略
- 介绍Neuron SDK的三种用户角色：ML开发者、数据科学家、性能工程师
- 详细介绍NKI：Python基础的领域特定语言，直接生成Neuron ISA指令

### 15:00-20:00 NKI内核示例代码解析
- 展示基础的张量加法内核实现
- 解释NKI内核的典型流程：HBM到SRAM的数据移动、计算操作、结果返回
- 介绍会议技术栈：Trainium2、Qwen3-0.6B模型、Hugging Face Transformers

### 20:00-25:00 基准测试脚本演示
- 详细解释基准测试代码的实现逻辑
- 展示模型编译和缓存机制
- 运行基线性能测试：0.35 prompts/second，延迟约3秒

### 25:00-30:00 性能分析与Perfetto可视化
- 使用Neuron Profile工具生成系统级性能分析
- 在Perfetto中可视化执行时间线
- 确认模型执行延迟接近3秒，性能有待提升

### 30:00-35:00 NKI注意力机制实现
- Sadaf接手演示，展示如何集成NKI内核到现有模型
- 修改Qwen3模型的注意力实现，从eager_attention切换到nki_attention
- 详细展示QKV张量的形状重塑过程

### 35:00-40:00 NKI内核集成与性能测试
- 完成注意力模块的NKI实现集成
- 重新编译模型并运行性能测试
- 获得显著性能提升：从0.35提升到2.99 prompts/second（约8倍提升）

### 40:00-44:00 结果分析与NKI Library发布
- 对比分析性能提升：延迟从3秒降至约0.25秒
- 宣布NKI Library开源项目正式发布
- 总结NKI的价值：为客户提供前所未有的底层性能优化能力
- 会议结束，开放问答环节