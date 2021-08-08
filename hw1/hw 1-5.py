

earn = float(input('Введите выручку - '))
cost = float(input('Введите издержки - '))
result = earn - cost

profit = earn > cost
loss = cost > earn

if profit:
    print(f'Выручка больше издержек и составляет {result:.2f}')
    proceeds = earn / cost
    print(f'Рентабельность фирмы составляет - {proceeds:.2f}%')
    staff = int(input('Количество сотрудников составляет - '))
    print(f'Прибыль фирмы в расчете на 1-го сотрудника составляет - {result/staff:.2f}')
else:
    print('Издержки больше выручки')














