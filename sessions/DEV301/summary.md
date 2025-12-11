# AWS re:Invent 2025 边缘AI代理工作流会议总结

## 会议概述

本次技术会议由AWS开发者倡导者Anna和AWS社区英雄David（来自墨西哥的Victoria）共同主讲，重点探讨了如何在边缘环境中实现AI代理工作流，特别是在网络连接不稳定或完全离线的工业场景中。会议介绍了使用Strengths Agents SDK和Ollama相结合的解决方案，以解决工业运营中因网络中断导致的高昂停机成本问题。

演讲者通过实际代码演示和现场Demo，展示了如何构建能够在本地运行的AI代理系统，该系统具备推理能力、工具调用、会话管理和结构化输出等核心功能。会议还介绍了AWS Kiro这一新的代理IDE工具，以及如何通过MCP（模型上下文协议）服务器扩展代理功能。

## 详细时间线与关键要点

### 0:00-5:00 会议开场与问题背景
- 介绍演讲者：Anna（AWS开发者倡导者）和David（AWS社区英雄，来自墨西哥）
- **核心问题**：Aberdeen研究显示工业运营中计划外停机的平均成本超过每小时206万美元
- **受影响行业**：采矿（地下无信号）、制造业（远程工厂遗留基础设施）、石油天然气（海上平台）、能源、政府（数据主权要求）、零售等

### 5:00-10:00 云依赖问题与解决方案架构
- **云依赖问题**：工厂传感器数据分析需要互联网连接，一旦断网就无法使用AI代理
- **离线代理需求**：本地LLM推理、本地工具调用、会话记忆、云端同步能力
- **混合架构方案**：Strengths Agents SDK + Ollama实现边缘AI代理能力
- 现场调研：部分观众有Strengths Agents和Ollama使用经验

### 10:00-15:00 Ollama介绍与代理循环机制
- **Ollama功能**：开源工具，支持在本地计算机运行轻量级LLM（如80亿参数模型）
- **支持模型**：Google Gemma 3、Mistral AI、Meta Llama、DeepSeek、Qwen GPT等
- **代理循环流程**：
  - 推理阶段：接收用户输入，LLM处理并决定是否调用工具
  - 行动阶段：执行工具调用获取额外上下文
  - 响应阶段：代理满意后返回最终输出

### 15:00-20:00 Strengths Agents SDK详解
- **核心特性**：开源Python SDK（昨天新增TypeScript支持），面向开发者的构建工具
- **扩展性**：支持工具、MCP、内存管理等功能扩展
- **模型兼容性**：支持Amazon Bedrock、Ollama、Anthropic API、OpenAI API、Grok等
- **基础代理代码**：
 python
  import strands
  agent = strands.Agent()  # 默认使用Bedrock Claude Sonnet 4.0
  

### 20:00-25:00 本地代理实现与工具创建
- **本地代理配置**：
 python
  from strands.models import OllamaModel
  model = OllamaModel(host="localhost", port=11434, model_id="qwen2.5:8b")
  agent = strands.Agent(model=model, tools=[custom_tools])
  
- **自定义工具创建**：使用@tool装饰器将Python函数转换为代理工具
- **工具示例**：读取传感器、触发警报等工业场景专用工具
- **文档字符串重要性**：帮助代理理解工具用途和调用方式

### 25:00-30:00 社区工具与结构化输出
- **内置工具类型**：HTTP请求、系统诊断、工作流程、人工干预、文件操作等
- **结构化输出**：使用Pydantic模型定义数据结构，确保与ERP、CRM、MIS等系统的API兼容
- **工单示例**：
 python
  class WorkOrder(BaseModel):
      part_id: str
      priority: str
      description: str
      estimated_hours: int
  

### 30:00-35:00 会话管理与MCP集成
- **会话管理**：使用FileSessionManager实现本地持久化内存
- **断电恢复**：应用重启后能够继续之前的对话上下文
- **MCP协议**：Anthropic创建的模型上下文协议，支持第三方工具集成
- **MongoDB MCP示例**：本地MongoDB数据库操作工具集成

### 35:00-40:00 现场Demo演示
- **Jupyter Notebook演示**：展示IOT控制代理的完整实现
- **工具功能**：温度传感器读取、湿度检测、阀门控制等
- **多步骤操作**：单次请求完成多个任务（检查湿度并判断是否在可接受范围内）
- **结构化输出Demo**：将SCADA系统文本响应转换为结构化JSON数据
- **会话恢复**：模拟系统故障后成功恢复对话状态

### 40:00-43:30 AWS Kiro介绍与总结
- **Kiro功能**：AWS新推出的代理IDE工具，支持MCP服务器集成
- **Strengths MCP服务器**：为Kiro提供最新的Strengths SDK文档和代码建议
- **AWS MCP生态**：超过40个AWS MCP服务器，包括实时文档查询
- **Steering功能**：为代理提供项目上下文和技术栈指导
- **自动提交**：Kiro完成任务后自动创建Git提交
- **结语**："不要等待云端思考，而要利用云端思考得更大"