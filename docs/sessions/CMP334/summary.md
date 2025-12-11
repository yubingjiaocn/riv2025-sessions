# AWS re:Invent 2025 EC2 Mac 会议总结

## 会议概述

本次会议由AWS EC2 Mac产品经理Vishal主持，邀请了来自Riot Games的Miranda Pearson和来自Supercell的Toni Syvanen分享他们在组织中实施EC2 Mac的经验。会议重点介绍了EC2 Mac的发展历程、客户面临的主要痛点，以及两家游戏公司如何利用EC2 Mac解决构建和测试挑战的实际案例。

会议涵盖了从2020年EC2 Mac推出至今的技术演进，包括最新的M4和M4 Pro支持、系统完整性保护(SIP)配置、Amazon DCV支持等新功能。两位客户代表详细分享了从本地Mac硬件迁移到AWS云端的完整旅程，展示了显著的性能提升和运营效率改善。

## 详细时间线与关键要点

### 0:00-10:00 - EC2 Mac历史与市场背景
- Vishal介绍EC2 Mac产品团队和今日演讲嘉宾
- 解释Apple平台应用开发生命周期中对macOS的依赖性
- 强调Xcode必须运行在Mac硬件上的限制
- 介绍市场规模：超过3400万开发者，App Store上200万应用，20亿活跃设备
- 阐述客户在EC2 Mac推出前面临的三大痛点：基础设施开销、无法自动化车队管理、无法弹性扩展

### 10:00-20:00 - EC2 Mac技术架构与演进
- 展示2020年首次推出的Intel Mac Mini架构图
- 详细介绍PCIE到Thunderbolt连接方式和AWS Nitro集成
- 分享工程团队的创新解决方案，包括机器人手指按压电源按钮
- 展示最新M4和M4 Pro Mac Mini在数据中心的实际部署照片
- 介绍新硬件带来的挑战，如电源按钮位置变化和内部SSD驱动器升级

### 20:00-30:00 - 2024年新功能发布
- M4和M4 Pro实例正式发布，已GA两个半月
- 引入专用主机自动恢复和基于重启的实例迁移功能
- 推出2TB实例存储卷，为客户提供免费的本地缓存空间
- Amazon DCV支持，提供高达4K分辨率的GUI访问
- 系统完整性保护(SIP)配置功能，通过自定义软件模拟鼠标和GUI交互
- macOS Sequoia AMI支持

### 30:00-35:00 - 客户成功案例概览
- 展示跨行业客户使用EC2 Mac的情况
- 分享客户反馈的关键收益：构建时间减少、构建失败率降低
- 强调AWS生态系统的网络和弹性优势
- 预告Matt Garman主题演讲中的EC2 Mac相关公告

### 35:00-42:00 - Riot Games案例分享
- Miranda介绍Riot的IT基础设施团队角色
- 详述在拉斯维加斯Switch数据中心的60台本地Mac硬件问题
- 分享硬件故障实例：驱动器字面意义上的融化、存储丢失、每次维修影响8%车队
- 解释迁移的三个驱动因素：公司决定退出数据中心、安全事件要求重建、VMware ESXi 8停止Mac支持
- 介绍基于Terraform的自动化解决方案和事件驱动的引导流程
- 展示迁移后的性能提升：主要构建时间提升3倍，签名提升2倍，代码构建提升2.5倍

### 42:00-49:00 - Supercell案例分享
- Toni介绍Supercell作为移动游戏公司的背景
- 分享从地下室Intel Mac"僵尸"硬件的迁移故事
- 详述四大技术支柱：EC2 Mac、Cirrus Labs Tart虚拟化、Terraform、Mise-en-place工具
- 解释使用虚拟化的原因：避免AMI切换时的清理时间
- 介绍Auto Scaling Group与AWS License Manager的集成方案
- 展示架构：EFS存储Tart VM镜像，使用本地NVME存储提升性能
- 分享显著成果：从每日150个构建增长到1800个构建，用3倍Mac数量支持10倍构建车间

### 49:00-49:24 - 会议总结与后续活动预告
- Vishal感谢演讲嘉宾并预告相关会议
- 强调关注Matt Garman CEO主题演讲的EC2 Mac公告
- 介绍三个相关技术会议：CMP 306实践工作坊、CMP 346 ML推理应用、CMP 344 GitHub Actions集成演示