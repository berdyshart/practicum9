with open('input.txt', 'r', encoding='utf-8') as f_in:
    text_input_lines = f_in.readlines()

with open('output.txt', 'a', encoding='utf-8') as f_out:
    for line in text_input_lines:
        try:
            if len(line.strip()) > 20:
                f_out.write(line)
        except IndexError:
            print('Empty line!')
