# 程序员必读的 Prompt Engineering 指南 - 完整目录

> 14个实战编程任务的AI协作指南，覆盖需求到交付的整个软件开发生命周期

---

## 🎯 14大核心任务概览

本指南按**5个开发阶段**组织，每个阶段包含若干核心任务：

### 📋 阶段1：需求与规划
- **T01: Requirement Clarification** - 理清需求、确认范围、澄清边界
- **T08: Architecture Decision Draft** - 架构决策、方案评估、技术选型

### 💻 阶段2：设计与开发
- **T09: API Contract Design** - API设计、接口定义、契约规范
- **T02: Feature Implementation** - 功能编码、代码生成、API实现
- **T04: Refactor with Behavior Safety** - 安全重构、代码改进、技术债处理

### 🐛 阶段3：测试与质量
- **T05: Unit Test Generation** - 单元测试编写、覆盖率提升
- **T06: Integration Test Plan** - 集成测试设计、场景规划
- **T07: Code Review Assistant** - 代码审查、质量把控、最佳实践
- **T03: Bug Reproduction and Root Cause** - Bug复现、根因分析、问题诊断

### 🚀 阶段4：优化与维护
- **T10: SQL/Query Optimization** - 数据库优化、查询性能
- **T12: Performance Optimization** - 整体性能优化、资源管理
- **T11: Security Review** - 安全审查、漏洞识别、防护加固
- **T13: Legacy Code Understanding** - 遗留代码理解、知识转移

### 📚 阶段5：文档与交付
- **T14: Documentation Generation** - 文档生成、知识沉淀

---

## 📚 按阶段的完整目录

### 📋 01-Phase-Planning（阶段1：需求与规划）

#### T01: Requirement Clarification（需求澄清）⭐

**文件位置**: `01-Requirement-Clarification/`
**难度**: ⭐ 初级
**关键能力**: 需求分析、边界确认、范围管理
**何时使用**: 项目启动、需求评审

**包含内容**:
- 核心概念：为什么要澄清需求
- 最佳实践：如何高效地与相关方沟通
- 6个Prompt示例
- 常见误区和高级技巧

**核心Prompt示例**:
1. 模糊需求的澄清
2. 用户故事补充
3. 场景边界确认
4. 非功能需求列举
5. 可行性快速评估
6. 风险识别

---

#### T08: Architecture Decision Draft（架构决策）⭐⭐⭐⭐

**文件位置**: `08-Architecture-Decision-Draft/`
**难度**: ⭐⭐⭐⭐ 中高级
**关键能力**: 架构设计、权衡分析、决策记录
**何时使用**: 系统设计、技术栈选择

**包含内容**:
- 核心概念：如何做出好的架构决策
- 最佳实践：ADR模式、权衡分析
- 架构决策框架和模板
- 常见架构选择的利弊分析

---

### 💻 02-Phase-Development（阶段2：设计与开发）

#### T09: API Contract Design（API设计）⭐⭐⭐

**文件位置**: `09-API-Contract-Design/`
**难度**: ⭐⭐⭐ 中级
**关键能力**: 接口设计、规范制定、文档生成
**何时使用**: 模块接口设计、API定义

**包含内容**:
- 核心概念：好的API设计原则
- 最佳实践：RESTful设计、版本管理
- OpenAPI/Swagger规范应用
- API文档生成和维护

---

#### T02: Feature Implementation（功能实现）⭐⭐

**文件位置**: `02-Feature-Implementation/`
**难度**: ⭐⭐ 初中级
**关键能力**: 代码生成、算法设计、框架应用
**何时使用**: 日常编码、功能开发

**包含内容**:
- 核心概念：如何有效地请求AI生成代码
- 最佳实践：代码质量标准、架构考虑
- 8个Prompt示例
- 代码审查要点
- examples.md（详细示例）
- best-practices.md（最佳实践）

**核心Prompt示例**:
1. 功能模块实现
2. API端点开发
3. 数据处理逻辑
4. 业务规则编码
5. 错误处理机制
6. 依赖集成

---

#### T04: Refactor with Behavior Safety（安全重构）⭐⭐⭐

**文件位置**: `04-Refactor-With-Behavior-Safety/`
**难度**: ⭐⭐⭐ 中级
**关键能力**: 代码改进、重构策略、风险控制
**何时使用**: 代码改进、技术债处理

**包含内容**:
- 核心概念：为什么要安全地重构
- 最佳实践：测试驱动的重构
- 大规模重构的步骤和注意事项
- 常见重构模式

---

### 🐛 03-Phase-Quality（阶段3：测试与质量）

#### T05: Unit Test Generation（单元测试）⭐⭐

**文件位置**: `05-Unit-Test-Generation/`
**难度**: ⭐⭐ 初中级
**关键能力**: 测试设计、边界覆盖、Mock使用
**何时使用**: 测试补充、覆盖率提升

**包含内容**:
- 核心概念：单元测试的价值
- 最佳实践：测试设计原则
- 各语言的测试框架应用
- 边界测试和异常处理

---

#### T06: Integration Test Plan（集成测试）⭐⭐⭐

**文件位置**: `06-Integration-Test-Plan/`
**难度**: ⭐⭐⭐ 中级
**关键能力**: 测试场景设计、系统交互验证
**何时使用**: 系统验证、上线前检验

**包含内容**:
- 核心概念：集成测试的设计
- 最佳实践：场景规划、模拟数据
- 测试环境配置
- 持续集成流程

---

#### T07: Code Review Assistant（代码审查）⭐⭐

**文件位置**: `07-Code-Review-Assistant/`
**难度**: ⭐⭐ 初中级
**关键能力**: 质量评估、最佳实践识别、建设性反馈
**何时使用**: PR审查、质量把控

**包含内容**:
- 核心概念：代码审查的目的和原则
- 最佳实践：如何进行有效的审查
- 8个真实审查示例
- 常见问题和改进建议
- examples.md（详细审查案例）

**审查维度**:
1. 功能正确性
2. 代码质量
3. 性能考虑
4. 安全性
5. 可维护性
6. 测试完整性
7. 文档充分性

---

#### T03: Bug Reproduction and Root Cause（Bug诊断）⭐⭐

**文件位置**: `03-Bug-Reproduction-Root-Cause/`
**难度**: ⭐⭐ 初中级
**关键能力**: 问题诊断、日志分析、根因追踪
**何时使用**: 问题排查、性能诊断

**包含内容**:
- 核心概念：系统化的Bug排查方法
- 最佳实践：信息收集、假设验证
- 7个真实诊断案例
- 日志分析指南
- examples.md（详细案例）
- checklist.md（诊断工具清单）

**诊断技巧**:
1. 错误堆栈分析
2. 重现步骤设计
3. 日志诊断
4. 性能瓶颈定位
5. 内存泄漏追踪
6. 并发问题诊断
7. 跨服务链路追踪

---

### 🚀 04-Phase-Optimization（阶段4：优化与维护）

#### T10: SQL/Query Optimization（查询优化）⭐⭐⭐

**文件位置**: `10-SQL-Query-Optimization/`
**难度**: ⭐⭐⭐ 中级
**关键能力**: 查询分析、索引设计、性能基准测试
**何时使用**: 数据库调优、性能瓶颈分析

**包含内容**:
- 核心概念：查询优化的原理
- 最佳实践：索引设计、查询改写
- 各数据库的优化技巧
- 性能测试和监控

---

#### T12: Performance Optimization（性能优化）⭐⭐⭐⭐

**文件位置**: `12-Performance-Optimization/`
**难度**: ⭐⭐⭐⭐ 中高级
**关键能力**: 性能分析、瓶颈识别、优化实施
**何时使用**: 性能调优、资源优化

**包含内容**:
- 核心概念：性能优化的系统方法
- 最佳实践：profiling、监控、优化策略
- 各层级的优化手段
- 成本与收益的权衡

---

#### T11: Security Review（安全审查）⭐⭐⭐⭐

**文件位置**: `11-Security-Review/`
**难度**: ⭐⭐⭐⭐ 中高级
**关键能力**: 漏洞识别、防护设计、安全加固
**何时使用**: 安全评估、漏洞检查

**包含内容**:
- 核心概念：常见的安全漏洞类型
- 最佳实践：OWASP Top 10应对
- 代码审查的安全视角
- 渗透测试基础

---

#### T13: Legacy Code Understanding（遗留代码）⭐⭐⭐

**文件位置**: `13-Legacy-Code-Understanding/`
**难度**: ⭐⭐⭐ 中级
**关键能力**: 代码理解、知识转移、重构规划
**何时使用**: 知识转移、技术债清理

**包含内容**:
- 核心概念：如何有效地理解陌生代码
- 最佳实践：文档补充、单元测试、逐步优化
- 大规模重构的规划
- 知识转移的方法

---

### 📚 05-Phase-Documentation（阶段5：文档与交付）

#### T14: Documentation Generation（文档生成）⭐⭐

**文件位置**: `14-Documentation-Generation/`
**难度**: ⭐⭐ 初中级
**关键能力**: 文档组织、清晰表达、自动化生成
**何时使用**: 文档生成、知识沉淀

**包含内容**:
- 核心概念：好的技术文档的特征
- 最佳实践：文档组织、维护策略
- 文档类型和模板
  - API文档
  - 架构文档
  - 部署指南
  - 故障排查指南
  - 开发指南
- 文档生成工具

---

## 📊 任务按难度分类

### ⭐ 初级任务（适合新手）
- T01: Requirement Clarification
- T02: Feature Implementation（第一部分）
- T05: Unit Test Generation
- T07: Code Review Assistant（第一部分）
- T14: Documentation Generation

### ⭐⭐ 初中级任务
- T02: Feature Implementation（完整）
- T03: Bug Reproduction and Root Cause
- T05: Unit Test Generation（完整）
- T07: Code Review Assistant（完整）
- T09: API Contract Design（基础）
- T14: Documentation Generation（完整）

### ⭐⭐⭐ 中级任务
- T04: Refactor with Behavior Safety
- T06: Integration Test Plan
- T09: API Contract Design（完整）
- T10: SQL/Query Optimization
- T13: Legacy Code Understanding

### ⭐⭐⭐⭐ 中高级任务
- T08: Architecture Decision Draft
- T11: Security Review
- T12: Performance Optimization

---

## 🗺️ 快速导航

### 按开发阶段
- 👉 **[01-Phase-Planning](01-Phase-Planning/)** - 需求与规划
- 👉 **[02-Phase-Development](02-Phase-Development/)** - 设计与开发
- 👉 **[03-Phase-Quality](03-Phase-Quality/)** - 测试与质量
- 👉 **[04-Phase-Optimization](04-Phase-Optimization/)** - 优化与维护
- 👉 **[05-Phase-Documentation](05-Phase-Documentation/)** - 文档与交付

### 快速查询
- 👉 [QUICK-REFERENCE.md](QUICK-REFERENCE.md) - 快速查询模板
- 👉 [使用说明.md](使用说明.md) - 学习路径和任务导航

---

## 📈 项目统计

- **核心任务**: 14个
- **开发阶段**: 5个
- **文件夹**: 19个（5个Phase + 14个Task）
- **文档**: 22个文件
- **Prompt示例**: 40+个
- **详细说明**: 相当于100+页的技术文档

---

**准备好了吗？选择一个阶段，开始学习吧！**
