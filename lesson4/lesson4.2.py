lst = [1, 4, 6, 9, 8, 2]

if not lst:
    result = 0
else:
    sum_index = sum(lst[::2])
    result = sum_index * lst[-1]
    print(result)
