# AWS re:Invent 2025 - DAT325 会议总结

## 会议概述

本次会议主题为"如何通过 RDS for SQL Server 和 Oracle 降低成本并提高运营效率"，由 AWS RDS 数据库总监 Mahul Sha 主讲。会议重点介绍了 Amazon RDS 商业数据库引擎（SQL Server 和 Oracle）的最新功能和成本优化策略。

会议首先回顾了 RDS 商业数据库引擎的核心价值：简化迁移、灵活的许可选项、托管服务的便利性以及高可用性配置。随后深入探讨了三个主要创新领域：存储卷管理的改进、SQL Server 的成本优化功能，以及 Oracle 的裸机实例支持。这些新特性使客户能够在保持性能的同时显著降低运营成本，特别是通过灵活的存储管理、优化的许可模式和智能的 CPU 配置实现高达 74% 的成本节省。

会议强调了 AWS 如何通过技术创新帮助客户更高效地使用商业数据库，同时为未来的数据库迁移和现代化提供灵活的路径。

## 详细时间线

### 开场与 RDS 介绍
[00:00 - 05:30] 会议开场与受众调查
- 会议编号 DAT325，主题为使用 RDS for SQL Server 和 Oracle 降低成本
- 主讲人 Mahul Sha 介绍自己负责 RDS 的 SQL Server、Oracle 和 DB2 数据库
- 现场调查显示大多数观众已使用 Amazon RDS，约半数使用 SQL Server，相当数量使用 Oracle

[05:30 - 08:45] AWS 关系型数据库产品组合
- 介绍 AWS 关系型数据库产品线：Aurora（PostgreSQL 和 MySQL 兼容版）、Aurora DSQL、开源数据库 RDS（PostgreSQL、MySQL、MariaDB）
- 重点讲解商业数据库引擎 RDS：Oracle、SQL Server 和 DB2

[08:45 - 15:20] RDS 商业数据库引擎的核心优势
- **易于迁移**：客户可直接将本地 Oracle 和 SQL Server 应用迁移到云端，无需修改应用、架构或存储过程
- **灵活的许可选项**：支持自带许可（BYOL）和许可包含（License Included）模式
- 许可包含模式的优势：按小时付费、根据需求灵活调整、适合逐步迁移到其他数据库的场景
- **托管服务**：自动化软件补丁、更新、备份和跨区域灾难恢复
- 新功能：分阶段升级，可先在测试环境应用更新，几周后再应用到生产环境
- **高可用性选项**：Multi-AZ 配置和只读副本

### 存储卷管理创新
[15:20 - 18:30] Multi-AZ 配置架构说明
- 应用通过实例端点连接到主实例
- 主实例由 EBS 卷支持
- Multi-AZ 配置自动在不同可用区创建备用实例
- 数据从主实例同步复制到备用实例，事务提交前写入两个实例

[18:30 - 23:45] 客户面临的存储挑战
- 存储容量限制：单个卷最大 64TB，部分客户需要更大容量
- 缺乏弹性伸缩：无法根据短期需求增减存储
- 存储类型限制：无法在同一数据库中混合使用 IO2（高性能）和 GP3（成本优化）卷
- 复制通道限制：单通道吞吐量约 625 MB/s，大数据量写入时可能成为瓶颈

[23:45 - 28:15] 附加存储卷功能介绍
- 可为单个实例添加最多 3 个附加卷（加上主卷共 4 个）
- 总存储容量可达 256TB
- 支持动态添加和删除卷，无需应用停机
- 功能同时支持 RDS Oracle 和 RDS SQL Server

[28:15 - 35:40] 附加存储卷使用演示
- 使用 modify-db-instance 命令添加卷，指定卷名、存储类型（IO2）、容量和 IOPS
- Oracle 中通过修改 db_create_file_dest 参数将默认表空间位置指向新卷
- 使用 ALTER SESSION 命令更改默认位置
- 新创建的表空间自动存储在附加卷中

[35:40 - 42:50] 表空间迁移操作
- 演示如何将现有表空间从主卷移动到附加卷
- 使用 SELECT 查询表空间位置和文件 ID
- 使用 MOVE DATAFILE 命令将表空间移动到附加卷
- 操作过程无需应用停机
- 演示反向操作：将表空间移回主卷并删除附加卷
- 删除卷前需确保卷中无活动文件，系统会防止误删除

[42:50 - 47:30] 附加存储卷的高级应用
- 支持混合使用 IO2 和 GP3 卷类型
- 建议主卷使用 IO2（因为预写日志始终在主卷），附加卷可使用 GP3
- Multi-AZ 配置中每个附加卷拥有独立的复制通道（625 MB/s）
- 多个卷可提供更高的总复制吞吐量
- 适合将高写入量的表或数据库放在独立卷中

[47:30 - 49:20] 附加存储卷功能总结
- 提供更大存储容量（最高 256TB）
- 支持 SQL Server 和 Oracle
- 动态添加/删除卷，无停机时间
- 支持临时存储需求（如 SQL Server 临时文件）
- 可混合 IO2 和 GP3 卷
- Multi-AZ 配置中自动复制到主备实例

### SQL Server 成本优化功能
[49:20 - 54:30] SQL Server Developer Edition 支持
- Microsoft SQL Server Developer Edition 现已完全支持 RDS
- Developer Edition 功能完整，包含 Enterprise Edition 所有特性
- 免许可费用，专为非生产和开发测试环境设计
- 可将开发和测试环境切换到 Developer Edition，生产环境继续使用 Standard 或 Enterprise

[54:30 - 57:15] Developer Edition 成本节省分析
- 以 M6.XL 实例为例（美国东部弗吉尼亚地区公开定价）
- Standard Edition：$0.977/小时 → Developer Edition：$0.60/小时
- Enterprise Edition：$2.501/小时 → Developer Edition：$0.74/小时
- 切换到 Developer Edition 可节省高达 74% 的开发测试环境成本

[57:15 - 01:01:30] Developer Edition 使用步骤
1. 从 Microsoft 网站下载 SQL Server Developer Edition ISO 镜像（许可合规要求）
2. 使用 s3 cp 命令将 ISO 上传到 S3 存储桶
3. 使用 create-db-engine-version 命令创建自定义引擎版本，指定 S3 存储桶和 ISO 文件名
4. 使用 create-db-instance 命令创建实例，指定自定义引擎版本
5. 实例创建后即可使用所有 RDS 功能

[01:01:30 - 01:06:45] SQL Server Web Edition 高可用性支持
- Web Edition 专为 Web 托管设计，适用于网站、Web 服务、ASP 页面和内部 Web 应用
- 许可费用低于 Standard 和 Enterprise Edition
- 问题：Web Edition 不支持 Always On 可用性组（仅 Enterprise 和 Standard 支持）
- AWS 解决方案：使用同步块级复制实现 Multi-AZ 高可用性

[01:06:45 - 01:11:20] Web Edition Multi-AZ 架构
- 应用连接到 RDS 实例端点
- 主实例由 EBS 卷支持
- 块级复制将数据同步到备用实例的 EBS 卷
- 许可仅计算一个实例（主实例），因为备用实例不运行 SQL Server
- RDS 自动检测故障并切换到备用实例
- 切换后原主实例变为新备用实例，复制方向反转

[01:11:20 - 01:14:30] Web Edition 成本节省
- Multi-AZ 配置价格对比（美国东部弗吉尼亚地区）
- M6.XL：Standard $2.45/小时 → Web $1.01/小时
- R6.XL：Standard $3.04/小时 → Web $1.69/小时
- 切换到 Web Edition 可节省高达 58% 成本
- 现有 Web Edition 单可用区用户可升级到 Multi-AZ 获得高可用性

[01:14:30 - 01:16:00] 启用 Web Edition Multi-AZ
- 在控制台使用 modify-db-instance 选项
- 将 multi-az-deployment 属性设置为 Yes
- RDS 自动创建备用实例
- 应用无需任何更改

### CPU 优化与许可成本降低
[01:16:00 - 01:20:30] 基于 vCPU 的许可收费机制
- SQL Server 许可基于虚拟 CPU (vCPU) 数量收费
- Intel 实例使用 SMT（同步多线程）技术
- 每个物理 CPU 核心运行两个并行线程（2 个 vCPU）
- SMT 提供性能提升但非 2 倍性能
- 许可费用按 2 倍 vCPU 计算

[01:20:30 - 01:24:45] 内存密集型工作负载案例分析
- 示例：R7.8XL 实例工作负载
- 内存使用率：75%（剩余 25% 可用内存）
- CPU 使用率：仅 10%
- 工作负载为内存密集型而非 CPU 密集型
- 关闭 SMT 后：vCPU 从 32 降至 16，CPU 使用率仍低于 20%
- 许可费用从 32 vCPU 降至 16 vCPU

[01:24:45 - 01:29:30] Optimized CPU 功能
- 针对第 7 代及未来实例自动优化 SMT 设置
- 根据实例大小和性能特征自动调整
- 开箱即用获得更好的性价比

[01:29:30 - 01:33:15] 实例升级成本节省
- R6.2XL → R7.2XL（相同物理 CPU 核心数）
  - Enterprise：$7.202/小时 → $3.868/小时
  - Standard：$6.080/小时 → $2.848/小时
- M6.2XL → M7.2XL
  - Enterprise：$6.657/小时 → $3.295/小时
  - Standard：$5.096/小时 → $2.275/小时
- 升级到新一代实例可节省高达 55% 成本

[01:33:15 - 01:36:45] 高级 CPU 优化配置
- 可进一步微调 Optimized CPU 设置
- 配置活动 CPU 核心数量（开启或关闭物理核心）
- 示例：默认 8 个物理核心，可调整为 7 或 6
- 降低 vCPU 数量 = 降低软件许可费用
- 先通过升级获得性能提升，再通过微调进一步优化成本

### Oracle 裸机实例支持
[01:36:45 - 01:39:00] EC2 裸机实例介绍
- 裸机实例由完整物理服务器支持
- 绕过虚拟化层（无 Hypervisor）
- 应用软件直接访问物理硬件
- 适用于大型数据库和大内存实例
- 可从大型虚拟内存实例切换到裸机实例
- 提供相同的 CPU 和内存容量

[会议结束]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


关键要点：
- 附加存储卷功能提供高达 256TB 存储容量和灵活的存储管理
- SQL Server Developer Edition 可为开发测试环境节省 74% 成本
- SQL Server Web Edition Multi-AZ 支持可节省 58% 成本
- Optimized CPU 功能通过实例升级可节省高达 55% 成本
- 所有功能均支持零停机操作，保障业务连续性