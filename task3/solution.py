text_out = ''

with open('input.txt', 'r', encoding='utf-8') as f_in:
    text_input_lines = f_in.readlines()
    print(text_input_lines)
    for line in text_input_lines:
        text_out += line[0]
print(text_out)

with open('output.txt', 'w', encoding='utf-8') as f_out:
    f_out.write(text_out)
