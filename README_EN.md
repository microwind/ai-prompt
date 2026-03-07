# Programmer's Essential Guide to Prompt Engineering

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Last Updated](https://img.shields.io/badge/Last%20Updated-2026%2F03-blue)
![Status](https://img.shields.io/badge/Status-Active-success)
![Tasks](https://img.shields.io/badge/Tasks-14-blue)

> **14 Real-World Programming Tasks with AI Collaboration Guide** | From requirement clarification to documentation generation, covering the entire software development lifecycle

---

## 📖 Project Introduction

This is a **practical Prompt Engineering guide** organized around 14 core programming tasks, helping you collaborate more efficiently with AI (Claude, GPT, etc.) in your daily work.

**What makes this different from other Prompt guides:**
- 🎯 **Task-Driven** - Organized around actual programming workflows
- 💼 **Production-Focused** - Each task comes from real programming scenarios
- 📋 **Complete Coverage** - Full chain from requirements analysis to project delivery
- ✅ **Ready to Use** - Prompts can be copied directly without modification

**Suitable for developers:**
- 🎓 **Beginners** - Quickly learn standard programming workflows
- 👨‍💻 **Intermediate Developers** - Improve coding efficiency and code quality
- 🏗️ **Architects** - Optimize system design and decision making
- 🚀 **Tech Leads** - Guide teams to use AI tools effectively

---

## 🎯 14 Core Tasks Overview

### Organized by Difficulty

#### ⭐ Beginner Tasks (Entry Level)
| Task | Name | When to Use |
|------|------|--------|
| **T01** | **Requirement Clarification** | Project kickoff, requirement review |
| **T02** | **Feature Implementation** | Daily coding, feature development |
| **T03** | **Bug Reproduction & Root Cause** | Issue diagnosis, performance diagnosis |
| **T05** | **Unit Test Generation** | Test coverage, coverage improvement |
| **T07** | **Code Review Assistant** | PR review, quality control |
| **T14** | **Documentation Generation** | Documentation creation, knowledge consolidation |

#### ⭐⭐ Intermediate Tasks (Advanced Knowledge Required)
| Task | Name | When to Use |
|------|------|--------|
| **T04** | **Refactor with Behavior Safety** | Code improvement, technical debt handling |
| **T06** | **Integration Test Plan** | System verification, pre-launch checks |
| **T09** | **API Contract Design** | Interface definition, module design |
| **T10** | **SQL/Query Optimization** | Database optimization, query performance |
| **T13** | **Legacy Code Understanding** | Knowledge transfer, technical debt cleanup |

#### ⭐⭐⭐ Advanced Tasks (Professional Experience Required)
| Task | Name | When to Use |
|------|------|--------|
| **T08** | **Architecture Decision Draft** | System design, technology selection |
| **T11** | **Security Review** | Security audit, vulnerability checks |
| **T12** | **Performance Optimization** | Performance tuning, resource optimization |

---

## 📁 Project Structure

```
ai-prompt/
├── README.md                                    ← Quick navigation
├── README_EN.md                                 ← English version (this file)
├── CATALOG.md                                   ← Complete directory
├── QUICK-REFERENCE.md                           ← Quick reference templates
├── 使用说明.md                                  ← Learning path guide
├── 项目完整导航.md                              ← Detailed statistics
│
├── programmer_prompt_engineering_guide.md       ← 📚 Complete Prompt Engineering Guide
├── developer_prompt_engineering_guide.md        ← 📚 Developer's Prompt Engineering Guide
│
├── frameworks/                                  ← Prompt Framework Documentation
│   ├── BROKE.md                                ← BROKE Framework
│   ├── CRISPE.md                               ← CRISPE Framework
│   ├── ROBOTIC.md                              ← ROBOTIC Framework
│   ├── Chain-of-Thought.md                     ← Chain-of-Thought Framework
│   ├── CO-STAR.md                              ← CO-STAR Framework
│   ├── ICIO.md                                 ← ICIO Framework
│   └── RTF.md                                  ← RTF Framework
│
├── 01-Requirement-Clarification/                ← T01: Requirement Clarification ⭐
│   └── README.md
├── 02-Feature-Implementation/                   ← T02: Feature Implementation ⭐⭐
│   └── README.md
├── 03-Bug-Reproduction-Root-Cause/              ← T03: Bug Diagnosis ⭐⭐
│   ├── README.md
│   ├── checklist.md
│   └── examples.md
├── 04-Refactor-With-Behavior-Safety/            ← T04: Safe Refactoring ⭐⭐⭐
│   └── README.md
├── 05-Unit-Test-Generation/                     ← T05: Unit Testing ⭐
│   └── README.md
├── 06-Integration-Test-Plan/                    ← T06: Integration Testing ⭐⭐⭐
│   └── README.md
├── 07-Code-Review-Assistant/                    ← T07: Code Review ⭐
│   └── README.md
├── 08-Architecture-Decision-Draft/              ← T08: Architecture Design ⭐⭐⭐⭐
│   └── README.md
├── 09-API-Contract-Design/                      ← T09: API Design ⭐⭐⭐
│   └── README.md
├── 10-SQL-Query-Optimization/                   ← T10: Query Optimization ⭐⭐⭐
│   └── README.md
├── 11-Security-Review/                          ← T11: Security Review ⭐⭐⭐⭐
│   └── README.md
├── 12-Performance-Optimization/                 ← T12: Performance Optimization ⭐⭐⭐⭐
│   └── README.md
├── 13-Legacy-Code-Understanding/                ← T13: Legacy Code ⭐⭐⭐
│   └── README.md
└── 14-Documentation-Generation/                 ← T14: Documentation Generation ⭐
    ├── README.md
    └── prompt_examples.md
```

---

## 🚀 Quick Start

### Method 1: Find answers by problem (5 minutes)

**What problem did I encounter?** → **Open the corresponding task directory** → **Copy the Prompt**

| Common Problem | Corresponding Task |
|--------|--------|
| Requirements unclear | → [01-Requirement-Clarification](01-Requirement-Clarification/) |
| Don't know how to write code | → [02-Feature-Implementation](02-Feature-Implementation/) |
| Code has bugs | → [03-Bug-Reproduction-Root-Cause](03-Bug-Reproduction-Root-Cause/) |
| Need to refactor code | → [04-Refactor-With-Behavior-Safety](04-Refactor-With-Behavior-Safety/) |
| Missing unit tests | → [05-Unit-Test-Generation](05-Unit-Test-Generation/) |
| Need integration tests | → [06-Integration-Test-Plan](06-Integration-Test-Plan/) |
| Need code review | → [07-Code-Review-Assistant](07-Code-Review-Assistant/) |
| Need system design | → [08-Architecture-Decision-Draft](08-Architecture-Decision-Draft/) |
| Need to design API | → [09-API-Contract-Design](09-API-Contract-Design/) |
| SQL is too slow | → [10-SQL-Query-Optimization](10-SQL-Query-Optimization/) |
| Security concerns | → [11-Security-Review](11-Security-Review/) |
| Performance bottlenecks | → [12-Performance-Optimization](12-Performance-Optimization/) |
| Code is outdated and messy | → [13-Legacy-Code-Understanding](13-Legacy-Code-Understanding/) |
| Need to write documentation | → [14-Documentation-Generation](14-Documentation-Generation/) |

### Method 2: Systematic learning (1-2 weeks)

**Choose a learning path** → **Study tasks in order** → **Apply in real work**

**Path A: Quick Start (Beginners, 1 week)**
```
T01 → T02 → T05 → T07 → T03
Requirements → Implementation → Unit Tests → Code Review → Debugging
```

**Path B: Complete Development Cycle (Standard workflow, 2 weeks)**
```
T01 → T08 → T09 → T02 → T05 → T06 → T07 → T03 → T04 → T14
Requirements → Architecture → API → Implementation → Unit Tests → Integration Tests → Code Review → Debugging → Refactor → Documentation
```

**Path C: Quality & Performance (Advanced, 2 weeks)**
```
T11 → T12 → T10 → T04 → T13
Security → Performance → Queries → Refactor → Legacy Code
```

See [使用说明.md](使用说明.md) for complete learning paths.

---

## 💡 Each task includes

✅ **Core Concepts** - Why this task matters
✅ **Best Practices** - How to complete efficiently
✅ **5-9 Prompt Examples** - Real-world Prompts ready to copy
✅ **Common Mistakes** - What to avoid
✅ **Advanced Tips** - Optimization techniques
✅ **Checklists** - Verification before completion

---

## 🎨 Prompt Frameworks Comparison & Application

This project provides **7 Prompt frameworks** to help you choose the best one for different scenarios.

### Framework Overview

| Framework | Use Case | Complexity | Documentation |
|-----------|----------|-----------|----------------|
| **BROKE** | Fast code generation, standard requirements | ⭐ Simple | [📖 BROKE Framework](frameworks/BROKE.md) |
| **CRISPE** | Complex problem analysis, creative output | ⭐⭐ Medium | [📖 CRISPE Framework](frameworks/CRISPE.md) |
| **ROBOTIC** | Architecture design, iterative feedback | ⭐⭐⭐ Complex | [📖 ROBOTIC Framework](frameworks/ROBOTIC.md) |
| **Chain-of-Thought** | Algorithm design, logical reasoning | ⭐⭐ Medium | [📖 Chain-of-Thought Framework](frameworks/Chain-of-Thought.md) |
| **CO-STAR** | Content creation, marketing copy | ⭐⭐⭐ Complex | [📖 CO-STAR Framework](frameworks/CO-STAR.md) |
| **ICIO** | Iterative problem solving | ⭐⭐ Medium | [📖 ICIO Framework](frameworks/ICIO.md) |
| **RTF** | Role playing, scenario simulation | ⭐ Simple | [📖 RTF Framework](frameworks/RTF.md) |

### Framework Quick Reference

**Choose your framework by task type:**

```
Task Type                        → Best Framework
─────────────────────────────────────────────────
Write code, generate functions   → BROKE
Optimize queries, analyze performance → CRISPE
Design architecture              → ROBOTIC
Write algorithms, logical reasoning → Chain-of-Thought
Write marketing copy, creative   → CO-STAR
Problem solving, step by step    → ICIO
Role playing, scenario simulation → RTF
```

---

## 🌟 Project Features

### 1️⃣ Task-Driven, Real Workflow Alignment

- ✅ Organized around actual programming workflows
- ✅ 14 tasks cover complete cycle from requirements to delivery
- ✅ Each task is independent yet can be combined

### 2️⃣ High-Quality, Production-Ready Prompts

- ✅ Every example has been battle-tested
- ✅ Copy and use directly in AI tools
- ✅ Clear expected outputs, reliable results
- ✅ Complete background and constraints

### 3️⃣ Best Practices & Common Mistakes

- ✅ Each task lists "DO" and "DON'T"
- ✅ Avoid common inefficient practices
- ✅ Understand underlying principles, improve efficiency

### 4️⃣ Progressive Learning Paths

- ✅ Tasks graded from beginner to advanced
- ✅ Multiple learning paths available
- ✅ Quick lookup or systematic learning

---

## 📚 Additional Resources

| Resource | Description |
|----------|-------------|
| **[00-Prompt-Examples-Library](00-Prompt-Examples-Library/)** | 💡 **70+ real-world Prompt examples** (content generation, system design, data processing, code generation) |
| [programmer_prompt_engineering_guide.md](programmer_prompt_engineering_guide.md) | 📚 Complete Prompt Engineering **Complete Guide** (in-depth learning) |
| [developer_prompt_engineering_guide.md](developer_prompt_engineering_guide.md) | 📚 Developer's Prompt Engineering Guide |
| [CATALOG.md](CATALOG.md) | 📋 Complete directory and detailed descriptions |
| [QUICK-REFERENCE.md](QUICK-REFERENCE.md) | ⚡ Quick reference and common templates |
| [使用说明.md](使用说明.md) | 🎓 Learning paths and usage guide |
| [项目完整导航.md](项目完整导航.md) | 🗺️ Detailed statistics and resources |

---

## 🎓 Learning Recommendations

### ✅ Recommendation 1: Learn by Problem (Recommended)

When you encounter specific problems:
1. Find the corresponding task in the quick navigation table above
2. Open the README.md in that task directory
3. Review related Prompt examples
4. Copy, adjust, and use

### ✅ Recommendation 2: Systematic Learning (In-Depth)

For comprehensive Prompt engineering study:
1. Open [programmer_prompt_engineering_guide.md](programmer_prompt_engineering_guide.md)
2. This is a complete Prompt engineering guide with principles, frameworks, practical examples
3. Combined with 14 task examples, you can master Prompt engineering

### ✅ Recommendation 3: Learn by Doing

Best learning method is applying in real work:
1. Read a Prompt example
2. Adjust it with your own problem
3. Copy to AI tool and use
4. Observe results, record insights

### ✅ Recommendation 4: Team Collaboration

Recommended approach:
1. Fork this project or download the code
2. Customize based on your tech stack and workflow
3. Share with team members
4. Build team-specific Prompt library together

---

## 🔥 Core Philosophy

> **Good Prompts should be like good code: clear, specific, and maintainable.**

Good Prompts have these characteristics:
- ✅ **Clear** - Immediately understand what to do
- ✅ **Specific** - Provide specific context and constraints
- ✅ **Reusable** - Can be applied and adjusted in different scenarios
- ✅ **Effective** - Reliably achieve expected results

---

## 📊 Project Statistics

- **Core Tasks**: 14
- **Prompt Examples**: 70+
- **Prompt Frameworks**: 7 (BROKE, CRISPE, ROBOTIC, Chain-of-Thought, CO-STAR, ICIO, RTF)
- **Detailed Documentation**: Equivalent to 200+ pages of technical documentation
- **Maintenance Status**: 🟢 Actively maintained
- **Last Updated**: March 2026

---

## 🤝 Contributing

We welcome contributions in the following forms:
- 🐛 Report issues or ineffective Prompts
- 💡 Suggest new Prompts or improvements to existing ones
- 📝 Supplement missing task guides
- 🌍 Translate into other languages

Please submit Issues or Pull Requests directly.

---

## 📄 License

This project uses [MIT License](LICENSE).

---

## 💬 FAQ

**Q: Are these Prompts applicable to all AI models?**

A: Core ideas are universal, but specific Prompts may need adjustment. This guide is based on Claude but also works with GPT series.

**Q: Can I use this project for commercial purposes?**

A: Yes. This project uses MIT License, allowing commercial use and modification.

**Q: Will there be version updates for Prompts?**

A: Yes, regular updates with new examples, improvements to existing Prompts, and supplementary tasks.

**Q: How frequently is it updated?**

A: Updated regularly based on feedback and new practical experiences. Expected at least monthly.

---

## 🎯 Next Steps

**👉 [Choose your first task](01-Requirement-Clarification/)** - Start with requirement clarification
**👉 [View learning path](使用说明.md)** - Find the right approach for you
**👉 [Open complete guide](programmer_prompt_engineering_guide.md)** - Deep dive into Prompt engineering

---

**Ready to improve your coding efficiency? Pick a task and start now!** 🚀
