with open("words.txt", "r") as f:
    lines = f.readlines()

filtered_lines = []
for line in lines:
    word = line.strip()
    if len(word) >= 4:
        filtered_lines.append(word + "\n")

with open("long_words.txt", "w") as f:
    f.writelines(filtered_lines)
