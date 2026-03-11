with open('input.txt', 'r', encoding='utf-8') as f:
    text_input = f.read().upper()

with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(text_input)
