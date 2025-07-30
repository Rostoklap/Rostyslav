number = int(input("Введите число: "))

while number > 9:
    x = 1
    for digit in str(number):
        x *= int(digit)
    number = x

print(number)
