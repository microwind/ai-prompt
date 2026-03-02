# 程序员必读的 Prompt Engineering 指南系列

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Last Updated](https://img.shields.io/badge/Last%20Updated-2026%2F03-blue)
![Status](https://img.shields.io/badge/Status-Active-success)
![Tasks](https://img.shields.io/badge/Tasks-14-blue)

> **14个实战编程任务的AI协作指南** | 从需求澄清到文档生成，覆盖整个软件开发生命周期

---

## 📖 项目介绍

这是一份**实用的Prompt Engineering指南**，围绕14个核心编程任务组织，帮助你在日常工作中更高效地与AI（Claude、GPT等）协作。

**不同于以往的Prompt指南：**
- 🎯 **任务驱动** - 围绕实际的编程工作流组织
- 💼 **实战导向** - 每个任务都源于真实的编程场景
- 📋 **完整覆盖** - 从需求分析到项目交付的全链路
- ✅ **即插即用** - Prompt可直接复制使用，无需修改

**适合以下开发者:**
- 🎓 **初学者** - 快速学习标准编程工作流
- 👨‍💻 **中级开发者** - 提高编码效率和代码质量
- 🏗️ **架构师** - 优化系统设计和决策过程
- 🚀 **技术主管** - 指导团队有效使用AI工具

---

## 🎯 14大核心任务一览

### 按难度分类

#### ⭐ 初级任务（入门级）
| 任务 | 名称 | 何时使用 |
|------|------|--------|
| **T01** | **Requirement Clarification** | 项目启动、需求评审 |
| **T02** | **Feature Implementation** | 日常编码、功能开发 |
| **T03** | **Bug Reproduction & Root Cause** | 问题排查、性能诊断 |
| **T05** | **Unit Test Generation** | 测试补充、覆盖率提升 |
| **T07** | **Code Review Assistant** | PR审查、质量把控 |
| **T14** | **Documentation Generation** | 文档生成、知识沉淀 |

#### ⭐⭐ 中级任务（需要进阶知识）
| 任务 | 名称 | 何时使用 |
|------|------|--------|
| **T04** | **Refactor with Behavior Safety** | 代码改进、技术债处理 |
| **T06** | **Integration Test Plan** | 系统验证、上线前检验 |
| **T09** | **API Contract Design** | 接口定义、模块设计 |
| **T10** | **SQL/Query Optimization** | 数据库优化、查询性能 |
| **T13** | **Legacy Code Understanding** | 知识转移、技术债清理 |

#### ⭐⭐⭐ 高级任务（需要专业经验）
| 任务 | 名称 | 何时使用 |
|------|------|--------|
| **T08** | **Architecture Decision Draft** | 系统设计、技术选型 |
| **T11** | **Security Review** | 安全审查、漏洞检查 |
| **T12** | **Performance Optimization** | 性能调优、资源优化 |

---

## 📁 项目结构

```
ai-prompt/
├── README.md                                    ← 本文件（快速导航）
├── CATALOG.md                                   ← 完整目录和详细说明
├── QUICK-REFERENCE.md                           ← 快速查询模板
├── 使用说明.md                                  ← 学习路径指南
├── 项目完整导航.md                              ← 详细统计和资源
│
├── programmer_prompt_engineering_guide.md       ← 📚 程序员Prompt工程完全指南
├── developer_prompt_engineering_guide.md        ← 📚 开发者版Prompt工程指南
│
├── 01-Requirement-Clarification/                ← T01: 需求澄清 ⭐
│   └── README.md
├── 02-Feature-Implementation/                   ← T02: 功能实现 ⭐⭐
│   └── README.md
├── 03-Bug-Reproduction-Root-Cause/              ← T03: Bug诊断 ⭐⭐
│   ├── README.md
│   ├── checklist.md
│   └── examples.md
├── 04-Refactor-With-Behavior-Safety/            ← T04: 安全重构 ⭐⭐⭐
│   └── README.md
├── 05-Unit-Test-Generation/                     ← T05: 单元测试 ⭐
│   └── README.md
├── 06-Integration-Test-Plan/                    ← T06: 集成测试 ⭐⭐⭐
│   └── README.md
├── 07-Code-Review-Assistant/                    ← T07: 代码审查 ⭐
│   └── README.md
├── 08-Architecture-Decision-Draft/              ← T08: 架构决策 ⭐⭐⭐⭐
│   └── README.md
├── 09-API-Contract-Design/                      ← T09: API设计 ⭐⭐⭐
│   └── README.md
├── 10-SQL-Query-Optimization/                   ← T10: 查询优化 ⭐⭐⭐
│   └── README.md
├── 11-Security-Review/                          ← T11: 安全审查 ⭐⭐⭐⭐
│   └── README.md
├── 12-Performance-Optimization/                 ← T12: 性能优化 ⭐⭐⭐⭐
│   └── README.md
├── 13-Legacy-Code-Understanding/                ← T13: 遗留代码 ⭐⭐⭐
│   └── README.md
└── 14-Documentation-Generation/                 ← T14: 文档生成 ⭐
    ├── README.md
    └── prompt_examples.md
```

---

## 🚀 快速开始

### 方式1：按问题找答案（5分钟）

**我遇到什么问题？** → **打开对应的任务目录** → **复制Prompt使用**

| 常见问题 | 对应任务 |
|--------|--------|
| 需求不清楚 | → [01-Requirement-Clarification](01-Requirement-Clarification/) |
| 不知道怎么写代码 | → [02-Feature-Implementation](02-Feature-Implementation/) |
| 代码有Bug | → [03-Bug-Reproduction-Root-Cause](03-Bug-Reproduction-Root-Cause/) |
| 需要重构代码 | → [04-Refactor-With-Behavior-Safety](04-Refactor-With-Behavior-Safety/) |
| 缺少单元测试 | → [05-Unit-Test-Generation](05-Unit-Test-Generation/) |
| 需要集成测试 | → [06-Integration-Test-Plan](06-Integration-Test-Plan/) |
| 需要Code Review | → [07-Code-Review-Assistant](07-Code-Review-Assistant/) |
| 需要系统设计 | → [08-Architecture-Decision-Draft](08-Architecture-Decision-Draft/) |
| 需要设计API | → [09-API-Contract-Design](09-API-Contract-Design/) |
| SQL太慢 | → [10-SQL-Query-Optimization](10-SQL-Query-Optimization/) |
| 有安全隐患 | → [11-Security-Review](11-Security-Review/) |
| 性能瓶颈 | → [12-Performance-Optimization](12-Performance-Optimization/) |
| 代码过时混乱 | → [13-Legacy-Code-Understanding](13-Legacy-Code-Understanding/) |
| 需要写文档 | → [14-Documentation-Generation](14-Documentation-Generation/) |

### 方式2：系统学习（1-2周）

**选择学习路径** → **按顺序学习任务** → **在实际工作中应用**

**路径A: 快速上手（初心者，1周）**
```
T01 → T02 → T05 → T07 → T03
需求 → 实现 → 单测 → 审查 → 调试
```

**路径B: 完整开发周期（标准流程，2周）**
```
T01 → T08 → T09 → T02 → T05 → T06 → T07 → T03 → T04 → T14
需求 → 架构 → API → 实现 → 单测 → 集测 → 审查 → 调试 → 重构 → 文档
```

**路径C: 质量与优化深化（进阶，2周）**
```
T11 → T12 → T10 → T04 → T13
安全 → 性能 → 查询 → 重构 → 遗留代码
```

详见 [使用说明.md](使用说明.md) 的完整学习路径。

---

## 💡 每个任务都包含

✅ **核心概念** - 为什么这个任务很重要
✅ **最佳实践** - 如何高效地完成这个任务
✅ **5-9个Prompt示例** - 真实场景的Prompt，可直接复制使用
✅ **常见误区** - 应该避免的做法
✅ **高级技巧** - 进阶的优化方法
✅ **检查清单** - 完成任务前的确认清单

---

## 🌟 项目特色

### 1️⃣ 任务驱动，符合实际工作流

- ✅ 按实际编程工作流组织（不是按主题）
- ✅ 14个任务覆盖从需求到交付的完整周期
- ✅ 每个任务都是独立完整的，也可以组合使用

### 2️⃣ 可直接使用的高质量Prompt

- ✅ 每个示例都经过实战验证
- ✅ 可直接复制到AI工具使用
- ✅ 预期输出清晰，结果可靠
- ✅ 包含完整的背景和约束说明

### 3️⃣ 最佳实践与常见误区

- ✅ 每个任务都列出"应该做"和"不应该做"
- ✅ 帮助你避免常见的低效做法
- ✅ 理解底层原理，提高工作效率

### 4️⃣ 循序渐进的学习路径

- ✅ 从初级到高级的任务分级
- ✅ 多条学习路径可选
- ✅ 既可以快速查阅，也可以系统学习

---

## 📚 额外资源

| 资源 | 说明 |
|------|------|
| [programmer_prompt_engineering_guide.md](programmer_prompt_engineering_guide.md) | 📚 程序员Prompt工程**完全指南**（深度学习资料） |
| [developer_prompt_engineering_guide.md](developer_prompt_engineering_guide.md) | 📚 开发者Prompt工程指南 |
| [CATALOG.md](CATALOG.md) | 📋 完整目录和详细说明 |
| [QUICK-REFERENCE.md](QUICK-REFERENCE.md) | ⚡ 快速参考和常用模板 |
| [使用说明.md](使用说明.md) | 🎓 学习路径和使用指南 |
| [项目完整导航.md](项目完整导航.md) | 🗺️ 详细统计和资源汇总 |

---

## 🎓 学习建议

### ✅ 建议1: 按问题学习（推荐）

遇到具体问题时：
1. 在上面的快速导航表中找到对应任务
2. 打开任务目录的README.md
3. 查看相关的Prompt示例
4. 复制、调整、使用

### ✅ 建议2: 系统学习（深度）

如果要系统学习Prompt工程：
1. 打开 [programmer_prompt_engineering_guide.md](programmer_prompt_engineering_guide.md)
2. 这是一份完整的Prompt工程指南，包含原理、框架、实战例子等
3. 配合14个任务的示例，可以全面掌握Prompt工程

### ✅ 建议3: 边学边用

最好的学习方式是在实际工作中应用：
1. 读一个Prompt示例
2. 用你自己的问题调整
3. 复制到AI工具中使用
4. 观察结果，记录心得

### ✅ 建议4: 团队协作

推荐做法：
1. Fork本项目或下载代码
2. 根据你的技术栈和工作流定制
3. 分享给团队成员
4. 一起积累团队特定的Prompt库

---

## 🔥 核心理念

> **好的Prompt应该像好的代码一样：清晰、具体、易维护。**

好的Prompt具有这些特征：
- ✅ **清晰** - 一眼看明白要做什么
- ✅ **具体** - 给出具体的上下文和约束
- ✅ **可复用** - 可以在不同场景中复用和调整
- ✅ **有效** - 能可靠地得到期望的结果

---

## 📊 项目统计

- **核心任务**: 14个
- **Prompt示例**: 70+个
- **详细说明**: 相当于200+页的技术文档
- **维护状态**: 🟢 主动维护中
- **最后更新**: 2026年3月

---

## 🤝 贡献

欢迎以下形式的贡献：
- 🐛 报告问题或Prompt不有效的情况
- 💡 建议新的Prompt或改进现有Prompt
- 📝 补充缺失的任务指南
- 🌍 翻译成其他语言

请直接提交Issue或Pull Request。

---

## 📄 许可证

本项目使用 [MIT License](LICENSE) 许可证。

---

## 💬 常见问题

**Q: 这些Prompt适用于所有AI模型吗？**
A: 核心思想通用，但具体Prompt可能需要微调。本指南基于Claude，但也适用于GPT系列。

**Q: 我可以将这个项目用于商业目的吗？**
A: 可以。本项目使用MIT许可证，允许商业使用和修改。

**Q: 有没有Prompt的版本更新？**
A: 会定期更新，包括新的示例、改进现有Prompt、补充缺失的任务。

**Q: 多久更新一次？**
A: 根据反馈和新的实践经验定期更新，预计每月至少一次。

---

## 🎯 下一步

**👉 [选择你的第一个任务](01-Requirement-Clarification/)** - 从需求澄清开始
**👉 [查看学习路径](使用说明.md)** - 找到适合你的学习方式
**👉 [打开完整指南](programmer_prompt_engineering_guide.md)** - 深度学习Prompt工程

---

**准备好提高编码效率了吗？立即选择一个任务开始！** 🚀

