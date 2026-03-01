# 05 调试与问题排查

> 初中级 ⭐⭐ | 适合解决bug和追踪问题根源

## 核心概念

有效的调试Prompt需要：
- **提供完整的错误信息**: 包括堆栈跟踪、日志输出
- **说明重现步骤**: AI需要理解如何触发问题
- **明确预期行为**: 什么是正常的，什么是错误的
- **给出你已尝试**: 说明你做过什么诊断
- **提供上下文环境**: 操作系统、软件版本等

## 最佳实践

🎯 **原则1: 完整的错误信息**
- ❌ 差: "我的代码不工作"
- ✅ 好: "运行时得到 AttributeError: 'NoneType' object has no attribute 'split'"

🎯 **原则2: 清晰的重现步骤**
- ❌ 差: "有时候会崩溃"
- ✅ 好: "每次上传大于100MB的文件都会卡住"

🎯 **原则3: 上下文信息**
- ❌ 差: "连接超时了"
- ✅ 好: "在Python 3.9 + Django 3.2 + PostgreSQL环境中，某些特定查询会超时"

🎯 **原则4: 你的诊断过程**
- ❌ 差: "请帮我找bug"
- ✅ 好: "我已经检查了输入数据（都有效），也加了日志发现变量X在第3行是正确的，但到第8行变成None了"

---

## ✅ 优质Prompt示例

### 示例1: 异常堆栈跟踪

**Prompt:**
```
我的Python Flask应用报错了，帮我诊断：

错误信息：
```
Traceback (most recent call last):
  File "app.py", line 45, in create_user
    user = User.query.filter_by(email=email).first()
  File "sqlalchemy/orm/query.py", line 127, in filter_by
    return self.filter(kwargs_to_columns(**kwargs))
KeyError: 'email'
```

背景信息：
- 使用Flask + SQLAlchemy
- User模型有email字段
- 在创建新用户时出现问题
- 其他查询都正常

相关代码：
```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    name = db.Column(db.String(100))

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()
    ...
```

问题：
1. 这个错误的根本原因是什么？
2. 为什么email字段找不到？
3. 如何修复？
```

**预期输出:**
- 错误的根本原因分析
- 为什么会发生的原因
- 具体的修复方案
- 预防类似问题的方法

**适用场景:** 生产环境bug修复、框架集成问题、数据库异常

---

### 示例2: 性能瓶颈诊断

**Prompt:**
```
我的Node.js API响应特别慢，请帮我诊断性能问题。

症状：
- 简单请求需要2-3秒才能响应
- 有时超时（timeout 5s）
- 其他端点很快，只有用户列表端点慢

相关代码：
```javascript
app.get('/api/users', async (req, res) => {
  const users = await User.find({});
  const enriched = await Promise.all(
    users.map(user => enrichUser(user))
  );
  res.json(enriched);
});

async function enrichUser(user) {
  user.posts = await Post.find({ userId: user._id });
  user.friends = await User.find({ id: { $in: user.friendIds } });
  user.stats = await UserStats.findOne({ userId: user._id });
  return user;
}
```

我已经：
- 检查了数据库连接（速度正常）
- 确认User集合有2000条记录
- 在MongoDB看过查询速度（单个查询很快）

我的假设：可能是N+1问题？
```

**预期输出:**
- 问题诊断：确认N+1查询问题
- 性能分析：解释为什么慢
- 优化方案：如何改进
- 预期效果：优化后的性能

**适用场景:** API性能问题、数据库查询优化、并发问题诊断

---

### 示例3: 内存泄漏追踪

**Prompt:**
```
我的Java应用慢慢吃掉系统内存，请帮我追踪内存泄漏。

现象：
- 应用启动时内存占用500MB
- 运行24小时后上升到3GB
- 即使停止处理新请求内存也不释放

我已尝试：
- 调用 System.gc() （没有帮助）
- 检查日志（没有报错）
- 重启应用（内存重置，说明是泄漏不是无限增长的集合）

代码片段（可能有问题的部分）：
```java
private static Map<String, CachedData> cache = new HashMap<>();

public void processRequest(Request req) {
  String key = req.getId();
  CachedData data = new CachedData(req);
  cache.put(key, data);  // 永远不删除？

  executor.submit(() -> {
    Thread.sleep(1000);
    // 处理data...
  });
}
```

环境：Java 11, Tomcat 9
```

**预期输出:**
- 内存泄漏的根本原因
- 诊断步骤（如何用JVM工具确认）
- 具体修复方案
- 监控策略

**适用场景:** 内存泄漏追踪、资源管理、长运行程序优化

---

### 示例4: 并发问题诊断

**Prompt:**
```
我的Go程序在高并发时会报错，间歇性出现，难以重现。

错误：
- 有时候看到 "concurrent map write"
- 有时看到 "index out of range"
- 不是每次都出现，大约1%的概率

症状重现：
```bash
# 压力测试时出现
wrk -t 12 -c 400 -d 30s http://localhost:8080/api/data
```

可能的问题代码：
```go
var dataCache map[string][]Item

func handler(w http.ResponseWriter, r *http.Request) {
  id := r.URL.Query().Get("id")

  // 读取
  items := dataCache[id]

  // 异步更新
  go func() {
    newItems := fetchFromDB(id)
    dataCache[id] = newItems  // 竞态条件？
  }()

  w.Header().Set("Content-Type", "application/json")
  json.NewEncoder(w).Encode(items)
}
```

问题：
1. 这确实是竞态条件吗？
2. 如何安全地修复？
3. 应该用什么同步原语（mutex, channel, atomic）?
```

**预期输出:**
- 竞态条件的确认和解释
- 修复方案（使用哪种同步方式）
- 代码修改建议
- 测试和验证方法

**适用场景:** 并发编程问题、数据竞争、线程安全

---

## ❌ 常见误区

### 误区1: 错误信息不完整

❌ 不要：
```
"我的代码报错了"
[什么错误信息都不给]
```

✅ 应该：
```
"运行时得到以下错误：
[完整的错误堆栈跟踪]"
```

### 误区2: 没有重现步骤

❌ 不要：
```
"有时候不工作"
```

✅ 应该：
```
"用以下步骤可以重现：
1. 打开应用
2. 上传大于10MB的文件
3. 刷新页面
这时就会出现错误"
```

### 误区3: 隐藏关键信息

❌ 不要：
```
"我的数据库查询很慢"
[没有说用的什么数据库、什么版本]
```

✅ 应该：
```
"我在MongoDB 4.4上的查询很慢
查询语句：[query]
集合大小：[size]
没有建立索引"
```

### 误区4: 要求太宽泛

❌ 不要：
```
"请优化我的代码"
[整个项目源代码]
```

✅ 应该：
```
"请帮我优化这个特定的函数，
它处理10万条记录需要30秒，
我期望在5秒内完成

函数代码：[精确的函数]
"
```

---

## 高级技巧

### 技巧1: 用日志辅助诊断

```
添加诊断日志后的现象：
[粘贴相关日志行]

日志显示：
1. 变量X在这一步的值是...
2. 这表明...
3. 问题可能在...

这个诊断对吗？下一步应该怎么做？
```

### 技巧2: 二分查找缩小问题范围

```
我知道问题出在这个模块的某处：
[代码片段A]

我已经隔离出来：
- 去掉X部分：问题消失 →X相关
- 去掉Y部分：问题依然 →Y无关

下一步应该怎么调查？
```

### 技巧3: 要求诊断工具建议

```
我想追踪这个问题，但不知道用什么工具。

问题特征：
- 内存缓慢增长
- 发生在生产环境
- Python应用

建议：
1. 应该用什么工具？
2. 具体怎么用？
3. 如何解读结果？
```

### 技巧4: 预防性诊断

```
这段代码在高并发时会有问题吗？

[代码]

请列出：
1. 潜在的问题点
2. 每个问题的触发条件
3. 预防方法
```

---

## 📌 诊断检查清单

提交调试Prompt前，检查：
- [ ] 完整的错误堆栈跟踪或错误消息
- [ ] 重现步骤清晰明确
- [ ] 环境信息（语言版本、框架版本、OS）
- [ ] 相关代码片段（不是整个文件）
- [ ] 你已经尝试过的诊断步骤
- [ ] 预期行为 vs 实际行为
- [ ] 问题出现的频率（每次都有、间歇性等）

---

## 📖 下一步学习

完成本章后，你可以：
- ✅ 有效诊断和修复bug
- ✅ 快速定位问题根源
- ✅ 预防常见问题

准备进阶？查看 **08 设计模式应用** 来从架构层面解决问题！
