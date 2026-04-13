import os
import re

def process_chapters(start, end):
    source_dir = 'output'
    platforms = {
        'xhs': 'output/xhs',
        'toutiao': 'output/toutiao',
        'zhihu': 'output/zhihu',
        'mp': 'output/mp'
    }

    # Ensure directories exist
    for path in platforms.values():
        os.makedirs(path, exist_ok=True)

    xhs_custom_titles = {
        61: "大国博弈的终极秘密：为什么“向下”才是真正的强大？✨",
        62: "万物的奥秘：老子这一席话，道破了人生的最高境界！🤔",
        63: "把小事做大，把难事做易：这就是普通人逆袭的最高心法！🔥",
        64: "扎心了！为什么你总是半途而废？老子早就在《道德经》里说了！💡",
        65: "为什么聪明人看起来都很“笨”？原来这才是真正的智慧！🚀",
        66: "想让别人听你的？老子教你一招：把自己放在最低处！✨",
        67: "老子压箱底的3件“保命符”，看懂的人都不再内耗了！💎",
        68: "真正的狠人，从来不跟人硬刚！老子教你什么叫“不争之德”！🔥",
        69: "高手过招，比的是谁更低调！揭秘《道德经》里的用兵智慧！🛡️",
        70: "越深刻的东西越简单，只是很多人都不愿意相信罢了！🧠",
        71: "清醒一点！那些“知不知”的人，才是真正站在顶端的人！💡",
        72: "别让傲慢毁了你的生活：老子谈什么是真正的“威严”！🚧",
        73: "天网恢恢疏而不漏：你的善良，老天爷都看在眼里！✨",
        74: "连死都不怕，那还怕什么？老子教你如何看透人生的恐惧！🌑",
        75: "为什么生活越来越难？老子这一段话，放在今天依然扎心！🥀",
        76: "人活着越柔软，命就越长？深度解析老子的养生智慧！🌱",
        77: "天之道：损有余而补不足。揭秘财富分配的终极规律！⚖️",
        78: "天下莫柔弱于水！为什么“以柔克刚”才是世界的真相？🌊",
        79: "天道无亲，常与善人！为什么最后赢的都是那些厚道人？✨",
        80: "回归本心：在喧嚣的世界里，寻找属于你的“世外桃源”！🏡",
        81: "《道德经》大结局：高手的一生，核心只有这四个字！🎓",
    }

    for i in range(start, end + 1):
        filename = f'chapter_{i:02d}.md'
        source_path = os.path.join(source_dir, filename)
        
        if not os.path.exists(source_path):
            print(f"Skipping {filename}, not found.")
            continue

        with open(source_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Parse sections
        title_match = re.search(r'^# (.*)', content, re.M)
        original_title = title_match.group(1) if title_match else f"第 {i} 章"
        
        # Split by ## sections
        sections = re.split(r'\n## ', content)
        
        parts = {}
        for section in sections[1:]:
            lines = section.split('\n')
            section_name = lines[0].strip()
            section_content = '\n'.join(lines[1:]).strip()
            parts[section_name] = section_content

        # Platform: xhs (Emotional titles, Emoji in analysis, 3 hashtags)
        xhs_title = f"# {xhs_custom_titles.get(i, f'深度解读《道德经》第{i}章：' + original_title.split('：')[-1] + ' ✨')}"
        
        xhs_analysis = parts.get('分析', '')
        # Add emojis to analysis
        xhs_analysis = xhs_analysis.replace('。', '。✨').replace('！', '！🔥').replace('？', '？💡').replace('“', '✨“').replace('”', '”✨')
        xhs_tags = "\n\n#道德经 #国学智慧 #人生哲理"
        
        xhs_content = f"{xhs_title}\n\n## 原文\n{parts.get('原文', '')}\n\n## 解释\n{parts.get('解释', '')}\n\n## 分析\n{xhs_analysis}{xhs_tags}\n\n## 底部链接\n{parts.get('链接', '')}"
        
        with open(os.path.join(platforms['xhs'], filename), 'w', encoding='utf-8') as f:
            f.write(xhs_content)

        # Platform: toutiao (Straightforward titles, life examples/common sense)
        tt_title = f"# 《道德经》第{i}章：{original_title.split('：')[-1]}，老子的人生智慧"
        tt_analysis = parts.get('分析', '')
        # Prepend a practical note
        tt_analysis = "【生活实战视角与现实案例】\n" + tt_analysis
        
        tt_content = f"{tt_title}\n\n## 原文\n{parts.get('原文', '')}\n\n## 解释\n{parts.get('解释', '')}\n\n## 分析\n{tt_analysis}\n\n## 底部链接\n{parts.get('链接', '')}"
        
        with open(os.path.join(platforms['toutiao'], filename), 'w', encoding='utf-8') as f:
            f.write(tt_content)

        # Platform: zhihu / mp (Solemn/Logical, first principles)
        zh_title = f"# {original_title}：底层逻辑分析"
        zh_analysis = parts.get('分析', '')
        # Wrap analysis to emphasize logic
        zh_analysis = "### 核心底层逻辑与第一性原理分析\n" + zh_analysis
        
        zh_content = f"{zh_title}\n\n## 原文\n{parts.get('原文', '')}\n\n## 解释\n{parts.get('解释', '')}\n\n## 分析\n{zh_analysis}\n\n## 底部链接\n{parts.get('链接', '')}"
        
        with open(os.path.join(platforms['zhihu'], filename), 'w', encoding='utf-8') as f:
            f.write(zh_content)
        with open(os.path.join(platforms['mp'], filename), 'w', encoding='utf-8') as f:
            f.write(zh_content)

    print(f"Successfully processed chapters {start} to {end} for 4 platforms.")

if __name__ == "__main__":
    process_chapters(61, 81)
