# AWS re:Invent 2025 - IM414 会议总结

## 会议概述

本次会议主题为"如何使用 Neff Kernel Interface (NKI) 优化大语言模型"，由 AWS Annapurna Labs 团队的解决方案架构师 Scott Perry 和 Saddaf 主讲。会议重点介绍了 AWS 自研的机器学习加速器芯片 Trainium 和 Inferentia，以及配套的 Neuron SDK 开发工具包。演讲者通过实际代码演示，展示了如何使用 NKI（Neuron Kernel Interface）这一 Python 领域特定语言来编写底层内核，从而显著提升 LLM 模型在 Trainium 上的推理性能。

会议采用代码实操的形式，以 Qwen 3 0.6B 嵌入模型为例，演示了从基准测试、性能分析到集成优化内核的完整流程。演讲者首先运行了使用原生注意力机制的 Qwen 3 模型作为基准，然后展示如何将 NKI 实现的 Flash Attention 内核集成到模型中，并对比优化前后的性能提升。整个演示在 TRN2 实例上进行，使用单个 Neuron 核心处理 16K 序列长度的输入，为观众提供了一个实用的性能优化参考案例。

## 详细时间线

### 开场介绍 (0:00 - 2:30)
- **0:00** - Scott Perry 介绍自己是 AWS Annapurna Labs 团队的解决方案架构师，专注于 Trainium 和 Inferentia 加速器
- **0:30** - Saddaf 自我介绍，专注于 Neuron 上的机器学习性能优化
- **1:00** - 说明这是一场代码实操会议，将在终端和代码编辑器中进行现场演示

### 背景知识讲解 (2:30 - 8:00)
- **2:30** - 介绍 AWS 机器学习加速器的发展历程：2019 年推出第一代 Inferentia，随后推出 Inferentia 2 和三代 Trainium 芯片
- **3:30** - 讲解 Neuron Core 架构，包含四个专用计算引擎：张量引擎（矩阵运算）、向量引擎、标量引擎和通用计算引擎
- **4:30** - 介绍三层内存层次结构：片上 SRAM（低容量高带宽）、HBM（中等容量和带宽）、主机内存（高容量低带宽）
- **5:30** - 使用 Roofline 模型解释性能优化：目标是从内存受限区域移动到计算受限区域，提高每字节内存读取的运算次数

### NKI 介绍 (8:00 - 12:00)
- **8:00** - 介绍 Neuron SDK 的三类用户角色：ML 开发者、数据科学家和性能工程师
- **8:30** - 重点介绍 NKI（Neuron Kernel Interface）：一种基于 Python 的领域特定语言，用于为 Trainium 和 Inferentia 编写内核
- **9:00** - 说明 NKI 直接发射 Neuron ISA 指令，与 PyTorch、JAX 和 NumPy 直接集成
- **10:00** - 展示示例内核代码，演示基本的张量加法操作

### 会议目标和技术栈 (12:00 - 14:00)
- **12:00** - 明确会议目标：对 Qwen 3 LLM 进行基准测试和性能分析，集成 NKI 注意力内核，对比性能提升
- **13:00** - 介绍技术栈：AWS Trainium 2、Neuron SDK、Qwen 3 0.6B 模型、Hugging Face Transformers

### 示例内核代码讲解 (14:00 - 18:00)
- **14:00** - 详细讲解 NKI 张量加法内核的实现
- **14:30** - 说明内核函数使用 @nki.jit 装饰器，输入输出必须位于 HBM
- **15:00** - 演示典型的 NKI 内核流程：在片上 SRAM 分配空间 → DMA 复制数据 → 执行计算 → 复制结果回 HBM
- **16:30** - 展示使用 sbuf.view、nki.isa.tensor_tensor 等 API 进行内存管理和计算操作

### 基准测试脚本讲解 (18:00 - 24:00)
- **18:00** - 展示基准测试 Python 脚本的结构和实现
- **19:00** - 说明脚本加载 Qwen 3 模型到 CPU，编译为 Neuron 格式，然后运行推理测试
- **20:00** - 介绍环境变量设置，包括单核心使用和性能分析启用
- **21:30** - 讲解 torch_neuronx.trace 调用触发 Neuron 编译器优化模型图
- **22:30** - 说明模型截断为 4 层以加快演示速度

### 基准测试执行 (24:00 - 28:00)
- **24:00** - 在 TRN2 3XL 实例上执行基准测试脚本
- **24:30** - 使用 neuron-ls 命令查看实例配置
- **25:00** - 脚本加载预编译的 Neuron 模型和 CPU 输出缓存
- **26:00** - 基准测试完成，显示结果：吞吐量 0.35 prompts/秒，延迟约 3 秒
- **26:30** - 验证准确性：MSE 损失和余弦相似度显示 Neuron 输出与 CPU 完全匹配

### 性能分析 (28:00 - 32:00)
- **28:00** - 使用 neuron-profile view 生成 Perfetto 格式的性能分析文件
- **29:00** - 在 Perfetto 浏览器工具中打开性能追踪文件
- **29:30** - 展示执行时间线：NRT load（加载权重到 HBM）和多次 NRT execute 调用
- **30:30** - 分析单次执行耗时约 2.8 秒，与基准测试结果一致
- **31:00** - 确认这是优化前的基准性能

### NKI 优化实施 (32:00 - 45:00)
- **32:00** - Saddaf 接手演示，说明将展示 NKI 内核集成的便捷性和性能影响
- **33:00** - 打开 Hugging Face Transformers 的 modeling_qwen3.py 文件
- **34:00** - 定位到 eager_attention_forward 方法，这是优化目标
- **35:00** - 创建新的 nki_attention_forward 函数
- **36:00** - 展示 attention_forward.py 文件，包含多种注意力机制的 NKI 实现（SDP、滑动窗口、Flash Attention）
- **37:00** - 开始实现张量重塑：将 Q、K、V 从 BHSD 格式转换为 NKI 内核所需格式
- **38:00** - 对 Query 张量进行 permute 和 reshape 操作：BHSD → BHDS → B*HDS
- **39:00** - 对 Key 张量执行相同操作
- **40:00** - 对 Value 张量进行简化的重塑：BHSD → B*HSD（无需 permute）
- **41:00** - 调用 NKI Flash Attention 内核，传入重塑后的 Q、K、V 张量
- **42:00** - 对输出进行逆向重塑：B*HSD → BHSD → BSHD
- **43:00** - 在模型配置中添加条件判断，根据配置选择使用 NKI 或原生注意力
- **44:00** - 清理之前的性能分析文件，准备运行优化后的模型

### 会议结束
- **45:00** - 演示即将运行优化后的基准测试（字幕在此处截断）