l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 54, 23, 55, 90, 60]
a=filter(lambda i:i%5==0,l)
print(list(a))
print(type(a))