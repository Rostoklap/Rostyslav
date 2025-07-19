lst = [0, 1, 4, 0, 5, 8]

no_zero = [elem for elem in lst if elem != 0]
zero = len(lst) - len(no_zero)

lst.clear()
lst.extend(no_zero)
lst.extend([0] * zero)

print(lst)
