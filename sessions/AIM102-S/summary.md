# AWS 技术会议总结：使用 Amazon SageMaker AI 简化 AI 模型开发生命周期

## 会议概述

本次会议主要介绍了如何使用 Amazon SageMaker AI 来简化 AI 模型开发生命周期，以及如何监控和管理 AI 工作流程。演讲者包括 Amazon 高级产品经理 Kushbush Shvastav（负责 SageMaker Studio 产品）、高级解决方案架构师 Bruno Piston（专注于模型训练和大语言模型定制），以及来自 COO 公司的高级架构师 Manikandan Pararmasan，他分享了实际使用 SageMaker 的客户案例。

会议重点讨论了生成式 AI 的快速增长趋势。根据 IDC 预测，到 2028 年全球生成式 AI 支出将达到 220 亿美元，占整体 AI 支出的 32%，复合年增长率为 29%。Goldman Sachs 预测生成式 AI 可使全球 GDP 增长 7%（约 7 万亿美元），并在未来 10 年内将生产力提高 1.5 个百分点。目前 89% 的企业正在推进生成式 AI 项目，92% 计划在 2027 年前增加投资，78% 的组织在至少一个业务功能中使用 AI，77% 的组织选择 130 亿参数或更小的 AI 模型，显示出对定制化和成本效益的偏好。

会议详细展示了 SageMaker Studio 如何提供端到端的 ML 开发平台，包括数据准备、模型选择与微调、训练、部署以及监控等完整工作流程。通过实际演示，展示了如何使用 SageMaker HyperPod 进行分布式训练、使用 MLflow 进行实验跟踪、以及如何在同一集群上部署推理端点等功能。

## 详细时间线

### 开场介绍（开始）
- **演讲者介绍**：Kushbush Shvastav 介绍自己是 Amazon SageMaker Studio 产品的高级产品经理，在 AWS 工作超过 6 年
- **团队成员**：Bruno Piston（来自意大利米兰的高级解决方案架构师，在 AWS 工作近 5.5 年）和 Manikandan Pararmasan（COO 公司数据 ML 和 AI 高级架构师）加入介绍

### 生成式 AI 市场趋势
- **市场预测**：IDC 预测到 2028 年全球生成式 AI 支出将达到 220 亿美元，占整体 AI 支出的 32%，复合年增长率为 29%
- **经济影响**：Goldman Sachs 预测生成式 AI 可使全球 GDP 增长 7%（约 7 万亿美元），并在未来 10 年内将生产力提高 1.5 个百分点
- **采用率统计**：89% 的企业正在推进生成式 AI 项目，92% 计划在 2027 年前增加投资，78% 的组织在至少一个业务功能中使用 AI，77% 的组织选择 130 亿参数或更小的模型

### 企业面临的挑战
- **工具分散问题**：分散和断开的 ML 工具显著增加了产品上市时间，团队花费更多时间管理工具而非开发解决方案
- **团队孤立**：数据科学家、AI 开发人员和业务团队之间的隔离导致生产力和协作受阻，造成重复工作和错失机会
- **治理复杂性**：随着规模扩大，高效治理 AI 和 ML 项目变得极其复杂，安全性和合规性可能成为主要瓶颈
- **基础设施管理**：基础设施的可用性和管理对于训练和微调机器学习及大语言模型至关重要

### ML 与生成式 AI 工作流程对比
- **数据准备**：在生成式 AI 项目中，需要将数据格式化为提示模板或已识别 LLM 的结构
- **模型选择**：选择合适的基础模型进行微调
- **计算执行**：在所需的计算集群上运行工作负载
- **评估部署**：评估并部署模型

### Amazon SageMaker Studio 介绍
- **平台定位**：提供专门构建的端到端 ML 开发平台，数据科学家可以构建、部署、微调模型，并管理和监控 AI 工作流程
- **IDE 选择**：提供多种 IDE 选择，包括 R Studio、Jupyter Lab 或基于开源 VS Code 的代码编辑器
- **数据准备功能**：可使用 SageMaker Studio notebooks 进行数据准备，编写数据生成和准备脚本，或使用内置 EMR 连接运行大规模 Spark 工作流程
- **模型中心**：可从基础模型中心选择预构建的基础模型，选择微调技术（任何微调技术或强化学习技术），或引入自己的模型从头训练
- **部署管理**：提供可视化界面部署生产端点，并在单一界面下管理和监控所有端点和模型
- **实验与管道**：可使用 MLflow 运行实验并监控，可使用 SageMaker Pipelines 构建管道（拖放式或代码方式）
- **客户案例**：数万客户使用 Amazon SageMaker AI，包括 3M、Coinbase、Intuit、Dominoes 等

### 实际演示（Bruno 主讲）
- **演示架构**：展示了两个角色的工作流程 - 平台管理员准备环境（私有网络、HyperPod 集群部署），数据科学家/工程师进行开发
- **开发环境**：部署 SageMaker Studio，通过 Amazon FSX for Lustre 共享文件系统连接 Studio 和 HyperPod
- **数据准备演示**：
  - 在 Jupyter Lab 中安装必要的 Python 模块
  - 选择 Qwen 34B 模型进行工具调用和推理任务的微调
  - 定义数据准备函数，将数据集格式化为模型接受的提示样式
  - 将准备好的数据上传到 Amazon S3 和共享文件系统

- **训练演示**：
  - 定义训练参数（学习率、epoch 等）
  - 使用 HyperPod with EKS 定义 manifest 文件（实例数量、GPU 类型、Docker 镜像）
  - 从 Jupyter Lab 终端使用 kubectl 提交作业
  - 监控训练日志，显示环境安装、模型下载、数据集准备和 MLflow 连接
 
- **监控演示**：
  - 在 SageMaker Studio 中访问 MLflow tracking server
  - 查看训练指标和系统指标（GPU 利用率等）
  - 在 HyperPod 控制台查看集群信息、任务状态和资源利用率

- **部署演示**：
  - 将训练好的模型复制到 Amazon S3
  - 创建部署 manifest 文件（指定模型位置、实例类型、容器镜像）
  - 使用 kubectl 部署到 HyperPod 集群
  - 在 SageMaker Studio 端点界面查看部署状态
  - 使用 SageMaker Python SDK 调用端点进行推理测试

### 数据准备方法详解
- **交互式方法**：在 Jupyter Lab 或代码编辑器中直接开发，可选择不同实例类型
- **分布式处理**：连接 Jupyter Lab notebooks 到 EMR 服务器（自管理或 EMR Serverless），使用 Spark 框架进行分布式数据准备
- **程序化方法**：使用 Amazon SageMaker Processing 创建异步作业，支持自定义镜像或预构建容器（如 Spark），可集成到 ML 管道中

### 生成式 AI 模型训练技术
- **持续预训练（Continued Pre-training）**：
  - 用途：使模型适应特定行业（如医疗保健、金融服务）
  - 数据格式：将文本文档（PowerPoint、Word）转换为机器可读格式（txt 文件）
  - 训练任务：基于整个上下文预测下一个 token

- **监督微调（Supervised Fine-tuning）**：
  - 用途：教授模型新任务或改进现有任务能力
  - 数据格式：使用标记数据集，包含用户提示和预期助手回答的交替消息数组
  - 训练目标：指导模型针对特定用户提示生成预期答案

- **偏好对齐（Preference Alignment）**：
  - 用途：使模型更像人类，生成更符合人类偏好的答案
  - 技术：强化学习技术
  - 数据格式：提供用户提示以及好答案和坏答案的示例，帮助模型区分两者

### SageMaker AI 训练选项
- **SageMaker HyperPod**：
  - 特点：专门构建的弹性自编排基础设施，最大化资源控制
  - 编排：支持 Amazon EKS 或 Slurm
  - 功能：提供任务治理和组织的高级功能，可根据策略组织任务执行

- **SageMaker Training Jobs**：
  - 特点：完全托管的弹性基础设施，适用于大规模和成本效益训练
  - 工作流程：原型代码 → 调用 API（指定实例类型和数量）→ SageMaker 自动管理基础设施 → 作业完成后自动关闭
  - 计费：按需付费，仅为作业执行时间付费
  - 优化选项：支持灵活训练计划或 Spot 实例以预留容量

### 可观测性功能
- **HyperPod 任务治理**：在 Studio 中分析正在执行的任务，定义自定义策略以优先处理特定任务（基于团队或优先级）
- **Training Jobs 监控**：分析训练作业使用的集群指标，使用 AWS Batch 编排作业执行
- **MLflow 集成**：跟踪训练指标和系统指标

### SageMaker HyperPod Recipes
- **发布时间**：2024 年 re:Invent 发布
- **定义**：为开源模型（DeepSeek、Meta Llama、Mistral）和第一方模型（Amazon Nova）提供的预配置参数集合
- **使用方式**：无需编写代码，只需指定要使用的 recipe，SageMaker AI 负责执行
- **支持平台**：SageMaker Training Jobs 和 SageMaker HyperPod

### 模型部署选项
- **SageMaker Managed Inference**：
  - 特点：完全托管的实时端点，支持自动扩展
  - 功能：可定义自动扩展策略，根据请求高峰自动扩展或缩减

- **HyperPod 部署**：
  - 特点：最大化训练集群利用率
  - 功能：在同一 HyperPod 集群上部署模型，用于训练和推理工作负载
  - 快速部署：从 SageMaker Studio 界面通过几次点击直接部署开源模型到 HyperPod 集群

### SageMaker Studio 最新功能（Kushbu 主讲）

#### IDE 套件
- **Jupyter Lab**：基于 Web 的 IDE，用于 notebooks、代码和数据，提供灵活可扩展的界面配置 ML 工作流程
- **Code Editor**：基于开源 VS Code OSS，提供熟悉的快捷键、终端、调试器和重构工具
- **R Studio**：完全托管的 R IDE，包含控制台、语法高亮编辑器、绘图工具、历史记录、调试和工作区管理

#### 远程 IDE 连接
- **功能**：AI 开发人员可以从本地 IDE（如本地 Visual Studio Code）连接到 SageMaker Studio spaces
- **优势**：利用 SageMaker AI 的强大计算资源和数据，同时保持所有现有的安全控制和权限，无需额外配置
- **AWS Toolkit 集成**：Visual Studio Code IDE 可在左侧导航栏显示所有 SageMaker Studio spaces
- **使用方式**：启用远程访问 → 在 Visual Studio 中打开 → 直接访问 spaces

#### 可信身份传播（Trusted Identity Propagation）
- **定义**：AWS Identity Center 的功能，可在 AWS 服务的所有工作流程中传递最终用户（人类用户）的身份
- **工作流程**：用户通过 AWS Identity Center 登录 SageMaker Studio → 打开 notebooks 连接下游服务（Redshift、EMR、Lake Formation）或 ML 服务（SageMaker Training、Processing、Inference）→ 人类用户身份或企业身份在所有工作流程中传播 → 记录到 CloudTrail 日志
- **管理员功能**：审计谁访问了哪些资源，应用细粒度访问控制（S3 Access Grants、Lake Formation Access Grants、Redshift Data APIs）

#### Amazon Nova 定制
- **发布时间**：2025 年初
- **功能**：用户可以在 SageMaker Studio 上定制 Amazon Nova 模型
- **支持模型**：Nova Micro、Light 和 Pro
- **定制技术**：监督微调或强化学习技术
- **使用方式**：打开预构建 notebook，在 SageMaker Training Jobs 或 SageMaker HyperPod 上开始定制工作负载

#### HyperPod 上的 Notebooks 和 IDE
- **发布时间**：上周发布
- **功能**：在 Amazon SageMaker HyperPod 集群上运行 IDE 和 notebooks，最大化 CPU 和 GPU 投资
- **新增组件**：Amazon SageMaker Spaces add-on（可安装在 HyperPod EKS 集群上）
- **Space 定义**：自包含实体，可定义所有配置（镜像、计算资源、本地存储、持久卷等）

#### AI 开发人员优势
- **加速开发**：在 Web 浏览器上启动 Jupyter Lab 和 Code Editor IDE，或连接本地 IDE（如本地 VS Code）在 HyperPod 计算集群上运行 notebooks
- **统一环境**：在同一持久集群上运行 IDE，该集群也用于训练和推理工作负载
- **数据共享**：使用熟悉的工具（如 HyperPod CLI），通过已挂载的文件系统（FSX 或 EFS）在交互式 AI 工作负载和训练作业之间共享数据
- **性能优化**：通过镜像缓存提供更快的 IDE 启动延迟，支持空闲关闭
- **GPU 共享**：支持 MIG profiles 进行 GPU 共享，可将多个 spaces 打包到单个实例上，甚至在单个 GPU 上运行多个 spaces（分数 GPU）

#### 管理员优势
- **统一治理**：利用 SageMaker HyperPod 的任务治理在不同工作负载中高效利用 GPU 投资
- **可观测性**：查看不同工作负载的内存、CPU 和 GPU 使用情况，使用 SageMaker HyperPod 任务治理和可观测性重新确定优先级

### Spaces Add-on 演示
- **安装方式**：
  - 快速安装：使用自动默认配置
  - 自定义安装：提供自己的配置（也包含自动默认值，但可覆盖）

- **安装配置**：
  - 远程访问配置（连接到本地 IDE）
  - Web 浏览器访问配置（提供自定义 DNS 和有效证书）
  - KMS 密钥配置

- **模板功能**：
  - 默认模板：提供两个默认模板（Jupyter Lab 和 Code Editor）
  - 自定义模板：管理员可创建默认模板定义配置
  - 配置项：应用程序类型、任务治理优先级标签、镜像（SageMaker Distribution、ECR repos、自定义镜像）、存储（本地 EBS）、计算资源（GPU、CPU、内存）、生命周期配置脚本

- **访问方式**：
  - Web 浏览器：管理员提供自定义 DNS，AI 开发人员运行 HyperPod CLI 命令生成 Web UI URL
  - 本地 IDE VS Code：启用远程连接后，运行 HyperPod CLI 命令获取 URL，点击后直接在 VS Code IDE 中打开 space
  - Kubernetes 本地端口转发：在 Web 浏览器上打开 Jupyter Lab IDE

会议在演示创建和配置模板的过程中结束。