# AWS re:Invent 2025 - GitHub Copilot 与 AI 驱动的软件开发生命周期

## 会议概述

本次会议由 GitHub Copilot 现场服务总监 Colin Dimbowski 主讲,这是他首次参加 AWS re:Invent 大会。Colin 拥有丰富的 Microsoft 技术栈背景,在加入 GitHub 四年多来一直专注于 GitHub Copilot 的推广和客户服务工作。

会议通过回顾计算机编程历史的演进过程,从打孔卡、终端打字机、Turbo Pascal 编译器,到现代 IDE 和 DevOps 工具,展示了开发效率的持续提升。Colin 强调,GitHub 在 2022 年 2 月推出 Copilot 技术预览版时,就已经领先于行业,比 ChatGPT 的爆发早了近一年。当前,AI 代理(Agents)正在成为软件开发的核心,GitHub 正在构建一个完整的"代理式软件开发生命周期"(Agentic SDLC),让开发者能够利用 AI 代理处理从规划、编码、审查到部署的全流程工作。

会议展示了 GitHub 内部使用数据:启用 Copilot Coding Agent 后,开发者的贡献量显著提升,其中 Copilot Coding Agent 在 GitHub 内部代码库的月度贡献量达到 1500 次,是人类最高贡献者的 5 倍。Code Review Agent 则将 PR 合并时间缩短了 20%。GitHub 的愿景是成为整个软件开发生命周期的骨干平台,不仅加速代码生成,还要在规划、安全扫描、代码审查和运维等各个环节引入 AI 能力,最终实现多线程、异步、多人协作的开发模式。

## 详细时间线与关键要点

### 开场与背景介绍
时间戳: 开始
- Colin Dimbowski 自我介绍,来自南非,现居休斯顿,担任 GitHub Copilot 现场服务总监
- 这是他首次参加 AWS re:Invent,之前主要参加 Microsoft 相关会议
- 在 GitHub 工作超过四年,之前担任解决方案工程师

### 计算机编程历史回顾
时间戳: 约 2-8 分钟
- **打孔卡时代(40-50年前)**: 通过在卡片上打孔(0和1)来编程,从想法到部署需要数月时间
- **终端打字机时代**: Ken Thompson 和 Dennis Richie 发明了 B 语言、C 语言和 Unix,使用打字机和点阵打印机,开发周期仍需数月或数周
- **1990年代 Turbo Pascal**: Colin 学习的第一门编程语言,需要购买编译器磁盘和阅读纸质书籍学习,开发周期为数周或数月
- **2000年代早期**: 使用 Linux、C++ 和 Corba,通过 printf 调试,没有语法高亮
- **Visual Studio 时代**: 引入断点调试功能,大幅提升开发效率,部署周期缩短至数周

### DevOps 和敏捷开发的兴起
时间戳: 约 8-12 分钟
- Colin 在金融服务公司引入 Team Foundation Server 2005 进行源代码管理
- 推动团队从瀑布模型转向敏捷开发,实现自动化构建和单元测试
- 提到 XKCD 漫画:编译时间长,开发者可以"合理摸鱼"
- **2008年**: GitHub 发明了 Pull Request,成为现代开发工作流的核心

### GitHub Copilot 的诞生
时间戳: 约 12-15 分钟
- **2022年2月23日**: GitHub 发布 Copilot 技术预览版博客文章
- 当时大多数人还不了解 LLM、Transformer 和生成式 AI
- Colin 在 2021年12月使用 Copilot 完成 Advent of Code 编程挑战
- **2022年11月**: ChatGPT 发布,生成式 AI 成为主流
- GitHub Next(研发部门)是 Copilot 的创造者,一直引领创新

### Advent of Code 与早期 Copilot 体验
时间戳: 约 15-17 分钟
- Advent of Code: 12月1日至25日每天两道编程谜题,难度递增
- Colin 使用 TypeScript 和早期 Copilot 完成挑战
- 最初的 Copilot 功能是代码补全(Code Completion)
- 第一次看到 Copilot 自动补全代码时感到"震撼"

### AI 代理时代的到来
时间戳: 约 17-20 分钟
- 更新版 XKCD 漫画:现在是"代理正在工作"
- 目标:让开发者更快、更高效,缩短从想法到部署的时间
- **Wave 1(第一波)**: 结对编程范式,代码补全,人类在前台
- **Wave 2(第二波)**: 代理能力增强,可以自主和异步工作
- **Wave 3(第三波)**: 混合团队,开发者与代理群协作
- **Wave 4(第四波)**: 完全自主,代理之间相互通信

### GitHub Copilot 使用数据
时间戳: 约 20-23 分钟
- 内部数据显示:使用 Copilot Coding Agent (CCA) 后,开发者吞吐量显著提升
- 中位数、高性能和前10%开发者的生产力都有明显增长
- **GitHub/GitHub 代码库贡献数据**:
  - 人类最高贡献者:每月约 400 次贡献
  - Copilot Coding Agent:每月 1500 次贡献(5倍于人类)
  - Copilot Code Review Agent:排名第三
- **Code Review Agent 效果**: PR 合并速度提升 20%(从5天缩短到4天)

### 挑战与解决方案
时间戳: 约 23-25 分钟
- 代码生成加速带来的挑战:需要更多规划、审查、测试、扫描和运维工作
- 分散的工具集成困难:"可互换的部件实际上不可互换"
- **GitHub 的愿景**: 成为整个 SDLC 的骨干,提供集成的平台
- 不仅加速编码,还要在规划、审查、测试、安全和运维各环节引入 AI 能力

### AI 代理的四个发展阶段
时间戳: 约 25-27 分钟
- **Wave 1 - 辅助(Assistance)**: 代码文件中的代码补全
- **Wave 2 - 增强(Augmentation)**: 代理可以同时编辑多个文件
- **Wave 3 - 编排(Orchestration)**: 自主和异步代理,多线程工作
- **Wave 4 - 完全自主(Full Autonomy)**: 代理之间相互通信,端到端自动化
- 目前处于 Wave 2 到 Wave 3 之间,部分功能已达到 Wave 4

### 未来愿景:代理式 SDLC
时间戳: 约 27-30 分钟
- **头脑风暴代理**: 创建功能或 bug 修复计划,生成工作分解
- **编码代理**: 接收任务并完成编码
- **安全和质量代理**: 检查漏洞、依赖项和代码质量
- **人工审查**: 保持"人在回路中"(Human-in-the-loop)
- **SRE 代理**: 监控生产环境,发现问题后自动创建 issue 并分配给编码代理
- 多个工作流并行运行,跨多个团队和业务单元

### GitHub Universe 2025 发布内容
时间戳: 约 30-33 分钟
- GitHub Universe 是 GitHub 的年度大会(相当于 AWS re:Invent)
- 2025年10月在旧金山举办
- 主题:**"代理的崛起"(The Rise of Agents)**
- 过去 6-8 个月的工作重点都是代理相关功能

### 三大核心能力
时间戳: 约 33-36 分钟
1. 加速编码: 更快生成代码,让代理处理繁琐任务,开发者专注高价值工作
2. 明确意图(Clarify Intent): 左移到规划阶段
   - 发布了 Planning Agent(规划代理)
   - 即将推出 Brainstorming Agent(头脑风暴代理)
   - 更详细的需求说明能获得更好的代码生成结果
3. 建立信任(Build Trust): 确保代码质量和安全性
   - 加速安全扫描和验证流程
   - 让开发者有信心部署代码

### 开发模式的转变
时间戳: 约 36-38 分钟
- **从**: 同步、单线程、单人开发
- **到**: 多线程、异步、多人协作
- 可以将 8-10 个任务同时分配给多个代理并行处理
- 改变软件工程师的日常工作方式

### Agent HQ(代理总部)
时间戳: 约 38-41 分钟
- **Agent HQ**: GitHub 作为所有代理工作流的总部(不是单独的产品标签)
- **第三方代理支持**: 
  - 即将支持 Claude Code、Jules、XAI 等第三方代理
  - 可以在 GitHub 平台上异步分配 issue 给不同代理
  - 模型和代理都将成为"商品化"选择
- **Agent Control Plane(代理控制平面)**:
  - 管理员视图
  - 批准模型列表
  - 定义自定义模型和代理
  - 设置策略和合规要求
- **Mission Control(任务控制中心)**:
  - 开发者视图
  - 查看所有正在进行的线程
  - 跟踪进度和文件变更
  - 在 Web 和 VS Code 中都可用

### 功能特性概览
时间戳: 约 41-43 分钟
- 展示了按 SDLC 阶段组织的所有功能:
  - Autofix(自动修复)
  - Code Quality(代码质量)
  - Coding Agent(编码代理)
  - Agent Mode(代理模式)
  - Code Review Agent(代码审查代理)
  - 等等
- 鼓励使用完整的工具集以获得规模经济效益
- 同时支持第三方代理集成

### 指标和度量
时间戳: 约 43-45 分钟
- 提供使用和采用指标:
  - 高级模型使用情况
  - 最受欢迎的模型
  - Coding Agent 和 Code Review Agent 使用率
- **从使用指标到影响指标**:
  - 当前重点:使用和采用度量
  - 未来方向:影响度量
  - 内部已开始测量 PR 前置时间(从打开到合并)
  - 计划将这些指标和 API 提供给用户

### 代理作为加速器
时间戳: 约 45-47 分钟
- **第三方代理**: 几周内推出
- **Mission Control**: 已推出
- **Copilot Coding Agent**: 已推出
- **自定义代理**: 类似 Claude Skills,使用 Markdown 文件定义代理行为
- **Copilot Code Review**: 在 Universe 之前,只审查 diff;现在可以审查整个 PR 上下文

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


注: 字幕在此处截断,会议可能还包含演示(Demo)环节和问答环节,但未包含在提供的字幕中。