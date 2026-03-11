with open('input.txt', 'r', encoding='utf-8') as f_in:
    text_input_lines = f_in.readlines()

with open('output.txt', 'w', encoding='utf-8') as f_out:
    num0, num1, num2, result = 0, 0, 0, 0

    try:
        num0 = int(text_input_lines[0])
        num1 = int(text_input_lines[1])
        num2 = int(text_input_lines[2])

        try:
            result = str(num0 / num1 + num2)
            f_out.write(result)
        except ZeroDivisionError:
            f_out.write('division by zero')

    except ValueError:
        f_out.write('Invalid data')
