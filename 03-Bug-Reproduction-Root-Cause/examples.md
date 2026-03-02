# T03 实际Prompt示例库

## 示例1: 错误堆栈分析

**场景:** Java应用抛出NullPointerException，需要快速定位

**Prompt:**
```
我的Java应用抛出以下异常，请帮我诊断原因：

异常信息：
java.lang.NullPointerException: Cannot invoke method getName() on null object
    at com.example.UserService.getUserInfo(UserService.java:45)
    at com.example.UserController.getProfile(UserController.java:123)
    at java.base/java.lang.Thread.run(Thread.java:834)

代码片段：
```java
public class UserService {
    private UserRepository userRepo;

    public UserInfo getUserInfo(int userId) {
        User user = userRepo.findById(userId);  // Line 45
        return new UserInfo(user.getName(), user.getEmail());
    }
}
```

使用场景：用户点击查看个人资料时发生

问题分析：
1. 具体是哪一行代码有问题？
2. 为什么user对象会是null？
3. userRepo.findById返回null的可能原因有哪些？
4. 怎样修复这个问题？
5. 应该添加什么防御性检查？
```

**预期输出:**
- 问题定位：user对象未初始化
- 原因分析：findById没有找到记录
- 修复方案：添加null判断或使用Optional
- 防御建议：添加输入验证

---

## 示例2: 性能问题诊断

**场景:** API响应时间从200ms增加到5秒，需要定位瓶颈

**Prompt:**
```
我的API突然变慢了，性能从200ms恶化到5秒以上。

环境：
- 框架：Spring Boot 2.6
- 数据库：MySQL 5.7
- 并发：50用户
- 服务器：4核8G内存

现象：
- 所有API都变慢（不只是某一个）
- 重启应用后恢复正常
- 一段时间后又开始慢
- CPU和内存看起来正常

日志显示：
2024-03-01 10:30:00 [INFO] Received GET /api/users
2024-03-01 10:30:03 [INFO] Query database took 2800ms
2024-03-01 10:30:04 [INFO] Response sent

我已经检查过：
- 数据库连接是否有泄漏（看起来没有）
- SQL查询是否变慢（单独执行很快）
- JVM堆内存（使用率60%左右）

问题分析：
1. 这个现象最可能是什么原因？
2. 为什么重启后会恢复？
3. 应该如何进一步诊断？
4. 需要采集什么样的指标？
```

**预期输出:**
- 可能的原因排序（最可能→次要）
- 进一步诊断的具体步骤
- 需要添加的监控和日志
- 快速临时缓解方案
- 根本解决方案

---

## 示例3: 并发问题诊断

**场景:** 多用户并发操作导致数据不一致

**Prompt:**
```
我的系统在高并发下出现数据不一致的问题。

问题现象：
- 两个用户同时转账，余额计算不对
- 库存扣减出现负数
- 订单状态更新冲突

核心代码（Python）：
```python
def transfer(from_user_id, to_user_id, amount):
    # 检查余额
    from_user = User.query.get(from_user_id)
    if from_user.balance < amount:
        return False

    # 扣减转账用户余额
    from_user.balance -= amount
    db.session.commit()

    # 增加接收用户余额
    to_user = User.query.get(to_user_id)
    to_user.balance += amount
    db.session.commit()

    return True
```

压力测试：
- 1000个并发请求
- 结果：最终余额不对，数据库不一致

问题：
1. 这段代码的并发问题在哪里？
2. 两个commit之间发生了什么导致问题？
3. 如何修复（使用事务、锁、还是其他）？
4. 怎样验证修复后的并发安全性？
```

**预期输出:**
- 竞态条件的详细解释
- 可能的并发场景和后果
- 修复方案（带代码）
- 测试方法验证修复

---

## 示例4: 内存问题诊断

**场景:** Java应用内存使用不断增长，最终OutOfMemoryError

**Prompt:**
```
我的Java服务长时间运行后内存不断增长，最终OOM。

观测：
- 启动时内存使用：300MB
- 运行24小时后：3000MB
- 最终触发：java.lang.OutOfMemoryError: Java heap space

监控数据显示：
- Old Generation内存逐渐增长
- Minor GC频繁，效果不明显
- Full GC越来越频繁且耗时

应用信息：
- 使用了缓存（HashMap）
- 定时任务每分钟运行一次
- 连接池大小20

代码可能的问题点：
```java
private static Map<String, Object> cache = new HashMap<>();

public void processData() {
    for (Data data : dataList) {
        cache.put(data.id, data);  // 数据一直累积？
    }
}

public void onTaskComplete() {
    listeners.add(new Listener() { ... }); // 监听器是否泄漏？
}
```

问题：
1. 这个内存增长最可能的原因是什么？
2. 如何使用jmap、jhat分析堆快照？
3. 代码中哪些地方可能导致内存泄漏？
4. 如何修复和验证修复？
```

**预期输出:**
- 内存泄漏的位置和原因
- 诊断命令和分析方法
- 修复代码和改进建议
- 监控方案防止再发生

---

## 示例5: 网络问题诊断

**场景:** 调用第三方API经常超时和失败

**Prompt:**
```
我的应用调用第三方支付API时经常超时。

问题：
- 超时错误频率：5%-10%
- 超时时间设置：10秒
- 错误信息：SocketTimeoutException / ConnectTimeoutException

已观察：
- 第三方API状态页显示一切正常
- 直接curl访问API速度很快
- 但应用中调用经常超时

代码：
```python
import requests

def call_payment_api(order_id, amount):
    url = 'https://api.payment.com/charge'
    data = {'order_id': order_id, 'amount': amount}

    try:
        response = requests.post(url, json=data, timeout=10)
        return response.json()
    except requests.Timeout:
        log_error('Payment API timeout')
        return None
```

可能的原因：
- 网络延迟?
- DNS解析慢?
- SSL握手耗时?
- 应用机器性能不足?
- API限流?

问题分析：
1. 最可能的原因是什么？
2. 如何逐一排除这些可能性？
3. 需要采集什么样的诊断数据？
4. 短期缓解方案是什么？
5. 长期解决方案是什么？
```

**预期输出:**
- 诊断步骤和工具（curl、tcpdump、Wireshark）
- 各个可能性的排除方法
- 监控和告警方案
- 重试和降级策略

---

## 示例6: 数据库问题诊断

**场景:** 某个SQL查询特别慢，导致整个系统性能下降

**Prompt:**
```
这个查询非常慢（平时100ms，现在5秒以上）：

```sql
SELECT u.id, u.name, COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE u.created_at > '2024-01-01'
GROUP BY u.id, u.name
ORDER BY order_count DESC
LIMIT 100
```

背景：
- 表users：100万行
- 表orders：5000万行
- 数据库：MySQL 5.7
- 主从部署（读写分离）

现象：
- 这个查询在某些时段特别慢
- 其他查询正常
- 数据库CPU正常
- 磁盘I/O正常

已检查：
- users表上有created_at索引
- orders表上有user_id索引
- EXPLAIN PLAN看起来正常

问题：
1. 为什么这个查询会变慢？
2. EXPLAIN输出应该怎么看？
3. 应该如何优化这个查询？
4. 索引策略应该如何调整？
5. 有没有更高效的方式实现？
```

**预期输出:**
- 执行计划分析
- 可能的优化方向
- SQL改写建议
- 索引设计建议
- 数据库参数调优

---

## 示例7: 日志追踪诊断

**场景:** 用户报告某个功能不工作，需要从日志追踪

**Prompt:**
```
用户报告："提交订单失败"，但我们没有清晰的错误日志。

收集到的信息：
- 用户：user_123
- 时间：2024-03-01 14:30:00
- 行为：填写订单信息 → 点击确认 → 看到"操作失败"

当前日志：
```
2024-03-01T14:30:01.234 [INFO] OrderController.createOrder - Received request
2024-03-01T14:30:01.567 [INFO] OrderService.validate - Order validation passed
2024-03-01T14:30:02.890 [INFO] PaymentService.charge - Calling payment gateway
2024-03-01T14:30:05.123 [ERROR] OrderService.save - Save failed: Database error
2024-03-01T14:30:05.124 [ERROR] OrderController.createOrder - Exception: null
```

问题：
1. 日志中缺少哪些关键信息？
2. 为什么"Database error"不具体？
3. 应该在哪些地方添加更详细的日志？
4. 日志应该包含什么字段便于追踪？
5. 怎样快速定位这类问题？

请给出：
1. 改进后的日志代码
2. 日志框架配置建议
3. 日志规范（字段、格式、级别）
```

**预期输出:**
- 添加详细日志的代码
- 日志规范和最佳实践
- 日志追踪框架建议
- 日志分析和告警方案

