# T10: SQL/Query Optimization（数据库查询优化）

> ⭐⭐⭐ 中级 | 优化数据库查询性能，提升系统吞吐量

## 核心概念

查询优化的三个层次：
1. **查询逻辑** - SQL怎样写更高效
2. **索引策略** - 哪些字段建索引
3. **架构设计** - 表设计、分库分表等

优化的目标：
- 减少扫描的行数
- 减少网络传输数据
- 减少内存占用
- 降低CPU使用

## 最佳实践

🎯 **原则1: 分析执行计划**
- 使用EXPLAIN查看执行计划
- 关注扫描行数和扫描方式
- 避免全表扫描

🎯 **原则2: 建立合适的索引**
- 条件列、JOIN列、ORDER BY列要建索引
- 但不是索引越多越好
- 避免冗余索引
- 定期分析索引使用情况

🎯 **原则3: 简化查询**
- 不查用不到的列
- 减少JOIN的表数
- 避免子查询，改用JOIN
- 避免使用函数在WHERE条件中

🎯 **原则4: 数据库特定优化**
- MySQL：使用LIMIT优化
- PostgreSQL：使用ANALYZE
- Oracle：使用Hints
- MongoDB：使用projection

---

## 常见优化场景

### 场景1: 慢查询分析

**Prompt:**
```
这个查询很慢，请帮我优化。

查询：
```sql
SELECT u.id, u.name, COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE u.created_at > '2024-01-01'
GROUP BY u.id, u.name
ORDER BY order_count DESC
LIMIT 100
```

执行计划：
[粘贴EXPLAIN输出]

现象：
- 执行时间：[多久]
- 目标：[期望时间]
- 数据规模：[表行数]

问题：
1. 为什么这个查询这么慢？
2. 应该建什么索引？
3. 怎样改写查询？
4. 有没有架构上的优化？
```

### 场景2: 索引设计

**Prompt:**
```
为我的应用设计索引策略。

常见查询：
1. SELECT * FROM users WHERE email = ?
2. SELECT * FROM users WHERE status = ? ORDER BY created_at DESC
3. SELECT * FROM orders WHERE user_id = ? AND created_at > ?

表结构：
[表定义]

当前索引：
[已有的索引]

问题：
1. 现有索引是否够用？
2. 需要新增什么索引？
3. 有没有冗余索引？
4. 索引对INSERT/UPDATE性能的影响？
```

### 场景3: N+1查询问题

**Prompt:**
```
我的应用有N+1查询问题。

代码：
```python
users = User.query.all()  # 1次查询
for user in users:
    posts = Post.query.filter_by(user_id=user.id).all()  # N次查询
    print(user.name, len(posts))
```

问题：
1. 这个代码怎样优化？
2. 用JOIN还是eager loading？
3. 如何在[ORM框架]中实现？
4. 性能提升有多大？
```

---

## 数据库优化工具

| 工具 | 用途 | 特点 |
|-----|------|------|
| **EXPLAIN** | 查看执行计划 | 内置命令 |
| **pt-query-digest** | 分析慢查询日志 | 好用强大 |
| **SolarWinds DPA** | 数据库性能分析 | 专业工具 |
| **New Relic** | APM和监控 | 端到端视图 |

---

## 🎓 下一步

- 整体性能问题 → **T12: Performance Optimization**
- 查询优化代码审查 → **T07: Code Review**
