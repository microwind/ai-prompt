# Prompt 框架：BROKE

## BROKE 框架概述

**BROKE** 是一个高效、易用的 Prompt 结构化框架，特别适合**代码生成和快速需求**场景。框架名称由五个核心要素组成：

- **B**ackground（背景）
- **R**ole（角色）
- **O**bjective（目标）
- **K**ey Constraints（约束）
- **E**xamples（示例）

BROKE 框架强调**简洁性和高效率**，是最容易学习和应用的 Prompt 框架。

---

## 特点

| 特点 | 说明 |
|------|------|
| **学习曲线** | 极低，5分钟掌握 |
| **适用场景** | 代码生成、功能实现、快速答疑 |
| **框架复杂度** | ⭐ 简洁（仅5个要素） |
| **有效性** | ⭐⭐⭐⭐⭐ 非常高 |
| **迭代性** | 中等（需要手动调整） |
| **个性化** | 通过 Examples 实现 |

### BROKE 的优势

✅ **快速上手** - 规则简单，无需专业背景
✅ **高效执行** - 直接得到结果，减少不必要的讨论
✅ **易于记忆** - 5个单词组成的框架，便于日常使用
✅ **结果稳定** - 明确的约束确保输出质量
✅ **广泛适用** - 适合 80% 的日常编程任务

### BROKE 的局限

❌ **缺乏迭代机制** - 不适合多轮对话的设计任务
❌ **灵活性有限** - 复杂场景可能需要额外补充
❌ **不强调探索** - 创意输出时可能显得呆板

---

## 模板

```text
[Role]
你是一名 [职位/身份]，拥有 [N年] 经验，精通 [相关技能]。

[Background]
项目背景：
- [项目名称/类型]
- [技术栈信息]
- [相关约束条件]

[Objective]
请 [明确的任务描述]。

[Key Constraints]
- [约束条件1]
- [约束条件2]
- [约束条件3]

[Examples]
输入示例：[具体的输入]
输出示例：[期望的输出]
```

---

## 相关框架比较

| 维度 | BROKE | CRISPE | ROBOTIC |
|------|-------|--------|---------|
| **框架大小** | 5 个要素 | 5 个要素 | 7 个要素 |
| **学习难度** | ⭐ 极简 | ⭐⭐ 中等 | ⭐⭐⭐ 较难 |
| **适用场景** | 代码生成 | 问题分析 | 架构设计 |
| **迭代能力** | 弱 | 中 | 强 |
| **个性化程度** | 中等 | 强 | 强 |
| **最佳实践** | 快速编码 | 深度思考 | 多轮评审 |

### 何时选择 BROKE？

✅ 你需要快速生成代码
✅ 需求明确、没有歧义
✅ 任务相对简单、规范化
✅ 不需要多轮交互和反馈
✅ 追求高效率而非完美

---

## 应用实践

### 实践1：生成 Spring Boot 登录接口

**问题描述**：需要快速生成一个基于 JWT 的登录接口

```text
[Role]
你是一名精通 Spring Boot 3 和安全认证的 Java 架构师。

[Background]
项目环境：
- Spring Boot 3.2
- Java 21
- MyBatis-Plus 数据库操作
- MySQL 8.0
- 使用 Lombok 简化代码

[Objective]
使用 JWT 生成一个登录接口，支持用户认证和 Token 生成。

[Key Constraints]
- 使用 Spring Security 6
- 密码使用 BCrypt 加密存储
- Token 有效期 24 小时
- 返回统一的 Result<T> 格式
- 包含全局异常处理
- 要求生产级代码质量

[Examples]
输入：POST /auth/login { username: "user1", password: "123456" }
输出：{ code: 200, data: { token: "eyJhbGc...", expiresIn: 86400 }, message: "登录成功" }
```

**预期输出**：完整的 Controller、Service、实体类和配置

---

### 实践2：数据库连接池配置

**问题描述**：为 Java 应用配置高性能的数据库连接池

```text
[Role]
你是一名资深的 Java 性能优化专家，熟悉数据库连接管理。

[Background]
应用场景：
- 高并发 Web 应用（QPS 5000+）
- 使用 Spring Boot
- MyBatis 作为 ORM 框架
- PostgreSQL 数据库

[Objective]
配置一个高效、稳定的数据库连接池。

[Key Constraints]
- 使用 HikariCP 连接池（开源标准）
- 最大连接数 50
- 最小空闲连接数 10
- 连接超时时间 30 秒
- 空闲连接超时时间 10 分钟
- 包含连接池监控和健康检查

[Examples]
输入：application.yml 配置文件模板
输出：完整的连接池配置和说明
```

**预期输出**：YAML 配置文件、监控类、以及性能调优建议

---

### 实践3：单元测试生成

**问题描述**：为 UserService 生成完整的单元测试

```text
[Role]
你是一名资深的 Java 测试工程师，精通 JUnit 5 和 Mockito。

[Background]
测试框架：
- JUnit 5
- Mockito 2.x
- AssertJ 断言库
- Spring Boot Test

[Objective]
为 UserService 的 createUser 和 getUserById 方法编写完整的单元测试。

[Key Constraints]
- 使用 @ExtendWith(MockitoExtension.class)
- 使用 Mockito 模拟数据库层
- 覆盖正常场景和异常场景
- 测试覆盖率 100%
- 每个测试方法独立，无依赖

[Examples]
方法签名：
- createUser(UserCreateRequest request) -> User
- getUserById(Long id) -> User

测试场景：
- createUser：正常创建、用户已存在、参数验证失败
- getUserById：用户存在、用户不存在
```

**预期输出**：完整的测试类，包含 setUp、多个测试方法和断言

---

## BROKE 框架最佳实践

### ✅ 做这些事

1. **明确技术栈版本**
   - 不要说"Java"，要说"Java 21"
   - 不要说"Spring Boot"，要说"Spring Boot 3.2"

2. **给出具体例子**
   - 输入输出示例胜过千言万语
   - 一个例子抵得上10句描述

3. **列出所有约束**
   - 格式约束（JSON、XML）
   - 性能约束（响应时间）
   - 安全约束（加密、认证）

4. **简明扼要**
   - 每个部分一句话总结
   - 不要写长篇幅的背景描述

### ❌ 避免这些事

1. **模糊的角色定义**
   - ❌ "你是一个专家"
   - ✅ "你是一名资深的 Java 并发编程专家，10年经验"

2. **隐含假设**
   - ❌ "生成登录代码"（假设 AI 知道你用什么框架）
   - ✅ "使用 Spring Boot 3.2、MyBatis-Plus 生成登录代码"

3. **模糊的约束**
   - ❌ "代码要好"
   - ✅ "使用 Lombok、包含 Javadoc、符合阿里编码规范"

4. **缺少示例**
   - ❌ 只给输入描述
   - ✅ 给出具体的输入输出例子

---

## 常见问题

**Q: BROKE 框架和其他框架有什么区别？**

A: BROKE 最简洁快速，适合直接出活。如果需要深度思考和多轮迭代，考虑 CRISPE 或 ROBOTIC。

**Q: 可以组合其他框架吗？**

A: 可以。BROKE 可以和 Chain-of-Thought 结合，要求 AI 先解释思路再生成代码。

**Q: 我的 Prompt 不工作怎么办？**

A: 检查 Background 和 Constraints 是否足够具体。大多数情况是上下文信息不足。

---

## 进一步阅读

- 📚 [深入理解 BROKE 框架原理](../programmer_prompt_engineering_guide.md#三broke-prompt-结构)
- 🎯 [BROKE vs CRISPE vs ROBOTIC](../programmer_prompt_engineering_guide.md#robotic-vs-broke-vs-crispe-对比)
- 💡 [Prompt 工程完全指南](../programmer_prompt_engineering_guide.md)
