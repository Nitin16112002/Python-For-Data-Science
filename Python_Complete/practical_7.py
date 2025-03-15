def circle():
   print("You've chosen Circle")
   r=int(input("Enter the radius: "))
   area1=3.14*(r**2) 
   print("Area of the circle with radius ",r," units is ", area1," square units.")

def square():
   print("You've chosen Square")
   s=int(input("Enter the side: "))
   area2=s**2 
   print("Area of the square with side ",s," units is ",area2," square units.")

def rectangle():
   print("You've chosen Rectangle")
   l=int(input("Enter the length of the rectangle: "))
   b=int(input("Enter the breadth of the rectangle: "))
   area3=l*b 
   print("Area of the rectangle with length and breadth ",l,",",b," units is ",area3," square units.")

print("1. Circle\n""2. Square\n""3. Rectangle\n")
choice=int(input("Enter your choice: "))
if choice==1:
   circle()
elif choice==2:
   square()
elif choice==3:
   rectangle()
else:
   print("Wrong Choice")
