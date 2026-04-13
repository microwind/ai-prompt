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
        
        sections = re.split(r'\n## ', content)
        header = sections[0]
        # Skip header for now, we'll rebuild it
        
        parts = {}
        for section in sections[1:]:
            lines = section.split('\n')
            parts[lines[0].strip()] = '\n'.join(lines[1:]).strip()

        # Platform: xhs
        xhs_title = f"# 深度解读《道德经》第{i}章：{original_title.split('：')[-1]} ✨"
        if i == 36: xhs_title = "# 揭秘顶级博弈：想要拿走，必须先给？🤔"
        elif i == 38: xhs_title = "# 扎心了！老子教你分辨：什么是真正的善良？"
        elif i == 41: xhs_title = "# 为什么优秀的人，看起来都很“笨”？💡"
        elif i == 44: xhs_title = "# 赚多少钱才算够？老子这一席话太清醒了！"
        elif i == 48: xhs_title = "# 高手的最高境界：做减法！🚀"
        
        xhs_analysis = parts.get('分析', '')
        # Add some emojis to analysis
        xhs_analysis = xhs_analysis.replace('。', '。✨').replace('！', '！🔥').replace('？', '？💡')
        xhs_tags = "\n\n#道德经 #国学智慧 #人生哲理"
        
        xhs_content = f"{xhs_title}\n\n## 原文\n{parts.get('原文', '')}\n\n## 解释\n{parts.get('解释', '')}\n\n## 分析\n{xhs_analysis}{xhs_tags}\n\n## 链接\n{parts.get('链接', '')}"
        
        with open(os.path.join(platforms['xhs'], filename), 'w', encoding='utf-8') as f:
            f.write(xhs_content)

        # Platform: toutiao
        tt_title = f"# 《道德经》第{i}章：{original_title.split('：')[-1]}，老子的人生智慧"
        tt_analysis = parts.get('分析', '')
        # Prepend a practical note
        tt_analysis = "【生活实战视角】\n" + tt_analysis
        
        tt_content = f"{tt_title}\n\n## 原文\n{parts.get('原文', '')}\n\n## 解释\n{parts.get('解释', '')}\n\n## 分析\n{tt_analysis}\n\n## 链接\n{parts.get('链接', '')}"
        
        with open(os.path.join(platforms['toutiao'], filename), 'w', encoding='utf-8') as f:
            f.write(tt_content)

        # Platform: zhihu / mp (Solemn/Logical)
        zh_title = f"# {original_title}：底层逻辑分析"
        zh_analysis = parts.get('分析', '')
        # Wrap analysis to emphasize logic
        zh_analysis = "### 核心逻辑演绎\n" + zh_analysis
        
        zh_content = f"{zh_title}\n\n## 原文\n{parts.get('原文', '')}\n\n## 解释\n{parts.get('解释', '')}\n\n## 分析\n{zh_analysis}\n\n## 链接\n{parts.get('链接', '')}"
        
        with open(os.path.join(platforms['zhihu'], filename), 'w', encoding='utf-8') as f:
            f.write(zh_content)
        with open(os.path.join(platforms['mp'], filename), 'w', encoding='utf-8') as f:
            f.write(zh_content)

    print(f"Successfully processed chapters {start} to {end} for 4 platforms.")

if __name__ == "__main__":
    process_chapters(36, 60)
