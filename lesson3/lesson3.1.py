a = int(input("Введите первое число :"))
b = int(input("Введите второе число :"))
action = input("Введите действие ( + , - , * , /): ")

if action == "+":
    print("Результат", a + b)
elif action == "-":
    print("Результат", a - b)
elif action == "*":
    print("Результат", a * b)
elif action == "/":
    if b == 0:
        print("0 нельзя!")
    else:
        print ("Результат", a / b)