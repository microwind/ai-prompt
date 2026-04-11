import os
import re

source_dir = '/Users/jarry/github/ai-prompt/Prompt-Examples/05-Project-Pratice/03-daodejing-short-content/原稿/notes'
output_dir = '/Users/jarry/github/ai-prompt/Prompt-Examples/05-Project-Pratice/03-daodejing-short-content/output'

links = """## 链接
《道德经》资料：https://github.com/jarry/daodejing
《理解道德经》PDF下载: https://pan.baidu.com/s/1-r2jRpVWAAir2tadAb-qMA 密码: 2k6b"""

quote = "> 《道德经》简单解说版，用简单朴素语言解说。"

def process_chapter(chapter_num):
    file_path = os.path.join(source_dir, f"{chapter_num}.md")
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract title from the first sentence of the text
    # Look for "原文：" section
    original_text_match = re.search(r'## 《道德经》第.*?章通行本原文：\n\n?(.*?)\n\n?##', content, re.DOTALL)
    if not original_text_match:
        # Try a different pattern if the first one fails
        original_text_match = re.search(r'## 《道德经》第.*?章通行本原文：\s*(.*?)\s*##', content, re.DOTALL)
    
    if not original_text_match:
        print(f"Original text not found for chapter {chapter_num}")
        return

    original_text = original_text_match.group(1).strip()
    # Clean up whitespace/indentation in original text
    original_lines = [line.strip() for line in original_text.split('\n') if line.strip()]
    original_text_clean = '\n'.join(original_lines)

    # Use the first line (or part of it) as the title
    title_line = original_lines[0].split('，')[0].split('；')[0].split('。')[0]
    title = f"# 第 {chapter_num} 章：{title_line}"

    # Extract Explanation
    explanation_match = re.search(r'## 逐句解释：\n\n?(.*?)\n\n?(##|<img|\[返回目录\])', content, re.DOTALL)
    if not explanation_match:
         explanation_match = re.search(r'## 逐句解释：\s*(.*?)\s*(##|<img|\[返回目录\])', content, re.DOTALL)
    
    explanation_text = ""
    if explanation_match:
        explanation_raw = explanation_match.group(1).strip()
        # Convert ### Heading to **Heading**
        # Also remove images
        explanation_raw = re.sub(r'<img.*?>', '', explanation_raw)
        lines = explanation_raw.split('\n')
        processed_explanation_lines = []
        for line in lines:
            line = line.strip()
            if line.startswith('###'):
                processed_explanation_lines.append(f"**{line.replace('###', '').strip()}**")
            elif line:
                processed_explanation_lines.append(line)
            else:
                processed_explanation_lines.append("")
        explanation_text = '\n'.join(processed_explanation_lines).strip()

    # Extract Analysis
    analysis_match = re.search(r'## 心得总结：\n\n?(.*?)\n\n?(##|附帛书版|\[返回目录\]|<img)', content, re.DOTALL)
    if not analysis_match:
        analysis_match = re.search(r'## 心得总结：\s*(.*?)\s*(##|附帛书版|\[返回目录\]|<img)', content, re.DOTALL)
    
    analysis_text = ""
    if analysis_match:
        analysis_raw = analysis_match.group(1).strip()
        # Clean up images and subheadings in analysis if any
        analysis_raw = re.sub(r'<img.*?>', '', analysis_raw)
        # Convert ### Heading in analysis to just bold or plain text
        analysis_raw = re.sub(r'###\s*(.*)', r'**\1**', analysis_raw)
        analysis_text = analysis_raw.strip()

    # Construct the final markdown
    output_content = f"{title}\n\n{quote}\n\n## 原文\n```\n{original_text_clean}\n```\n\n## 解释\n{explanation_text}\n\n## 分析\n{analysis_text}\n\n{links}"
    
    output_file = os.path.join(output_dir, f"chapter_{int(chapter_num):02d}.md")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output_content)
    print(f"Wrote {output_file}")

for i in range(2, 82):
    process_chapter(str(i))
