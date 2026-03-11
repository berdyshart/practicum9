with open('input.txt', 'r', encoding='utf-8') as f_in:
    text_input_lines = f_in.readlines()

with open('output.txt', 'w', encoding='utf-8') as f_out:
    for line in text_input_lines:
        if '100' not in line:
            f_out.write(line)
