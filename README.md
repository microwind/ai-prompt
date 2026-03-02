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

| 任务ID | 任务名称 | 难度 | 何时使用 |
|--------|---------|------|---------|
| **T01** | **Requirement Clarification** | ⭐ | 项目启动、需求评审 |
| **T02** | **Feature Implementation** | ⭐⭐ | 日常编码、功能开发 |
| **T03** | **Bug Reproduction & Root Cause** | ⭐⭐ | 问题排查、性能诊断 |
| **T04** | **Refactor with Behavior Safety** | ⭐⭐⭐ | 代码改进、技术债处理 |
| **T05** | **Unit Test Generation** | ⭐⭐ | 测试补充、覆盖率提升 |
| **T06** | **Integration Test Plan** | ⭐⭐⭐ | 系统验证、上线前检验 |
| **T07** | **Code Review Assistant** | ⭐⭐ | PR审查、质量把控 |
| **T08** | **Architecture Decision Draft** | ⭐⭐⭐⭐ | 系统设计、技术选型 |
| **T09** | **API Contract Design** | ⭐⭐⭐ | 接口定义、模块设计 |
| **T10** | **SQL/Query Optimization** | ⭐⭐⭐ | 数据库优化、查询性能 |
| **T11** | **Security Review** | ⭐⭐⭐⭐ | 安全审查、漏洞检查 |
| **T12** | **Performance Optimization** | ⭐⭐⭐⭐ | 性能调优、资源优化 |
| **T13** | **Legacy Code Understanding** | ⭐⭐⭐ | 知识转移、技术债清理 |
| **T14** | **Documentation Generation** | ⭐⭐ | 文档生成、知识沉淀 |

---

## 📚 快速导航

### 🔴 我需要快速解决问题

打开对应的**Phase**文件夹，查看该阶段的README.md找到具体任务：

**常见问题快速跳转：**
- 需求不清楚？ → **[01-Phase-Planning](01-Phase-Planning/)** → 01-requirement-clarification
- 不知道怎么写代码？ → **[02-Phase-Development](02-Phase-Development/)** → 02-feature-implementation
- 代码有Bug？ → **[03-Phase-Quality](03-Phase-Quality/)** → 04-bug-diagnosis
- 代码质量差？ → **[03-Phase-Quality](03-Phase-Quality/)** → 03-code-review
- 缺少测试？ → **[03-Phase-Quality](03-Phase-Quality/)** → 01-unit-testing + 02-integration-testing
- 性能瓶颈？ → **[04-Phase-Optimization](04-Phase-Optimization/)** → 01-query-optimization + 02-performance-optimization
- 需要设计API？ → **[02-Phase-Development](02-Phase-Development/)** → 01-api-design
- 需要重构代码？ → **[02-Phase-Development](02-Phase-Development/)** → 03-refactoring-safely
- 代码过时混乱？ → **[04-Phase-Optimization](04-Phase-Optimization/)** → 04-legacy-code
- 安全隐患？ → **[04-Phase-Optimization](04-Phase-Optimization/)** → 03-security-review
- 需要写文档？ → **[05-Phase-Documentation](05-Phase-Documentation/)** → 01-documentation-generation

---

### 🟡 我想系统学习

选择适合你的学习路径：

**路径1: 快速上手（1-2周）**
```
T01 → T02 → T07 → T03 → T05
需求澄清 → 功能实现 → 代码审查 → Bug排查 → 单元测试
```

**路径2: 完整开发周期（1-2个月）**
```
T01 → T08 → T09 → T02 → T05 → T06 → T07 → T03 → T04 → T14
需求 → 架构 → API设计 → 实现 → 单测 → 集测 → 审查 → 调试 → 重构 → 文档
```

**路径3: 质量与优化深化**
```
T11 → T12 → T10 → T04 → T13
安全 → 性能 → 查询 → 重构 → 遗留代码
```

详见 **[使用说明.md](使用说明.md)** 中的完整学习路径指南。

---

## 📁 项目结构

项目按**5个开发阶段**组织，每个阶段包含若干相关任务。

```
ai-prompt/
├── README.md                                    ← 本文件
├── CATALOG.md                                   ← 详细任务目录
├── QUICK-REFERENCE.md                           ← 快速查询模板
├── 使用说明.md                                  ← 任务导航和学习路径
├── 项目完整导航.md                              ← 完整导航和统计
│
├── 📋 01-Phase-Planning/                        ← 阶段1：需求与规划
│   ├── README.md                                ← 阶段导航
│   ├── 01-requirement-clarification/            ← T01: 需求澄清
│   └── 02-architecture-decision/                ← T08: 架构决策
│
├── 💻 02-Phase-Development/                     ← 阶段2：设计与开发
│   ├── README.md                                ← 阶段导航
│   ├── 01-api-design/                           ← T09: API设计
│   ├── 02-feature-implementation/               ← T02: 功能实现
│   └── 03-refactoring-safely/                   ← T04: 安全重构
│
├── 🐛 03-Phase-Quality/                         ← 阶段3：测试与质量
│   ├── README.md                                ← 阶段导航
│   ├── 01-unit-testing/                         ← T05: 单元测试
│   ├── 02-integration-testing/                  ← T06: 集成测试
│   ├── 03-code-review/                          ← T07: 代码审查
│   └── 04-bug-diagnosis/                        ← T03: Bug诊断
│
├── 🚀 04-Phase-Optimization/                    ← 阶段4：优化与维护
│   ├── README.md                                ← 阶段导航
│   ├── 01-query-optimization/                   ← T10: 查询优化
│   ├── 02-performance-optimization/             ← T12: 性能优化
│   ├── 03-security-review/                      ← T11: 安全审查
│   └── 04-legacy-code/                          ← T13: 遗留代码
│
└── 📚 05-Phase-Documentation/                   ← 阶段5：文档与交付
    ├── README.md                                ← 阶段导航
    └── 01-documentation-generation/             ← T14: 文档生成
        ├── README.md                            ← 文档生成核心指南
        ├── programmer_prompt_engineering_guide.md ← 中高级程序员Prompt工程完全指南
        └── prompt_examples.md                   ← 14个真实场景的Prompt实践库
```

**项目完成度：** ✅ 14个任务的核心指南已完成 | ✨ 新增: Prompt工程完全指南 + 14个实践场景库

**快速导航：** 👉 [打开项目完整导航.md](项目完整导航.md) 查看详细统计和学习路径

---

## ✨ 每个任务都包含

- 📖 **核心概念** - 为什么这个任务很重要
- 🎯 **最佳实践** - 如何高效地完成这个任务
- 💡 **5-9个Prompt示例** - 真实场景的Prompt，可直接复制使用
- ❌ **常见误区** - 应该避免的做法
- 🚀 **高级技巧** - 进阶的优化方法

每个示例Prompt都包含：
- 具体的场景描述
- 完整的Prompt文本
- 预期的输出内容
- 适用场景说明
- 可改进的方向

---

## 🎓 学习建议

### ✅ 建议1: 不用全部读完

这不是一本书，而是**问题导向的工具书**：
- 遇到具体问题时，找对应的Phase和任务
- 查看该任务的README中的Prompt示例
- 需要深入学习Prompt工程？查看[Prompt工程完全指南](05-Phase-Documentation/01-documentation-generation/programmer_prompt_engineering_guide.md)
- 需要找真实场景的例子？查看[Prompt实践库](05-Phase-Documentation/01-documentation-generation/prompt_examples.md)
- 复制示例，根据你的情况调整

### ✅ 建议2: 边学边用

最好的学习方式是在实际工作中应用：
1. 读一个Prompt示例
2. 用你自己的问题调整
3. 复制到AI工具中使用
4. 观察结果，记录心得

### ✅ 建议3: 积累个人库

找到好用的Prompt时：
1. 复制到个人笔记或Wiki
2. 标注适用场景和效果
3. 逐步积累属于自己的Prompt库
4. 和团队分享优秀的Prompt

### ✅ 建议4: 针对团队定制

推荐做法：
1. 下载或Fork本项目
2. 根据你的技术栈调整Prompt
3. 添加团队特定的约定和规范
4. 作为新人培训和知识库

---

## 🔥 核心特色

### 1️⃣ 任务导向，而非主题导向

- ❌ 不是按"代码生成、代码解释、代码优化"这样的通用主题组织
- ✅ 而是按"T01需求澄清、T02功能实现、T07代码审查"这样的实际工作任务组织

这样的好处：
- 更符合实际的编程工作流
- 容易快速找到你需要的任务
- 理解每个任务之间的关系

### 2️⃣ 覆盖完整的开发生命周期

从**需求分析** → **架构设计** → **功能实现** → **质量保证** → **性能优化** → **知识沉淀**，全流程覆盖

### 3️⃣ 可直接使用的Prompt

不是讲理论，而是给出真实场景的Prompt：
- 可以直接复制使用
- 预期输出清晰
- 适用场景明确
- 包含完整示例

### 4️⃣ 最佳实践和常见误区

每个任务都列出：
- 该怎么做（最佳实践）
- 不该怎么做（常见误区）
- 为什么（理解底层原理）

---

## 📊 项目统计

- **核心任务**: 14个
- **完成任务**: 3个（T01, T02, T07）
- **Prompt示例**: 40+个
- **详细说明**: 相当于100+页的技术文档
- **维护状态**: 🟢 主动维护中

---

## 🌟 和其他Prompt指南的区别

| 特性 | 本项目 | 通用指南 |
|-----|--------|--------|
| **组织方式** | 任务导向 | 主题导向 |
| **覆盖范围** | 完整开发周期 | 通用编程技巧 |
| **使用场景** | 实战工作流 | 单点问题解决 |
| **学习模式** | 按工作流学 | 按兴趣学 |
| **示例数量** | 40+ | 少 |
| **深度** | 深（每个任务） | 浅（通用知识） |

---

## 🚀 立即开始

### 快速开始（5分钟）

1. **打开对应Phase文件夹** - 根据你的工作阶段选择，如`01-Phase-Planning/`
2. **查看README.md** - 了解该阶段的所有任务
3. **进入具体任务** - 如`01-requirement-clarification/`
4. **复制Prompt示例** - 查看README中的Prompt示例，复制到AI工具使用

### 系统学习（1-2周）

1. **选择学习路径** - 见[使用说明.md](使用说明.md)的学习路径
2. **按阶段学习** - 从01-Phase-Planning开始，按顺序学习5个阶段
3. **每个阶段15-30分钟** - 阅读README.md和任务README
4. **实践应用** - 在实际工作中使用学到的Prompt

---

## 📄 许可证

本项目使用 [MIT License](LICENSE) 许可证。

---

## 🤝 贡献

欢迎以下形式的贡献：
- 🐛 报告问题或Prompt不有效的情况
- 💡 建议新的Prompt或改进现有Prompt
- 📝 补充缺失的任务指南
- 🌍 翻译成其他语言

请直接提交Issue或Pull Request。

---

## 📚 相关资源

### Prompt Engineering最佳实践
- [Anthropic官方文档](https://docs.anthropic.com)
- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)

### 编程最佳实践
- 各语言官方编码规范
- 《Clean Code》《Code Complete》等经典著作

---

## 💬 常见问题

**Q: 这些Prompt适用于所有AI模型吗？**
A: 核心思想通用，但具体Prompt可能需要微调。本指南基于Claude，但也适用于GPT系列。

**Q: 我可以将这个项目用于商业目的吗？**
A: 可以。本项目使用MIT许可证，允许商业使用和修改。

**Q: 有没有Prompt的版本更新？**
A: 会定期更新，包括新的示例、改进现有Prompt、补充缺失的任务。

---

## 🎯 核心理念

> **好的Prompt应该像好的代码一样：清晰、具体、易维护。**

好的Prompt具有这些特征：
- ✅ **清晰** - 一眼看明白要做什么
- ✅ **具体** - 给出具体的上下文和约束
- ✅ **可复用** - 可以在不同场景中复用和调整
- ✅ **有效** - 能可靠地得到期望的结果

---

**准备好了吗？**

👉 **打开[项目完整导航.md](项目完整导航.md)** - 查看完整导航和统计
👉 **打开[01-Phase-Planning](01-Phase-Planning/)** - 从需求规划阶段开始
👉 **打开[02-Phase-Development](02-Phase-Development/)** - 学习设计与开发阶段

