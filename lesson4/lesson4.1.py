lst = [0, 1, 4, 0, 5, 8]

no_zero = [elem for elem in lst if elem != 0]
zero = [0] * (len(lst) - len (no_zero))
lst = no_zero + zero
print(lst)
