a=int(input("Enter the first number:- "))
operator=input("Enter the Operator:- ")
b=int(input("Enter the second number:- "))

if(a==45 and b==3 and operator=='*'):
    print("455")
elif(a==56 and b==9 and operator=='+'):
    print("77")
elif(a==56 and b==6 and operator=='/'):
    print("4")
elif(operator=='+'):
    print(a+b)
elif(operator=='-'):
    print(a-b)
elif(operator=='*'):
    print(a*b)
elif(operator=='/'):
    print(a/b)

else:
    print("Invalid input!!!!")