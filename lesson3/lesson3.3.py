lst = [4, 7, 8, 10, 11]

sep = (len(lst) + 1) // 2 # округление в большую сторону

lst_new = [lst[:sep], lst[sep:]]

print(lst_new)
