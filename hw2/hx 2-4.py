# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.




words = input('Введите несколько слов через пробел- ').split()

for i, word in enumerate(words):
    i +=1
    print(f'{i}, {word[:10]}')
















