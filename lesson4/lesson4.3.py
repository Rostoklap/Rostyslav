import random

lst = [random.randint(0,70) for _ in range(random.randint(3,10))]

result = [lst[0], lst[2], lst[-2]]

print(lst)
print(result)
