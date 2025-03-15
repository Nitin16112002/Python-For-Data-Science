# import random

# number=random.randint(1,99)
# # def guess():
# print(number)
# # n=5
# i=0
# for i in range(0,5):
#     a=int(input("Enter the guess:-"))
#     if(a==number):
#         print("Congrats!!")
#         break
#     else:
#         print("Better Luck Next Time")


# if(a!=number):
#     print("Out of guess.")
# else:
#     print("Game Over")

# guess()


    
# print(random.randint(1,99))





import random

from scipy.misc import electrocardiogram

number=random.randint(1,99)
# def guess():
print(number)
# n=5
i=0
while i<5:
    a=int(input("Enter the guess:-"))
    if(a==number):
        print("Congrats!!")
        break
    elif(a<number):
        print("you enter less number please input greater number")
    else:
        print("you enter greater number please input smaller number")


    i=i+1

if(a!=number):
    print("Out of guess.")
else:
    print("Game Over")