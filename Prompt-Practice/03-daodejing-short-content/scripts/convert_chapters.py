import os
import re

def get_all_chapters():
    with open('原稿/tongxingben.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by ### 【
    parts = re.split(r'### 【', content)
    # The first part is usually the title/header of the file
    chapters = {}
    for part in parts[1:]:
        # Part starts with "第一章】\n..."
        match = re.search(r'^(.*?)】\n(.*)', part, re.DOTALL)
        if match:
            ch_title = match.group(1).strip()
            ch_content = match.group(2).strip()
            # Convert Chinese number to Arabic if needed, but we can just use the index
            # But wait, I'll just find the one that matches our target index
            chapters[ch_title] = ch_content
    
    # Let's map them by index
    chapter_list = [None] * 82
    # We can try to determine the index from the title
    # But it's easier to just assume they are in order 1-81
    for i, part in enumerate(parts[1:], 1):
        match = re.search(r'^.*?】\n(.*)', part, re.DOTALL)
        if match:
            if i <= 81:
                chapter_list[i] = match.group(1).strip()
    
    return chapter_list

def parse_note(ch_num):
    file_path = f'原稿/notes/{ch_num}.md'
    if not os.path.exists(file_path):
        print(f"Note for chapter {ch_num} not found at {file_path}")
        return None, []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract Explanation
    explanation_section = ""
    exp_match = re.search(r'## 逐句解释：(.*?)(?=## |$)', content, re.DOTALL)
    if exp_match:
        section = exp_match.group(1).strip()
        # Parse each subsection
        items = re.split(r'### ', section)
        for item in items:
            if not item.strip(): continue
            lines = item.strip().split('\n')
            orig = lines[0].strip()
            # Remove pinyin in parentheses if present in the header
            orig_clean = re.sub(r'（.*?）', '', orig).strip()
            # Remove markdown formatting like bold if already there
            orig_clean = orig_clean.replace('**', '')
            meaning = "\n".join(lines[1:]).strip()
            if orig_clean and meaning:
                explanation_section += f"**{orig_clean}**\n{meaning}\n\n"
    else:
        print(f"Explanation for chapter {ch_num} not found")

    # Extract Analysis
    analysis_paragraphs = []
    ana_match = re.search(r'## 心得总结：(.*?)(?=## |附帛书版|$)', content, re.DOTALL)
    if ana_match:
        section = ana_match.group(1).strip()
        # Remove images
        section = re.sub(r'<img.*?>', '', section)
        # Split by double newlines or single newlines that look like paragraphs
        paragraphs = [p.strip() for p in re.split(r'\n\s*\n', section) if p.strip()]
        analysis_paragraphs = paragraphs
    else:
        print(f"Analysis for chapter {ch_num} not found")

    return explanation_section.strip(), analysis_paragraphs

all_texts = get_all_chapters()

def generate_chapter(ch_num):
    orig_text = all_texts[ch_num] if ch_num < len(all_texts) else None
    if not orig_text:
        print(f"Original text for chapter {ch_num} not found")
        return
    
    # Title selection: first sentence of orig_text
    title_match = re.split(r'[，。；？！\n]', orig_text)
    title_phrase = title_match[0].strip() if title_match else "未命名"
    
    explanation, analysis_paras = parse_note(ch_num)
    
    # Re-structure analysis into 3 parts
    if len(analysis_paras) >= 3:
        logic = analysis_paras[0]
        life = "\n\n".join(analysis_paras[1:-1])
        action = analysis_paras[-1]
    elif len(analysis_paras) == 2:
        logic = analysis_paras[0]
        life = analysis_paras[1]
        action = analysis_paras[1] # fallback
    elif len(analysis_paras) == 1:
        logic = analysis_paras[0]
        life = analysis_paras[0]
        action = analysis_paras[0]
    else:
        logic = "遵循天道规律。"
        life = "在生活和职场中顺势而为。"
        action = "保持谦卑与无为。"

    # Format output
    output = f"""# 第 {ch_num} 章：{title_phrase}

> 《道德经》简单解说版，用简单朴素语言解说。

## 原文
```
{orig_text}
```

## 解释
{explanation}

## 分析
{logic}

{life}

{action}

## 链接
《道德经》资料：https://github.com/jarry/daodejing
《理解道德经》PDF下载: https://pan.baidu.com/s/1-r2jRpVWAAir2tadAb-qMA 密码: 2k6b
"""
    
    file_path = f'output/chapter_{ch_num:02d}.md'
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(output)
    # print(f"Successfully wrote {file_path}")

for i in range(41, 82):
    # print(f"Generating Chapter {i}...")
    generate_chapter(i)
