#Write a program to display the first n terms of Fibonacci series.(without recursion)

a= int(input("Enter the first number of the series "))
b= int(input("Enter the second number of the series "))
n= int(input("Enter the  number of terms needed  "))
print(f"{a}, {b} ",end=",")
while(n!=0):
    c=a+b
    a=b
    b=c
    print(c,end=", ")
    n=n-1