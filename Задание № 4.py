#  Пользователь вводит целое положительное число.
#  Найдите самую большую цифру в числе.
#  Для решения используйте цикл while и арифметические операции.

number = int(input())
number1 = number%10
number = number//10
while number > 0:
    if number%10 > number1:
        number1 = number%10
    number = number//10
print ( number1)