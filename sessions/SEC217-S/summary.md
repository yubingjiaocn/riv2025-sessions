# AWS re:Invent 2025 技术会议总结：基于代理工作流的自动化云安全修复

## 会议概述

本次技术会议由Dynatrace首席解决方案工程师Matt Gibbets主讲，AWS同事Raj和Shannon共同参与。会议主题聚焦于通过代理工作流实现自动化云安全修复，展示了Dynatrace与AWS Security Hub的深度集成如何利用AI技术自动化处理安全漏洞。

演讲者详细介绍了Dynatrace可观测性平台与AWS安全服务的协同工作原理，重点展示了如何通过MCP协议驱动的代理工作流，在2分钟内完成从安全问题识别、优先级排序到自动修复的完整流程。会议包含了实时演示，展现了从AWS Security Hub检测到EC2端口开放问题，到通过Dynatrace平台自动关闭端口并验证修复结果的全过程。

## 详细时间线与关键要点

### 0:00-2:00 会议开场与议程介绍
- Matt Gibbets介绍演讲团队和会议主题
- 强调将讨论AI驱动的自动化云安全修复
- 概述议程：Dynatrace与AWS合作关系、云安全挑战、代理工作流安全修复

### 2:00-5:00 Dynatrace与AWS Security Hub集成亮点
- 介绍Dynatrace与AWS Security Hub的关键集成功能
- 展示如何将AWS云原生服务漏洞数据整合到统一可观测性平台
- 说明Davis co-pilot如何利用AI理解并触发安全漏洞自动化修复
- 强调MCP协议在代理工作流中的核心作用

### 5:00-8:00 Dynatrace平台架构深度解析
- 详细介绍Dynatrace可观测性平台的整体架构
- 重点阐述Grail后端架构的独特优势
- 说明如何将性能数据、安全数据、业务数据进行上下文关联
- 强调准确数据对自动化修复的重要性

### 8:00-10:00 AWS合作关系与Security Hub功能
- Raj介绍Dynatrace作为AWS高级技术合作伙伴的地位
- 展示100+AWS服务集成和10年以上合作历史
- 详细介绍AWS Security Hub的统一云安全解决方案功能
- 说明漏洞关联、优先级排序、规模化响应等核心能力

### 10:00-12:00 云安全挑战与解决方案架构
- Shannon分析当前云安全面临的主要挑战：告警过载、手动流程、工作流碎片化
- 介绍通过EventBridge和Lambda将Security Hub数据导入Dynatrace
- 展示Open Pipeline功能如何实现安全告警的上下文化分析
- 说明完整的自动化修复架构流程

### 12:00-15:00 实时演示与总结
- 现场演示从AWS Security Hub发现EC2端口开放问题
- 展示Dynatrace平台自动创建Jira工单并进行影响分析
- 演示通过Kiro CLI和MCP服务器实现自动修复
- 验证修复结果并确认Security Hub中问题状态更新
- 总结2分钟内完成完整自动化修复流程的价值

### 15:00-15:20 互动环节与会议结束
- 邀请观众扫描二维码了解更多集成信息
- 推广Dynatrace展台575号展位
- 强调该工作流适用于所有云安全从业者