result = ''
counter = 0
days_in_months = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

with open('input.txt', 'r', encoding='utf-8') as f_in:
    lines = f_in.readlines()
    current_date = lines[0].strip()
    current_day = int(current_date[:2])
    current_month = int(current_date[3:])
    num_of_cells = lines[1].strip()
    lines = lines[2:]

    for line in lines:
        cell_id, date = line.split()
        day = int(date[:2])
        month = int(date[3:])

        if month == current_month:
            if current_day - day > 3:
                result += cell_id + '\n'
        elif current_month - month > 1:
            result += cell_id + '\n'
        else:
            try:
                days_cell_occup = current_day + (days_in_months[month] - day)
                if days_cell_occup > 3:
                    result += cell_id + '\n'
            except KeyError:
                print(month, day)

with open('output.txt', 'w', encoding='utf-8') as f_out:
    f_out.write(result)
