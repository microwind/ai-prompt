---
name: a-share-market-commentary
description: Generate structured A-share market commentary for three fixed trading sessions using supplied market data: within 30 minutes after market open, after midday close, and after market close. Use this skill when the user wants factual market observation, intraday commentary, or end-of-day review content based on real A-share inputs. Do not use it for stock picking, trading advice, or fabricated commentary without data.
---

# A-Share Market Commentary

## Purpose

Generate concise, structured A-share market commentary for:

1. `morning_open_30m`
2. `midday_close`
3. `market_close`

This skill is for market observation and content generation. It is not for investment advice.

## When To Use

Use this skill when the user wants:

- a morning market opening commentary
- a midday market summary
- an end-of-day market review
- structured A-share market content based on supplied market data

Do not use this skill when:

- the input data is too incomplete for a factual summary
- the user asks for direct stock recommendations
- the user asks for certain market predictions
- the user asks you to invent facts not present in the input

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
- `special_events`
- `extra_notes`

## Session Focus

### `morning_open_30m`

Focus on:

- opening index behavior
- early breadth and turnover
- first-wave sector rotation
- initial capital preference
- what to watch next

### `midday_close`

Focus on:

- first-half market structure
- whether morning themes are strengthening or diverging
- breadth and turnover by noon
- what to watch in the afternoon

### `market_close`

Focus on:

- full-day market summary
- leading and weak themes
- capital flow and sentiment confirmation
- next-session watch points

## Working Rules

1. Use only the supplied data.
2. Never fabricate facts or hidden causes.
3. Never give buy or sell advice.
4. Never promise market direction or returns.
5. Use a professional, calm, neutral tone.
6. Prefer synthesis over raw data dumping.
7. If input is incomplete, state that cautiously and narrow the conclusion.

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

Title: {concise title}

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

## Workflow

1. Confirm `session_type`.
2. Validate key fields before writing.
3. Select the proper session focus.
4. Summarize the market with restraint.
5. End with 2-3 useful watch points.
6. Append the fixed risk notice.

## Example Inputs

Use these files when needed:

- `examples/morning.json`
- `examples/midday.json`
- `examples/close.json`
