months = [
    'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
    'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'
]
days_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
counter = 0

with open('input.txt', 'r', encoding='utf-8') as f_in:
    steps_per_day = f_in.readlines()
    steps_per_day = [int(steps) for steps in steps_per_day]

with open('output.txt', 'w', encoding='utf-8') as f_out:
    for i in range(len(months)):
        month = months[i]
        days = days_list[i]

        steps_average = sum(steps_per_day[counter:counter + days]) / days

        f_out.write(f'{month}: {str(steps_average)}' + '\n')
        counter += days
