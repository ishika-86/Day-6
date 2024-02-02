# make a new list that has only the even elements of this list in it.

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [num for num in a if not num & 1]
print(b)
