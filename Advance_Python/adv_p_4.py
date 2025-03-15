# from decimal import DivisionImpossible


def division(a,num):
    try:
        b=a/num
        print(b)
    except ZeroDivisionError as e:
        print("Infinite")
    else:
        print("Succesfully found the division")

a=int(input("Enter the number : "))
num=int(input("Enter the number : "))
division(a,num)