# f=open("sample.txt",'r')
# text=f.readline()
# print(text)
# f.close()

# with open ("sample.txt") as f:
#     a=f.read()
#     if "harry" in a:
#         print("Yes")
#     else:
#         print("No")
#     print(a)



# def game(a):
#     return a
# points=int(input("Enter your score:-"))
# score=game(points)
# with open("highscore.txt") as f:
#    highscore= f.read()
 
# if highscore=="":
#         with open ("highscore.txt",'w') as f:
#             f.write(str(score))
# elif int(highscore)<score:
#     with open ("highscore.txt",'w') as f:
#             f.write(str(score))



# for i in range(2, 21):
#     with open(f"Multiplication_Table_Of_{i}.txt",'w') as f:
#      for j in range(1, 11):
#             f.write(f"{i}X{j}={i*j} \n")

# with open ("another.txt") as f:
#     a=f.read()
#     print(a)
#     if "donkey" in a:
#         print("Yes")
# content=a.replace("donkey","@@@@@@@")
# with open ("another.txt",'w') as f:
#         f.write(content)

# class RailwayForm():
#     def PrintDetails(self):
#         print(f"The name is {self.name} ")
#         print(f"The city is {self.city} ")

# ram=RailwayForm()
# ram.name="Haary"
# ram.city="Purnea"
# ram.PrintDetails()

# class programmer:
#     company="Microsoft"
#     def details(self):
#         print(f"The name is {self.name}")
#         print(f"The company is {self.company}")
#         print(f"The age is {self.age}")

# harry=programmer()
# harry.name="HarrryRajput"
# harry.age=19
# harry.details()

# sam=programmer()
# sam.name="SamirBam"
# sam.age=19
# sam.company="YouTube"   
# sam.details()


# class Calculator:
#     def square(self,num):
#         self.number=num
#         print(f"The square of {num} is {num**2}")

#     def squareroot(self,num):
#         self.number=num
#         print(f"The squareroot of {num} is {num**0.5}")

#     def cube(self,num):
#         self.number=num
#         print(f"The cube of {num} is {num**3}")

#     @staticmethod
#     def greet():
#         print("Hello Everyone")
        

# casio=Calculator()
# casio.square(3)
# casio.squareroot(10)
# casio.cube(4)
# casio.greet()





# class IndianRailways:

#     def __init__(self,name,seat,fare):
#         self.name=name
#         self.seat=seat
#         self.fare=fare

#     @staticmethod
#     def greet():
#         print("Hello Everyone")

#     def getStatus(self):
#             print(f"The name of the train is {self.name}")
#             print(f"The seat available on the train is {self.seat}")
#             print(f"The fare of the train is {self.fare}")
    
#     def bookTicket(self):
#         print("Payment succesfull ")
#         print(f"Your seat on train {self.name} is seat no. {self.seat}")
#         self.seat=self.seat-1

# harry=IndianRailways("RajDhani Express",32,"55$")
# harry.greet()
# harry.getStatus()
# harry.bookTicket()
# harry.bookTicket()





# class employee:
#     company="Google"
#     salary=600
#     salarybonus=200

#     @property
#     def totalsalary(self):
#         return self.salary+self.salarybonus

#     @totalsalary.setter
#     def totalsalary(self,val):
#         self.salarybonus=val-self.salary

# man=employee()
# man.totalsalary=900
# print(man.totalsalary)
# print(man.salarybonus)






class animal:
    @staticmethod
    def greet():
        print("I'm a animal")

class dog(animal):
    @staticmethod
    def bark():
        print("Bow Bow")

class pet(dog):
    @staticmethod
    def order():
        print("You are ordered to sit down")


a=animal()
a.greet()

d=dog()
d.greet()
d.bark()

p=pet()
p.greet()
p.bark()
p.order()

