# class programmer:
#     company="Microsoft"
#     def information(self):
#         print(f"Name of the programmer is {self.name} age is {self.age} and works in company {self.company}")

# harry=programmer()
# raju=programmer()
# harry.name="Harry"
# harry.age=25
# raju.name="Raju"
# raju.age=18
# harry.information()
# raju.information()
# *************************************************************************************
# class programmer:
#     company="Microsoft"
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def information(self):
#         print(f"Name of the programmer is {self.name} age is {self.age} and works in company {self.company}")

# harry=programmer("harry",25)
# raju=programmer("Raju",13)
# harry.information()
# raju.information()
# ***************************************************************************************

# class calculator:
#     def squareroot(self):
#      print(self.num*self.num)
#     def cuberoot(self):
#       print (self.num*self.num*self.num)

# num1=calculator()
# num1.num=3
# num1.squareroot()
# num1.cuberoot()
# ****************************************************************************************

# class calculator:
#     def __init__(self,num):
#         self.number=num
#     def square(self):
#         print(f"The value of {self.number} square is {self.number**2}")
#     def cube(self):
#         print(f"The value of {self.number} cube is {self.number**3}")
#     def squareroot(self):
#         print(f"The value of {self.number} squareroot is {self.number**0.5}")
#     @staticmethod
#     def greet():
#         print(" ********Hello everyone********")

# a=calculator(9)
# a.square()
# a.greet()
# a.squareroot()
# a.greet()
# a.cube()
# a.greet()
# **************************************************************************************

class train:
    company="indianrailways"
    def __init__(self,name,seat):
        self.name=name
        self.seat=seat
    def display(self):
        print(f"The number of seats in {self.name} train  is {self.seat}")
    def bookticket(self):
        if(self.seat<0):
            print("Sorry! No seats available|||")
        else:
            print(f"Your ticket is confirmed! Your seat number is {self.seat}")
            self.seat=self.seat-1

raju = train("Rajdhani",22)
raju.display()
raju.bookticket()
raju.bookticket()
        
 
