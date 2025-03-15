def multable(num):
    l=[i*num for i in range(1,11)]
    print(l)
    with open("tables.txt",'a') as f:
        f.write(str(l))
        f.write('\n')

number=int(input("Enter the number of which you want multiplication table of: "))
multable(number)
number=int(input("Enter the number of which you want multiplication table of: "))
multable(number)