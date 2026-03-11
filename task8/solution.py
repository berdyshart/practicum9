days_in_months = {
    'Январь': 31,
    'Февраль': 28,
    'Март': 31,
    'Апрель': 30,
    'Май': 31,
    'Июнь': 30,
    'Июль': 31,
    'Август': 31,
    'Сентябрь': 30,
    'Октябрь': 31,
    'Ноябрь': 30,
    'Декабрь': 31
}
counter = 0
months = days_in_months.keys()

with open('input.txt', 'r', encoding='utf-8') as f_in:
    steps_per_day = f_in.readlines()
    steps_per_day = [int(steps) for steps in steps_per_day]

with open('output.txt', 'w', encoding='utf-8') as f_out:
    for month in months:
        days = days_in_months[month]
        steps_average = sum(steps_per_day[counter:counter+days]) / days

        f_out.write(f'{month}: {str(steps_average)}' + '\n')
        counter += days
