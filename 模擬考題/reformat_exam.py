import os

filepath = r"d:\Obsidian\30_Resources\AI應用規劃能力鑑定\模擬考題\模擬考卷_第一回.md"
with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
answers = []
q_num = 0

i = 0
while i < len(lines):
    line = lines[i]
    if line.startswith("> [!question] 第"):
        line = line.replace("> [!question] 第", "> [!question] [  ] 第")
        new_lines.append(line)
        i += 1
    elif line.startswith("> **解答**："):
        ans_text = line.replace("> ", "", 1).strip()
        q_num = len(answers) + 1
        answers.append(f"### 第 {q_num} 題\n{ans_text}\n")
        
        # Remove the preceding empty blockquote line "> \n" or ">\n" if it exists
        if len(new_lines) > 0 and new_lines[-1].strip() == ">":
            new_lines.pop()
        
        i += 1
    elif "【作答結束】" in line:
        # Keep it but remove it from here so we can place it before answers
        new_lines.append(line)
        i += 1
    else:
        new_lines.append(line)
        i += 1

with open(filepath, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
    f.write("\n---\n\n# 📝 考題解答\n\n")
    for ans in answers:
        f.write(ans + "\n")

print("Exam format updated successfully.")
