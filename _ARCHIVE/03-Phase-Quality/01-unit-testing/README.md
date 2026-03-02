# T05: Unit Test Generation（单元测试生成）

> ⭐⭐ 初中级 | 编写高质量的单元测试，提升代码可靠性

## 核心概念

好的单元测试应该：
1. **独立** - 不依赖其他测试或外部资源
2. **清晰** - 一眼看出测试什么和期望什么
3. **快速** - 毫秒级执行
4. **确定性** - 总是相同的结果
5. **有目的** - 验证特定的行为

测试的金字塔：
- **单元测试** (70%) - 最快、最便宜、最细粒度
- **集成测试** (20%) - 中等速度和成本
- **端到端测试** (10%) - 最慢、最贵、最高层次

## 最佳实践

🎯 **原则1: 遵循AAA模式**
- **Arrange** - 准备测试数据和环境
- **Act** - 执行要测试的代码
- **Assert** - 验证结果

🎯 **原则2: 一个测试只验证一件事**
- ❌ 差: test_user_creation_and_email_sending
- ✅ 好: test_user_creation_returns_user_id

🎯 **原则3: 使用有意义的测试名称**
- ❌ 差: test1, testEdgeCase, testValid
- ✅ 好: test_login_with_invalid_email_should_throw_exception

🎯 **原则4: 充分覆盖边界情况**
- 空值、零值、负数
- 最大值、最小值、边界值
- 特殊字符、超长输入
- 异常和错误条件

---

## 单元测试框架对比

| 框架 | 语言 | 特点 |
|-----|------|------|
| **JUnit** | Java | 最流行，生态成熟 |
| **pytest** | Python | 简洁语法，灵活 |
| **Jest** | JavaScript | 内置mocking，快速 |
| **RSpec** | Ruby | BDD风格，表达力强 |
| **NUnit** | C# | .NET标准，功能完整 |

---

## 常见的单元测试模式

### 模式1: 基础单元测试

**Prompt:**
```
为这个函数编写完整的单元测试。

函数：
```python
def calculate_discount(price, customer_type):
    if customer_type == 'VIP':
        return price * 0.8
    elif customer_type == 'regular':
        return price * 0.9
    else:
        return price
```

要求：
1. 使用pytest框架
2. 覆盖所有分支（VIP、regular、其他）
3. 覆盖边界情况（0、负数、大数)
4. 每个测试函数名称清晰
5. 包含参数化测试（多个输入）

生成：
1. 完整的测试代码
2. 测试覆盖率应该100%
```

### 模式2: Mock和Stub

**Prompt:**
```
为这个有外部依赖的函数编写单元测试。

函数：
```java
public class OrderService {
    private PaymentGateway paymentGateway;
    private EmailService emailService;

    public boolean processOrder(Order order) {
        if (!paymentGateway.charge(order.getAmount())) {
            return false;
        }
        emailService.sendConfirmation(order.getEmail());
        return true;
    }
}
```

要求：
1. Mock PaymentGateway和EmailService
2. 覆盖成功和失败的场景
3. 验证emailService.sendConfirmation被调用了一次
4. 验证在支付失败时不发送邮件

使用[Mockito/其他mocking库]实现。
```

### 模式3: 异常测试

**Prompt:**
```
为这些可能抛出异常的方法编写测试。

函数：
```python
def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero")
    return a / b
```

要求：
1. 测试正常情况（b != 0）
2. 测试异常情况（b == 0），验证是否抛出ValueError
3. 验证异常消息内容
4. 测试其他边界情况

使用pytest的pytest.raises()。
```

---

## 测试覆盖率指南

| 覆盖率 | 评估 | 建议 |
|--------|------|------|
| **< 50%** | 很差 | 紧急增加测试 |
| **50-70%** | 差 | 需要大幅增加 |
| **70-80%** | 还可以 | 继续改进 |
| **80-90%** | 良好 | 保持这个水平 |
| **> 90%** | 优秀 | 少数业务代码需要这样 |

关键点：
- 关注代码覆盖率，但不是终极目标
- 更重要的是测试的质量
- 某些代码（如UI、简单getters）可以不测试

---

## 🎓 下一步

- 添加集成测试 → **T06: Integration Testing**
- 测试失败后调试 → **T03: Bug Diagnosis**
- 重构测试代码 → **T04: Refactoring**
