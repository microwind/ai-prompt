# 🧩 股市点评 Skill 模板

> 这是一份可直接复制改造的 skill 模板草案，你可以据此生成自己的 `SKILL.md`

---

## 📌 使用方式

如果你后续要把这个能力封装成真正的 skill，可以直接参考下面这份模板。

你可以：

1. 直接复制整份模板
2. 按你的数据字段做微调
3. 把它整理进目标 skill 目录的 `SKILL.md`

---

## ✅ `SKILL.md` 模板

```markdown
# A-Share Market Commentary

## Purpose

Generate structured A-share market commentary for three fixed trading sessions:

1. Within 30 minutes after market open
2. After midday close
3. After market close

This skill is for market observation and content generation. It is not for investment advice.

## When To Use

Use this skill when the user wants:

- a morning market opening commentary
- a midday market summary
- an end-of-day market review
- structured A-share market content based on supplied market data

Do not use this skill when:

- the input data is obviously incomplete and cannot support a factual summary
- the user asks for direct stock recommendations or trading advice
- the user asks for fabricated market interpretation without real data

## Required Inputs

- `session_type`
  - one of: `morning_open_30m`, `midday_close`, `market_close`
- `trade_date`
- `index_summary`
  - `shanghai_composite`
  - `shenzhen_component`
  - `chinext`
  - optional `star50`
- `turnover`
  - `market_total`
  - optional `estimated_total`
- `advancers_decliners`
  - `up_count`
  - `down_count`
  - optional `limit_up_count`
  - optional `limit_down_count`
- `hot_sectors`
- `weak_sectors`

## Optional Inputs

- `main_themes`
- `divergent_themes`
- `leading_stocks`
- `weak_stocks`
- `capital_flow`
- `market_sentiment`
- `extra_notes`
- `special_events`

## Output Goals

The output should:

- be factual and based on the provided inputs
- be concise, structured, and readable
- reflect the correct focus for the requested session
- avoid exaggerated or emotional language
- include a clear risk notice

## Session Logic

### `morning_open_30m`

Focus on:

- opening index behavior
- early market breadth
- first-wave sector rotation
- capital preference in the first 30 minutes
- what to watch next

### `midday_close`

Focus on:

- first-half session structure
- whether the morning theme is strengthening or diverging
- turnover and breadth by noon
- what to watch in the afternoon session

### `market_close`

Focus on:

- full-day market summary
- leading themes and weak themes
- capital flow and sentiment confirmation
- next-session watch points

## Writing Rules

- Never fabricate market facts
- Never provide direct buy/sell advice
- Never promise gains or market direction
- Never overstate sentiment using words like “must rise”, “explode”, “certainly”, or similar
- Use a professional, calm, and neutral tone
- Prefer synthesis over raw data dumping
- If input data is incomplete, say so cautiously and limit conclusions

## Output Structure

Always produce:

1. `title`
2. `one_line_summary`
3. `index_and_sentiment`
4. `hotspots_and_divergence`
5. `capital_and_stock_watch`
6. `next_watch_points`
7. `risk_notice`

The `risk_notice` must explicitly state:

`以上内容仅为市场盘面观察与信息整理，不构成任何投资建议。`

## Response Template

Title: {session-appropriate concise title}

一句话概览：
{brief summary}

指数与情绪：
{summary based on index, breadth, turnover, and mood}

热点与分化：
{summary based on sectors, themes, and structure}

资金与个股观察：
{summary based on capital flow and representative stocks}

后续观察点：
1. {watch point one}
2. {watch point two}
3. {watch point three if needed}

风险提示：
以上内容仅为市场盘面观察与信息整理，不构成任何投资建议。

## Invocation Guide

Before generating commentary:

1. confirm `session_type`
2. validate key data fields
3. identify whether data is enough for a factual summary
4. generate only session-relevant commentary
5. keep the final text concise

## Example Input

```json
{
  "session_type": "midday_close",
  "trade_date": "2026-04-01",
  "index_summary": {
    "shanghai_composite": "3358.21, +0.42%",
    "shenzhen_component": "10231.55, +0.68%",
    "chinext": "2012.43, +1.15%"
  },
  "turnover": {
    "market_total": "7865亿"
  },
  "advancers_decliners": {
    "up_count": 3521,
    "down_count": 1618,
    "limit_up_count": 62,
    "limit_down_count": 4
  },
  "hot_sectors": ["算力", "AI应用", "半导体"],
  "weak_sectors": ["煤炭", "银行"],
  "leading_stocks": ["示例A", "示例B"],
  "capital_flow": {
    "northbound": "净流入23.5亿"
  },
  "market_sentiment": "偏强"
}
```
```

---

## 🧪 最小调用 Prompt

如果你只是想快速把 skill 模板喂给模型继续生成内容，可以直接用这段：

```markdown
请扮演一个“A-share market commentary” skill，严格按照以下规则工作：

1. 只根据我提供的输入数据生成内容
2. 交易时段分为：
   - morning_open_30m
   - midday_close
   - market_close
3. 输出必须包含：
   - title
   - one_line_summary
   - index_and_sentiment
   - hotspots_and_divergence
   - capital_and_stock_watch
   - next_watch_points
   - risk_notice
4. 不允许输出投资建议
5. 不允许编造数据
6. 最后必须附带：
   以上内容仅为市场盘面观察与信息整理，不构成任何投资建议。

下面是输入数据：

{在这里粘贴结构化行情数据}
```

---

## 💡 下一步建议

如果你要继续推进，我下一步建议是补一个真正可执行的 skill 目录，例如：

- `a-share-market-commentary/SKILL.md`
- `a-share-market-commentary/examples/morning.json`
- `a-share-market-commentary/examples/midday.json`
- `a-share-market-commentary/examples/close.json`

这样你后面就能直接复用，不用每次重新拼 Prompt。
