

a=6/5
b=a%1
print(b)



# def greet(name):
#     print("Good morning",name)
# name=str(input("Enter your name : "))
# print(greet(name))

# def sum(n1,n2):
#     return n1+n2
# s=sum(5,9)
# print(s)

# def result(marks='no marks'):
#     return ((marks[0]+marks[1]+marks[2])/300)*100
# marks=[96,88,65]

# # print(result(marks))

# def factorial(n):
#     if n==0 or n==1:
#         return 1

#     else:
#         return n*factorial(n-1)
# n=int(input("Enter a number : "))
# print("factorial of a number is : " , end=(""))
# print(factorial(n))

# def greatestno(n1,n2,n3):
#     if(n1>n2):
#         if(n1>n3):
#             return n1
#         else:
#             return n3
#     else:
#         if(n2>n3):
#             return n2
#         else:
#             return n3  
# n1=int(input("Enter the number : "))
# n2=int(input("Enter the number : "))
# n3=int(input("Enter the number : "))
# m = greatestno(n1,n2,n3)

# if(n1==n2==n3):
#     print("all are equal")        
# print("the greatest number is " + str(m))

# def temprature(cel):
#     return (cel * 9/5) + 32 
# c=0
# f = int(input("Enter the temprature  "))
# print("Temprature in farehnhite is " , temprature(f))

# def sum(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*((n+1)/2)
# n=int(input("Enter the number : ",))
# print("The sum of natural numbers upto",n,"is  ",end="")
# n=sum(n)
# print(str(n))
 
# n = 3
# for i in range(n):
#     print("*" * (n-i))

# n=int(input("Enter a number : "))
# n_original=n
# reverse=0
# while n>0:
#     reverse= reverse * 10 + n % 10
#     n//=10
# if(reverse==n_original):
#     print("The pelindrome  no. is ",reverse)
# else:
#     print("The no. is not pelindrome")

# def mean(n1,n2):
#     return (n1+n2)/2
# n1=int(input("Enter the num 1 : "))
# n2=int(input("Enter the num 2 : "))
# s=mean(n1,n2)
# print("The mean is ", s)