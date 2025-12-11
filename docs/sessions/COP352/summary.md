# AWS re:Invent 2025 基础设施即代码治理会议总结

## 会议概述

本次会议由AWS首席工程师David Kilman和高级解决方案架构师Sefi Abrech主讲，主题为"基础设施即代码治理：让IAC部署更安全"。会议重点介绍了AWS CloudFormation Hooks功能，展示了如何通过主动控制机制防止不安全或不合规的基础设施部署。

演讲者通过生动的实际案例和现场演示，展示了从被动检测控制向主动预防控制的转变。会议涵盖了CloudFormation Guard规则编写、Hooks配置、以及如何在组织级别通过Control Tower实施治理策略。同时也演示了如何在Terraform中使用AWSCC provider实现相同的治理效果。

## 详细时间线与关键要点

### 0:00-5:00 开场介绍
- David Kilman自我介绍，AWS CloudFormation首席工程师
- Sefi Abrech介绍，专注治理、合规和安全的高级解决方案架构师
- 现场调研：100%参会者使用基础设施即代码
- 介绍会议互动形式和主题概览

### 5:00-15:00 主动控制的重要性
- 展示传统CICD流程中的治理挑战
- David分享Lambda Function Endpoints的真实故事：创建了全球可访问的端点，被安全团队检测到并要求删除
- 强调主动控制优于被动检测的原因：防止问题发生而非事后修复
- 介绍另一个案例：实习生意外修改Auto Scaling Group配置，Hooks成功阻止了生产环境的潜在故障

### 15:00-25:00 成本控制和最佳实践
- 讨论如何通过Hooks防止意外的高成本资源创建
- 介绍组织级别的成本优化策略：强制使用有折扣的EC2实例类型
- 解释COE（Correction of Error）文化和如何将经验教训编码化为自动化控制
- 强调主动控制在合规性框架（如FedRAMP、NIST）中的重要作用

### 25:00-35:00 CloudFormation Guard和Hooks实战
- 介绍CloudFormation Guard作为策略即代码DSL
- 演示从GitHub Guard Rules Registry获取预写规则
- 创建"Gotcha Hook"，配置为在资源创建/更新时运行
- 展示Hook在失败模式下的工作原理

### 35:00-45:00 实际部署演示
- 使用生成式AI创建包含Lambda、DynamoDB和S3的CloudFormation模板
- 演示部署失败场景：S3 bucket缺少object lock和public access block配置
- 展示如何通过Change Sets提前发现所有合规性问题
- 逐步修复模板中的合规性问题

### 45:00-50:00 Control Catalog简化体验
- 介绍AWS Control Catalog作为预构建策略的解决方案
- 展示如何通过点击界面快速启用多个合规性控制
- 演示按合规框架（如NIST）分组的控制策略
- 强调无需编写代码即可实现治理的便利性

### 50:00-55:00 Terraform集成演示
- Sefi演示使用AWSCC provider在Terraform中实现Hooks
- 展示Lambda运行时版本检查和S3安全配置验证
- 解释AWSCC provider与标准AWS provider的区别
- 演示Terraform中的错误输出和调试信息

### 55:00-59:00 组织级部署和总结
- 通过Control Tower在组织单元级别部署控制策略
- 展示多账户环境中的集中化治理管理
- 介绍防御深度策略：结合主动和被动控制
- 回答观众问题：异常处理、区域支持、可观测性改进等