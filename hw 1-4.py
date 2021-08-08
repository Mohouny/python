




number = int(input('Введите целое положительное число- '))
max = number % 10
num = number

while num > 0:
    num2 = num % 10
    if num2 > max:
        max = num2

    num = num //10

print(f"Самая большая цифра в числе {number} - {max}")



