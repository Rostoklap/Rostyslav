import string
import keyword

name = input("Введите имя переменной: ")

if name and name[0] in "0123456789":
    print(False)

elif any(c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for c in name):
    print(False)

elif any(c in (string.punctuation.replace("_", "") + " ") for c in name):
    print(False)

elif name in keyword.kwlist:
    print(False)

elif name.count("_") == len(name) and len(name) > 1:
    print(False)

else:
    print(True)
