# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().



list_1 = list(input('введите числа - '))

list_len = len(list_1)
for i in range(1, list_len, 2):
    list_1[i-1], list_1[i] = list_1[i], list_1[i-1]
    print(list_1)











