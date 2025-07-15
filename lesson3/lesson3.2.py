lst= [24, 45, 56, 78, 89]

if len(lst) > 1:
    lst = [lst[-1]] + lst[:-1]

print(lst)
