from functools import reduce
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 54, 23, 55, 90, 60]

a=reduce(min,l)
a=reduce(max,l)
print(a)