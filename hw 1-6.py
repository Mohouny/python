
result_day = int(input('Введите результат в 1ый день - '))
result_total = int(input('Введите желаемый результат - '))

day = 0

while result_day < result_total:
    result_day = result_day * 1.1
    day = day + 1
print(f'Вы достигли результат на {day} день')




