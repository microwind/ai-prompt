# T07: Code Review Assistant（代码审查）

> ⭐⭐ 初中级 | 保证代码质量，传递最佳实践的最后防线

## 核心概念

代码审查是保证代码质量的关键。好的代码审查应该检查：
- **功能正确性**: 逻辑是否正确
- **代码风格**: 是否遵循规范
- **可维护性**: 代码是否易于理解和修改
- **性能**: 是否有明显的性能问题
- **安全**: 是否有安全漏洞
- **测试**: 是否有充分的测试
- **文档**: 是否清晰记录

代码审查的目标：
1. 找到bug和潜在问题
2. 确保代码质量
3. 分享知识和最佳实践
4. 提升整个团队的技术水平

## 最佳实践

🎯 **原则1: 给出建设性的反馈**
- ❌ 差: "这代码很糟糕"
- ✅ 好: "这个方法有点复杂，可以考虑提取出[具体建议]来简化"

🎯 **原则2: 关注重点**
- ❌ 差: "这个变量名不好、那个注释不够、这里空格多了..."
- ✅ 好: "关注逻辑正确性、性能、安全和可维护性，风格问题用lint工具自动化"

🎯 **原则3: 提供具体的改进建议**
- ❌ 差: "这里有bug"
- ✅ 好: "这里有race condition，建议加锁或使用原子操作"

🎯 **原则4: 承认好的实现**
- ❌ 差: 只找问题
- ✅ 好: "这个错误处理做得很好"、"这个性能优化很聪明"

---

## ✅ 优质Prompt示例

### 示例1: 功能正确性审查

**Prompt:**
```
请审查这段代码的功能正确性，检查是否有逻辑问题。

```java
public class BankAccount {
    private double balance = 0;

    public void withdraw(double amount) {
        if (balance >= amount) {
            balance -= amount;
            System.out.println("取出: " + amount);
        }
    }

    public void deposit(double amount) {
        balance += amount;
        System.out.println("存入: " + amount);
    }
}
```

这段代码要用于多线程环境，请检查：
1. 是否有并发问题？
2. 是否有数据一致性问题？
3. 是否有edge case没有处理？
4. 浮点数比较是否安全？
5. 如果操作失败，是否能回滚？

请给出具体的问题和修复方案。
```

**预期输出:**
- 并发问题的识别和解决方案
- Edge case分析
- 改进建议
- 改进的代码示例

---

### 示例2: 代码风格检查

**Prompt:**
```
请审查这段代码的风格和规范。

```python
def processdata(data_list):
    result=[]
    for i in data_list:
        if i>10:
            x=i*2
            result.append(x)
    return result
```

检查维度：
1. 命名约定（函数名、变量名是否清晰）
2. 格式化（缩进、空格、换行）
3. 文档（是否需要docstring）
4. 复杂度（函数功能是否单一）
5. Python风格（是否符合PEP8）

基于最佳实践，给出改进的版本。
```

---

### 示例3: 性能风险识别

**Prompt:**
```
请审查这段代码的性能问题。

```javascript
function findDuplicates(arr) {
    const result = [];
    for (let i = 0; i < arr.length; i++) {
        for (let j = i + 1; j < arr.length; j++) {
            if (arr[i] === arr[j] && !result.includes(arr[i])) {
                result.push(arr[i]);
            }
        }
    }
    return result;
}

// 使用：
const data = getMillionRecords(); // 100万条记录
const dupes = findDuplicates(data);
```

分析：
1. 时间复杂度是多少？如果数据增加10倍会怎样？
2. 空间复杂度？
3. 有没有更优的算法？
4. result.includes()的性能瓶颈？
5. 如何优化这个函数？

给出优化方案和改进代码。
```

---

### 示例4: 安全漏洞检测

**Prompt:**
```
请审查这段代码的安全问题。

```python
@app.route('/search')
def search():
    query = request.args.get('q')
    sql = f"SELECT * FROM products WHERE name LIKE '{query}%'"
    results = db.execute(sql)
    return render_template('results.html', products=results)
```

安全检查清单：
1. SQL注入漏洞？怎么利用？怎么修复？
2. 输入验证？需要什么验证？
3. 输出转义？template是否安全？
4. 认证授权？是否需要权限检查？
5. 日志敏感信息？
6. 其他漏洞？

对于每个问题，给出具体的攻击方式和防护方案。
```

---

### 示例5: 可维护性评估

**Prompt:**
```
请评估这个函数的可维护性。

```javascript
function calc(o) {
    let r = 0;
    for (let k in o) {
        if (o[k] > 0) {
            r += o[k] * 0.1;
        } else if (o[k] < 0) {
            r += o[k] * 0.05;
        }
    }
    return r;
}
```

评估维度：
1. 命名清晰度：o、k、r都是什么意思？
2. 业务逻辑清晰度：这个函数做什么？
3. 可扩展性：如果规则变化怎么办？
4. 可测试性：如何单元测试？
5. 文档缺陷：需要什么文档？

给出改进的版本。
```

---

### 示例6: 测试充分性评价

**Prompt:**
```
请评估这个代码的测试覆盖。

```python
def is_valid_email(email):
    if '@' not in email:
        return False
    if '.' not in email.split('@')[1]:
        return False
    return True

# 现有测试
def test_valid_email():
    assert is_valid_email('user@example.com') == True

def test_invalid_email():
    assert is_valid_email('user.example.com') == False
```

分析：
1. 现有测试覆盖了哪些case？
2. 缺少了哪些重要的edge case？
   - 空字符串
   - 多个@符号
   - @在最后
   - 特殊字符
   - 非常长的邮箱
   - 其他？

列出所有缺失的测试用例和测试代码。
```

---

### 示例7: 架构合理性审视

**Prompt:**
```
请审查这个系统架构的合理性。

架构描述：
- Frontend (React) → Backend API → Database

详细：
```
Web服务器（Node.js）
  ├── 用户API: /api/users
  ├── 订单API: /api/orders
  ├── 支付: 直接调用Stripe API
  ├── 邮件: 同步调用邮件服务
  └── 报表: 在API中做复杂计算

数据库：
  └── PostgreSQL (单点)
```

审查问题：
1. 支付和邮件为什么是同步的？应该异步吗？
2. 报表计算在API中做，会不会成为瓶颈？
3. 数据库单点故障？
4. 不同模块紧耦合吗？
5. 如何扩展？
6. 缺少什么组件？
   - 缓存？
   - 消息队列？
   - 日志聚合？

给出改进的架构建议。
```

---

### 示例8: 技术债评估

**Prompt:**
```
请评估这段代码的技术债。

```python
# TODO: 这个太慢了，以后优化
def get_recommendations(user_id):
    user = User.query.get(user_id)
    recommendations = []
    for product in Product.query.all():  # 查询所有产品！
        if user.interests.contains(product.category):
            recommendations.append(product)
    return recommendations

# FIXME: 这里偶尔会crash
def process_payment(order):
    try:
        stripe_response = stripe.charge(order.amount)
        order.status = 'paid'
        db.commit()
    except:
        pass  # 忽略所有异常
```

分析：
1. 每个TODO/FIXME的优先级？
2. 这些技术债的影响？
3. 修复需要多久？
4. 如何制定修复计划？
5. 有没有其他隐藏的技术债？

给出优先级排序和修复建议。
```

---

## ❌ 常见误区

### 误区1: 审查过于严格

❌ 不要：
```
挑剔每一个细节：
- 变量名不喜欢
- 注释多了
- 空格位置不对
```

✅ 应该：
```
关注重要的问题：
- 功能正确性
- 性能
- 安全
- 可维护性
让工具处理代码风格问题
```

### 误区2: 无建设性的反馈

❌ 不要：
```
"这个方法太复杂了"
[不说为什么也不说怎么改]
```

✅ 应该：
```
"这个方法有10个判断分支，推荐：
1. 使用多态替换if-else
2. 提取出helper方法
3. 这样圈复杂度可以降到5"
```

---

## 高级技巧

### 技巧1: 整体性评估

```
不要一行一行评论，而是整体评估：

Prompt:
"请先给这段代码的总体评分：
- 功能正确性: /10
- 代码风格: /10
- 性能: /10
- 可维护性: /10
- 安全性: /10

然后列出TOP 3最重要的问题和改进建议"
```

### 技巧2: 对标最佳实践

```
参考行业最佳实践：

Prompt:
"请根据Google Python Style Guide审查这段代码的风格，
并根据OWASP审查安全问题"
```

### 技巧3: 检查清单式审查

```
使用标准化的检查清单：

Prompt:
"请按以下清单审查代码：
□ 功能正确（没有逻辑bug）
□ 错误处理（所有异常都处理了）
□ 性能（符合性能要求）
□ 安全（没有已知漏洞）
□ 可读性（变量和函数名清晰）
□ 测试（有充分的单元测试）
□ 文档（有必要的注释）
□ 兼容性（没有破坏现有接口）
"
```

---

## 📌 代码审查检查清单

- [ ] 功能正确性（符合需求，没有逻辑bug）
- [ ] 边界条件（null/empty/overflow等处理）
- [ ] 错误处理（异常都被捕获和处理）
- [ ] 性能（没有明显的性能问题）
- [ ] 安全（没有注入、XSS等漏洞）
- [ ] 代码风格（遵循团队约定）
- [ ] 可维护性（易于理解和修改）
- [ ] 可测试性（有充分的单元测试）
- [ ] 文档（注释和文档完整）
- [ ] 向后兼容（没有破坏现有功能）

---

## 🎓 下一步

- 如果发现bug → **T03: Bug Diagnosis**
- 如果需要重构 → **T04: Refactoring**
- 如果要补充测试 → **T05: Unit Testing**
