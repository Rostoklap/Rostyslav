number = int(input("Введите 4-х значное число: "))

digit1 = number // 1000
# Например, вводим 1234. 1234/1000= 1.234 = 1
digit2 = (number % 1000) // 100
# Остаток от деления нацело числа 1234 % 1000 = 234, далее мы делим нацело 234 // 100 = 2
digit3 = (number % 100) // 10
# Остаток от деления нацело 1234 % 100 = 34, 34 // 10= 3
digit4 = number % 10
# 1234 % 10 = 1234 - ((1234 // 10) * 10)) = 4

print(digit1)
print(digit2)
print(digit3)
print(digit4)

