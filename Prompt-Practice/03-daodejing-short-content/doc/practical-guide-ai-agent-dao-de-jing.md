# AI Agent实战：我用Gemini批量完成了《道德经》解读

> Claude Code 在开发上很好用，但用来做古文解读，效果不太理想。于是我换成了 Codex 和 Gemini，先从 Gemini 开始尝试。

几年前，我写过一本[《理解道德经》](https://www.zhihu.com/column/c_1477225327726850048)的读书笔记，整理成册后放到了 [Github](https://github.com/jarry/daodejing) 上。原版内容较长，需要不少耐心才能读完。我一直想把其中的核心提炼出来，做一个简化版，用最通俗、最简单的方式分享给大家。但苦于时间关系，一直没有落地。

直到Claude Code的出现，让我意识到AI Agent不只是写代码，也可以帮我来完成这项工作。下面就是我利用 AI Agent，分五步完成《理解道德经》81 章内容改写。

**先进入Gemini界面：**

![img](https://pic-out.zhimg.com/v2-0d32c329653accb67bf344baba6ae3f1~resize:1440:q75.png?animatedImageAutoPlay=false&animatedImagePlayCount=1&auth_key=1776083058-0-0-da794e56471363701e02cf86a17fee91&bizSceneCode=article_draft&expiration=1776083058&incremental=false&mid=46a42a228e63bcc9785041c0bd75e024&overTime=60&precoder=false&protocol=v2&retryCount=3&sampling=false&sceneCode=editor_copy_outbound&source=bfcaadb1)

### **步骤 1：规划与需求定义**

我先将 Agent 切换到“**Plan 模式**”，目的是让 AI 帮我完成三件事：

1. 澄清需求：制定需求文档
2. 制定整体计划：分步骤执行
3. 输出项目的“施工图纸”：制定SKILL

具体操作是：通过一段提示词，让 Gemini 进行需求分析，并自动生成可复用的 SKILL。

**提示词如下**：

```
背景：
我有一份《理解道德经》的完整解读原稿（每个章节独立成文）。
我想将其改编为简版解读，适合快节奏阅读，发布在小红书、微头条、知乎、微信公众号等平台。
格式规范请参考 `原稿/notes/第一章范本.md` 的内容。

角色：
你是一个国学研究专家，精通《道德经》以及经子史集。
同时你深谙互联网运营之道，知道什么样的内容符合当下社会的需要。
你也明白各自媒体平台差异与特点。

输出要求：
1. 需求分析文档：包括目标受众分析、各平台特点与适配策略、内容长度建议、风格关键词（如通俗、金句、启发）、排版规范（如分段、emoji使用、标点）等。
2. 工作计划：按章节数量（共81章）估算工期，分为若干阶段，每个阶段明确产出物和验收标准。
3. SKILL定义：输出一个提示词模板，我以后只需填入“章节号 + 原稿内容 + 目标平台”，即可自动生成符合规范且适配该平台的简版解读。
   SKILL模板应采用纯自然语言描述，不依赖特定模型扩展语法，以便支持各种大模型调用。
   当用户指定平台时，输出适配该平台的单一版本；未指定平台时，输出通用简版。

约束条件：
- 标准简版的内容和格式必须严格遵循上述“第一章范本.md”的样式。
- 简版解读的总字数（不含标题）应控制在范本字数的90%~110%之间，根据章节内容可酌情增删。字数以中文字符数为准。
- 生成的SKILL需明确说明输入格式和输出示例。

请按顺序输出：先需求分析文档，再工作机计划，然后SKILL定义。
```

几分钟后，Agent 按照我的要求，完成了设计文档、工作计划以及SKILL.md。

![img](https://pic-out.zhimg.com/v2-6732a95b229f7b52427efa2b3b86c62a~resize:1440:q75.png?animatedImageAutoPlay=false&animatedImagePlayCount=1&auth_key=1776083058-0-0-50c6de4eb729f1f9d8e507e0d48a6929&bizSceneCode=article_draft&expiration=1776083058&incremental=false&mid=46a42a228e63bcc9785041c0bd75e024&overTime=60&precoder=false&protocol=v2&retryCount=3&sampling=false&sceneCode=editor_copy_outbound&source=bfcaadb1)![img](https://pic-out.zhimg.com/v2-c52177c9c3845d58ea85e9364ede0364~resize:1440:q75.png?animatedImageAutoPlay=false&animatedImagePlayCount=1&auth_key=1776083058-0-0-ddb53699fb7d2f75bb22bfb3f1109948&bizSceneCode=article_draft&expiration=1776083058&incremental=false&mid=46a42a228e63bcc9785041c0bd75e024&overTime=60&precoder=false&protocol=v2&retryCount=3&sampling=false&sceneCode=editor_copy_outbound&source=bfcaadb1)![img](https://pic-out.zhimg.com/v2-80bd9515d60c90e578493c0646093631~resize:1440:q75.png?animatedImageAutoPlay=false&animatedImagePlayCount=1&auth_key=1776083058-0-0-e836e72be7f4aa083b011f1a04d1f14b&bizSceneCode=article_draft&expiration=1776083058&incremental=false&mid=46a42a228e63bcc9785041c0bd75e024&overTime=60&precoder=false&protocol=v2&retryCount=3&sampling=false&sceneCode=editor_copy_outbound&source=bfcaadb1)

**步骤 2：保存生成的文档，修改SKILL文件**

为了后续可重复生成 ，也为了能用其他大模型来生成内容，我需要保存技能文档（`SKILL.md`）。同时，为保证输出质量，我还需要手工修改和打磨技能文件。接下来跟AI交互对话。

![img](https://pic-out.zhimg.com/v2-e4d86a77aa1c4622b11d3ac24c156a6d~resize:1440:q75.png?animatedImageAutoPlay=false&animatedImagePlayCount=1&auth_key=1776083058-0-0-b5459f59b4bca0b0c616a48f3a1b18bd&bizSceneCode=article_draft&expiration=1776083058&incremental=false&mid=46a42a228e63bcc9785041c0bd75e024&overTime=60&precoder=false&protocol=v2&retryCount=3&sampling=false&sceneCode=editor_copy_outbound&source=bfcaadb1)![img](https://pic-out.zhimg.com/v2-8c7494eed1bcff26af71b94a52c1664f~resize:1440:q75.png?animatedImageAutoPlay=false&animatedImagePlayCount=1&auth_key=1776083058-0-0-ddcb821eb5e8c11e7cfb74d1e6f8c9e4&bizSceneCode=article_draft&expiration=1776083058&incremental=false&mid=46a42a228e63bcc9785041c0bd75e024&overTime=60&precoder=false&protocol=v2&retryCount=3&sampling=false&sceneCode=editor_copy_outbound&source=bfcaadb1)![img](https://pic-out.zhimg.com/v2-15070e83c81f710a7c3449bb49871f71~resize:1440:q75.png?animatedImageAutoPlay=false&animatedImagePlayCount=1&auth_key=1776083058-0-0-f6e869ab84e81321ed10ab2b82909d93&bizSceneCode=article_draft&expiration=1776083058&incremental=false&mid=46a42a228e63bcc9785041c0bd75e024&overTime=60&precoder=false&protocol=v2&retryCount=3&sampling=false&sceneCode=editor_copy_outbound&source=bfcaadb1)

需求分析我看了下，可以作为生成SKILL参考。开发计划并不适用，毕竟这不是软件开发，不需要复杂的流程。SKILL生成完成，基本可以使用，我稍微调整了下措辞。

需求分析我看了，可以作为生成 SKILL 的参考。开发计划并不适用，毕竟这不是软件开发，不需要复杂的流程。SKILL 已生成完成，基本可用，我稍微调整了一下措辞。

**下面是修改后的完整SKILL内容：**

~~~python
# SKILL：老子智慧解读器 (Laozi Wisdom Interpreter)

## Role: 
你是一位精通《道德经》的国学研究者且深谙自媒体平台内容运营。
你懂得古人的智慧，也懂得该如何传递给当下的人们。
你能将深奥的古籍原稿转化为适合快节奏阅读的简版解读，语言朴素、通俗易懂且极具启发性。

## Knowledge & Source:
- **参考来源：** 本地项目目录 `原稿/notes/` 下的对应章节文件。你必须基于该原始解读进行改编，保留其核心逻辑和深度洞察。
- **参考范本** 本地项目目录 `原稿/notes/第一章范本.md`。
- **项目在线地址：** https://github.com/jarry/daodejing (在输出的“链接”部分引用)。

## Constraints:
1. **严格格式：** 输出格式必须严格遵循“第一章范本”。
2. **金句标题：** 标题必须摘自原文中最具代表性、最能引起共鸣的短句。
3. **全量原文：** 必须输出章节的全部原文，并为其中的生僻字或多音字增加注音（如：恶 wù、几 jī）。
4. **深度分析：** 分析内容需保持深度与启发性，必须基于参考来源中的核心思想进行提炼。要直击人心，关联现代人的生活焦虑、职场规则或成长困惑。
5. **资源组件：** 文章末尾必须包含固定的“## 链接”部分。
6. **结构：** ## 原文 (代码块) -> ## 解释 (加粗原文+白话) -> ## 分析 (核心洞察) -> ## 链接。

## Workflow:
1. **加载原稿：** 读取 `原稿/notes/[章节号].md`。
2. **解析与精炼：** 提取原稿中的原文、核心解释和深度分析。去除琐碎身份描述，将深刻的哲学观点升华为普适智慧。
3. **平台适配优化：**
   - 若未特别指定，默认按标准版本，即完全遵照“第一章范本”格式和风格去解读和分析，不要增加多余内容。
   - 若是指定[小红书]风格：在分析部分增加 Emoji，文末加 3 个 Tag，标题需更具情绪冲击力。
   - 若是指定[知乎/公众号]风格：保持庄重、简洁、排版优雅，侧重逻辑和第一性原理。
   - 若是指定[微头条]风格：标题直白、分析部分多关联常识与现实案例。

4. **格式化输出：** 按照最终模板生成内容，确保包含完整原文、注音、深度分析和资源链接。

## Output Template:
# 第 [章节号] 章：[章节标题/原文金句]
> 《道德经》简单解说版，用简单朴素语言解说。

## 原文
```
[完整原文内容，带关键注音]
```

## 解释
**[原文核心句]**
[基于原稿的朴素白话解释，通俗易懂，去掉琐碎描述]

## 分析
[第1段：从原稿提炼核心底层逻辑]
[第2段：关联现代生活/职场/心理痛点，提供深度洞察]
[第3段：给出具体的行动启发或心态调整建议]

## 链接
《理解道德经》仓库：https://github.com/jarry/daodejing
《理解道德经》PDF下载: https://pan.baidu.com/s/1-r2jRpVWAAir2tadAb-qMA 密码: 2k6b
~~~

### **步骤 3：验证2-3个生成效果**

这是非常关键的一步，决定着最终质量。我按照“第一章范本”的标准，仔细检查了 AI 生成的内容，并给出了一些细微调整，根据AI又进行几轮对话。只有确认符合质量要求之后，才会进行批量输出。

![img](https://pic-out.zhimg.com/v2-b3d85dbc73ba1df965401b021de427b0~resize:1440:q75.png?animatedImageAutoPlay=false&animatedImagePlayCount=1&auth_key=1776083058-0-0-560f48ed0a02f4a2153946aaa2ff1a56&bizSceneCode=article_draft&expiration=1776083058&incremental=false&mid=46a42a228e63bcc9785041c0bd75e024&overTime=60&precoder=false&protocol=v2&retryCount=3&sampling=false&sceneCode=editor_copy_outbound&source=bfcaadb1)![img](https://pic-out.zhimg.com/v2-e2587bb651f9d4f36f1b6126db021275~resize:1440:q75.png?animatedImageAutoPlay=false&animatedImagePlayCount=1&auth_key=1776083058-0-0-6d6101be2f0281ed74ba776854b9b9a0&bizSceneCode=article_draft&expiration=1776083058&incremental=false&mid=46a42a228e63bcc9785041c0bd75e024&overTime=60&precoder=false&protocol=v2&retryCount=3&sampling=false&sceneCode=editor_copy_outbound&source=bfcaadb1)![img](https://pic-out.zhimg.com/v2-4892ae93ea6cf5bbf31d395ddc437632~resize:1440:q75.png?animatedImageAutoPlay=false&animatedImagePlayCount=1&auth_key=1776083058-0-0-130551dd28043cf1e6ebe60a48bb9900&bizSceneCode=article_draft&expiration=1776083058&incremental=false&mid=46a42a228e63bcc9785041c0bd75e024&overTime=60&precoder=false&protocol=v2&retryCount=3&sampling=false&sceneCode=editor_copy_outbound&source=bfcaadb1)![img](https://pic-out.zhimg.com/v2-aa90982750bab79f09f39254ec265463~resize:1440:q75.png?animatedImageAutoPlay=false&animatedImagePlayCount=1&auth_key=1776083058-0-0-1d1b132aa092e97b8f79616cfa554ab0&bizSceneCode=article_draft&expiration=1776083058&incremental=false&mid=46a42a228e63bcc9785041c0bd75e024&overTime=60&precoder=false&protocol=v2&retryCount=3&sampling=false&sceneCode=editor_copy_outbound&source=bfcaadb1)

经过几轮对话，AI Agent终于生成了让我满意的版本。

### 步骤 4： **挂载参考资料**

我将之前写的解读笔记目录挂载给 Agent。如果还有其他资料，也会一并告诉它。

![img](https://pic-out.zhimg.com/v2-830e6c8d551462de149e7c23ec15ba06~resize:1440:q75.png?animatedImageAutoPlay=false&animatedImagePlayCount=1&auth_key=1776083058-0-0-213c31f686e537d8939a9dfac649bfc0&bizSceneCode=article_draft&expiration=1776083058&incremental=false&mid=46a42a228e63bcc9785041c0bd75e024&overTime=60&precoder=false&protocol=v2&retryCount=3&sampling=false&sceneCode=editor_copy_outbound&source=bfcaadb1)![img](https://pic-out.zhimg.com/v2-eb7f10055b4b419af4a5f30ce7d0126c~resize:1440:q75.png?animatedImageAutoPlay=false&animatedImagePlayCount=1&auth_key=1776083058-0-0-fdc250ab1d9c24c0772709424c810772&bizSceneCode=article_draft&expiration=1776083058&incremental=false&mid=46a42a228e63bcc9785041c0bd75e024&overTime=60&precoder=false&protocol=v2&retryCount=3&sampling=false&sceneCode=editor_copy_outbound&source=bfcaadb1)

### 步骤 5：**批量生产与验证** 

现在需求文档、计划以及SKILL都整理完毕了，可以按计划批量生成结果了。生成过程是分批进行的，每一批我都要检查和确认下质量。

![img](https://pic-out.zhimg.com/v2-c88282127ff0e80bb9e2372634df40d9~resize:1440:q75.png?animatedImageAutoPlay=false&animatedImagePlayCount=1&auth_key=1776083058-0-0-795bf7243792babca510c1eaf6e90b77&bizSceneCode=article_draft&expiration=1776083058&incremental=false&mid=46a42a228e63bcc9785041c0bd75e024&overTime=60&precoder=false&protocol=v2&retryCount=3&sampling=false&sceneCode=editor_copy_outbound&source=bfcaadb1)![img](https://pic-out.zhimg.com/v2-6cdabbfda5a9c901cec22eb02dd5c043~resize:1440:q75.png?animatedImageAutoPlay=false&animatedImagePlayCount=1&auth_key=1776083058-0-0-0bf9e19413495a4fc801bd00aa9d97f9&bizSceneCode=article_draft&expiration=1776083058&incremental=false&mid=46a42a228e63bcc9785041c0bd75e024&overTime=60&precoder=false&protocol=v2&retryCount=3&sampling=false&sceneCode=editor_copy_outbound&source=bfcaadb1)![img](https://pic-out.zhimg.com/v2-dca81fbcb4cab287e6187bf7564d93cc~resize:1440:q75.png?animatedImageAutoPlay=false&animatedImagePlayCount=1&auth_key=1776083058-0-0-2f6f5082293db42c0fbe2de09b6f5c1f&bizSceneCode=article_draft&expiration=1776083058&incremental=false&mid=46a42a228e63bcc9785041c0bd75e024&overTime=60&precoder=false&protocol=v2&retryCount=3&sampling=false&sceneCode=editor_copy_outbound&source=bfcaadb1)![img](https://pic-out.zhimg.com/v2-121ee7b6086492dac251e92f0726825c~resize:1440:q75.png?animatedImageAutoPlay=false&animatedImagePlayCount=1&auth_key=1776083058-0-0-a53cbe531eebd3c7ccf6394ced1008c6&bizSceneCode=article_draft&expiration=1776083058&incremental=false&mid=46a42a228e63bcc9785041c0bd75e024&overTime=60&precoder=false&protocol=v2&retryCount=3&sampling=false&sceneCode=editor_copy_outbound&source=bfcaadb1)![img](https://pic-out.zhimg.com/v2-716e7289d7ea6dbe0e33ebe1d7405de0~resize:1440:q75.png?animatedImageAutoPlay=false&animatedImagePlayCount=1&auth_key=1776083058-0-0-67087dabb4fb7569459a06f98238d37e&bizSceneCode=article_draft&expiration=1776083058&incremental=false&mid=46a42a228e63bcc9785041c0bd75e024&overTime=60&precoder=false&protocol=v2&retryCount=3&sampling=false&sceneCode=editor_copy_outbound&source=bfcaadb1)![img](https://pic-out.zhimg.com/v2-a2b7ce5224d44000fff6a5c3ce9826a4~resize:1440:q75.png?animatedImageAutoPlay=false&animatedImagePlayCount=1&auth_key=1776083058-0-0-676e22aa5e3ee10173ff903a9845618c&bizSceneCode=article_draft&expiration=1776083058&incremental=false&mid=46a42a228e63bcc9785041c0bd75e024&overTime=60&precoder=false&protocol=v2&retryCount=3&sampling=false&sceneCode=editor_copy_outbound&source=bfcaadb1)![img](https://pic-out.zhimg.com/v2-6455d6df097cbafdb8e67dcbdaeca365~resize:1440:q75.png?animatedImageAutoPlay=false&animatedImagePlayCount=1&auth_key=1776083058-0-0-bead5ac0386644bfd02b120d573b4456&bizSceneCode=article_draft&expiration=1776083058&incremental=false&mid=46a42a228e63bcc9785041c0bd75e024&overTime=60&precoder=false&protocol=v2&retryCount=3&sampling=false&sceneCode=editor_copy_outbound&source=bfcaadb1)![img](https://pic-out.zhimg.com/v2-5f6480a5cb6e0c4b600c80ff509c7482~resize:1440:q75.png?animatedImageAutoPlay=false&animatedImagePlayCount=1&auth_key=1776083058-0-0-3eca7d984f133f7ed98d0480e2aeaaaa&bizSceneCode=article_draft&expiration=1776083058&incremental=false&mid=46a42a228e63bcc9785041c0bd75e024&overTime=60&precoder=false&protocol=v2&retryCount=3&sampling=false&sceneCode=editor_copy_outbound&source=bfcaadb1)

经过几轮对话，终于完成了我想要的效果。AI Agent还是不错的。

### **总结**

通过这种`Plan → SKILL → 指定范本 → 挂载资源 → 执行任务`的五步法，我终于将之前的《理解道德经》整理成了几套适合不同自媒体平台的简版文章。

虽然每一章内容在发布前我还是得审稿和修改，并不能直接发布，但有了 AI 的帮忙，确实节省了很多时间。关键是有了SKILL，以后还可以用不同的大模型来生成。

虽然我采取的仍是 Vibe Coding 模式，通过多轮对话来完成任务，并没有让 AI 自主制定计划和执行，我还是参与了不少工作。但我想对于这种项目来讲，这是有必要的。

AI Agent 在这里不仅是一个对话框，而是一个理解我思维的“数字助手”。它帮我处理了繁琐的格式转换和总结润色等工作，而我只需要守住第一章的“道”和原稿的“神”。

### **相关链接**

本文github源文件：https://github.com/microwind/ai-prompt 

《理解道德经》仓库：https://github.com/jarry/daodejing
