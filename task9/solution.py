import os

with open('input.txt', 'r', encoding='utf-8') as f_in:
    lines = f_in.readlines()
    lines = [lines[num] for num in range(len(lines)) if num % 2 == 1]

os.mkdir('simple')

with open('simple/output.txt', 'w', encoding='utf-8') as f_out:
    f_out.writelines(lines)
