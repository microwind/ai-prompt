# 📝 股市点评每日数据录入模板

> 用于每天在早盘、午盘、收盘三个时段快速整理结构化输入数据

---

## 📌 使用说明

建议每天按 3 个时段分别复制下面的模板，填完后直接交给：

- [05-final-prompts.md](./05-final-prompts.md) 里的对应 Prompt
- 或 [a-share-market-commentary/SKILL.md](./a-share-market-commentary/SKILL.md) 对应的 skill

这样可以保证每天输入结构稳定，输出口径一致。

---

## 1. 早盘数据模板

```json
{
  "session_type": "morning_open_30m",
  "trade_date": "YYYY-MM-DD",
  "weekday": "周X",
  "index_summary": {
    "shanghai_composite": "",
    "shenzhen_component": "",
    "chinext": "",
    "star50": ""
  },
  "turnover": {
    "market_total": "",
    "estimated_total": ""
  },
  "advancers_decliners": {
    "up_count": "",
    "down_count": "",
    "limit_up_count": "",
    "limit_down_count": ""
  },
  "hot_sectors": [],
  "weak_sectors": [],
  "main_themes": [],
  "divergent_themes": [],
  "leading_stocks": [],
  "weak_stocks": [],
  "capital_flow": {
    "northbound": "",
    "main_force": ""
  },
  "market_sentiment": "",
  "special_events": "",
  "extra_notes": ""
}
```

### 早盘填写建议

- `market_total`：写开盘后 30 分钟内两市成交额
- `estimated_total`：如有估算值可填写，没有可留空
- `hot_sectors`：只保留 3-5 个最有辨识度的热点
- `leading_stocks`：建议只写最有代表性的 3-5 只
- `extra_notes`：重点写“接下来还需观察什么”

---

## 2. 午盘数据模板

```json
{
  "session_type": "midday_close",
  "trade_date": "YYYY-MM-DD",
  "weekday": "周X",
  "index_summary": {
    "shanghai_composite": "",
    "shenzhen_component": "",
    "chinext": "",
    "star50": ""
  },
  "turnover": {
    "market_total": "",
    "estimated_total": ""
  },
  "advancers_decliners": {
    "up_count": "",
    "down_count": "",
    "limit_up_count": "",
    "limit_down_count": ""
  },
  "hot_sectors": [],
  "weak_sectors": [],
  "main_themes": [],
  "divergent_themes": [],
  "leading_stocks": [],
  "weak_stocks": [],
  "capital_flow": {
    "northbound": "",
    "main_force": ""
  },
  "market_sentiment": "",
  "special_events": "",
  "extra_notes": ""
}
```

### 午盘填写建议

- `market_total`：写半日成交额
- `main_themes`：写上午盘最明确的主线题材
- `divergent_themes`：写高位分化或冲高回落方向
- `market_sentiment`：建议用 `偏强 / 分化 / 偏弱 / 修复`
- `extra_notes`：重点写“午后最值得跟踪的 2-3 个点”

---

## 3. 收盘数据模板

```json
{
  "session_type": "market_close",
  "trade_date": "YYYY-MM-DD",
  "weekday": "周X",
  "index_summary": {
    "shanghai_composite": "",
    "shenzhen_component": "",
    "chinext": "",
    "star50": ""
  },
  "turnover": {
    "market_total": "",
    "estimated_total": ""
  },
  "advancers_decliners": {
    "up_count": "",
    "down_count": "",
    "limit_up_count": "",
    "limit_down_count": ""
  },
  "hot_sectors": [],
  "weak_sectors": [],
  "main_themes": [],
  "divergent_themes": [],
  "leading_stocks": [],
  "weak_stocks": [],
  "capital_flow": {
    "northbound": "",
    "main_force": ""
  },
  "market_sentiment": "",
  "special_events": "",
  "extra_notes": ""
}
```

### 收盘填写建议

- `market_total`：写全天两市成交额
- `main_themes`：写全天最强主线
- `divergent_themes`：写全天明显走弱或分化方向
- `capital_flow.northbound`：尽量填写全天净流入/净流出
- `extra_notes`：重点写“次日观察点”

---

## 4. 最小必填字段

如果你当天时间很紧，至少保证这些字段有值：

- `session_type`
- `trade_date`
- `index_summary.shanghai_composite`
- `index_summary.shenzhen_component`
- `index_summary.chinext`
- `turnover.market_total`
- `advancers_decliners.up_count`
- `advancers_decliners.down_count`
- `hot_sectors`
- `weak_sectors`

---

## 5. 人工核对清单

在把数据交给 Prompt 或 skill 之前，建议先人工核对：

1. 指数涨跌幅是否写反
2. 成交额单位是否统一
3. 板块名称是否规范
4. 个股名称是否准确
5. 时段类型是否与当前场景一致
