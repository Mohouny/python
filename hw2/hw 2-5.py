# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.


list = [9, 6, 4, 4, 3]
number = int(input('Введите число- '))
last_index = len(list)
i = 0
for num_in_list in list:
    i+=1
    if number > num_in_list:
        list.insert(i,number)
        break
    elif i == last_index:
        list.append(number)

print (list)


list = [9, 6, 4, 4, 3]
number = int(input('Введите число- '))
last_index = len(list)-1
for i, num_in_list in enumerate(list):
    if number > num_in_list:
        list.insert(i,number)
        break
    elif i == last_index:
        list.append(number)

print (list)






















