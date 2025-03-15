# num1= int(input())
# num2= int(input())
# try:
#     print("The sum of; two numbers are ",(num1)+(num2))
# except Exception  as e:
#   print(e)
# print("this line is very important")

# x=89
# def harry():
#      x=20
#      def rohan():
#           global x
#           x=58
#           print("After calling harry ",x)
#      rohan()
#      print("After calling rohan",x)
# harry() 
# print(x)

# def fiboonacci (n):
#      if n==1:
#           return 0
#      elif n==2:
#           return 1
#      else:
#           return fiboonacci(n-1)+fiboonacci(n-2)
# n=fiboonacci(12)
# print(n)

# import random
# rand=random.randint(0,100)
# print(rand)
# rand=random.random()*100
# print(rand)
# channels=["starplus","colors","aajtak","znews"]
# rand=random.choice(channels)
# print(rand)
 
# import math
# a=math.cos(0)
# print(a)

# def funargs(normal, *argsrohan):
#      print(normal)
#      for item in argsrohan:
#           print(item)
# har =["harry",'rohan','the programmer']
# normal="i'm normal argument and the students are : "
# funargs(normal,*har)

import time
initial= time.time()
print("\n",initial)

k=0
while k<5:
   print(" Arnav ko maro thappad \n \t")
   k=k+1
   time.sleep(2)   #awesome function which delays the output
print("Time taken by the while loop to execute",time.time()-initial, " seconds\n" )

# initial2= time.time()
# print("\n",initial2)
# i=0
# for i in range(15):
#      print(" Arnav ko maro thappad ")
#      i=i+1
# print("Time taken by for loop to execute program is ",time.time()-initial2,"seconds.\n")


# import time
# localtime= (time.asctime(time.localtime(time.time())))
# print("\n",(localtime),"\n")