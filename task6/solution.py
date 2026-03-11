with open('output.txt', 'w', encoding='utf-8') as f_out:
    with open('input.txt', 'r', encoding='utf-8') as f_in:
        text_input_lines = f_in.readlines()
    amount_lines = len(text_input_lines) - 1

    try:
        amount_lines_required = int(text_input_lines[0])
        if amount_lines_required == amount_lines:
            f_out.write('YES')
        else:
            f_out.write('NO')
    except ValueError:
        f_out.write('ERROR')
