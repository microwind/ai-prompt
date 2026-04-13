import os
import re

def parse_note(ch_num):
    file_path = f'原稿/notes/{ch_num}.md'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract Explanation
    explanation_section = ""
    # Try multiple patterns
    exp_match = re.search(r'## 逐句解释：?\n(.*?)(?=\n## |$)', content, re.DOTALL)
    if not exp_match:
        # Try without the newline requirement
        exp_match = re.search(r'## 逐句解释：?(.*?)(?=\n## |$)', content, re.DOTALL)
    
    if exp_match:
        section = exp_match.group(1).strip()
        print(f"Found section for {ch_num}, length: {len(section)}")
        items = re.split(r'### ', section)
        print(f"Items: {len(items)}")
        for item in items:
            if not item.strip(): continue
            lines = item.strip().split('\n')
            orig = lines[0].strip()
            meaning = "\n".join(lines[1:]).strip()
            print(f"  Orig: {orig[:20]}...")
            if orig and meaning:
                explanation_section += f"**{orig}**\n{meaning}\n\n"
    else:
        print(f"Regex failed for {ch_num}")

    return explanation_section.strip()

print("Testing Chapter 41:")
print(parse_note(41))
