print(' \n Here are the choices:-')

print("1. Fahrenheit to Celsius")
print("2. Celcius to Fahrenheit")
print("3. Exit")

selection=int(input("Enter your choice:-"))
    
if selection==1:
    print("Fahrenheit to Celsius:")
    F = int(input("Enter a temperature in Fahrenheit."))
    C = (F-32)*5.0/9.0
    print("Temperature:", F, "Fahrenheit")          
    print("Temperature:", C, "Celsius") 
elif selection==2:
    print(" Celsius to Fahrenheit:")
    C = int(input("Enter a temperature in Celsius."))
    F = 9.0/5.0 * C + 32
    print("Temperature:", C, "Celsius")  
    print("Temperature:", F, "Fahrenheit") 
elif selection==3:
    exit    
else:
    print('''Invalid Choice. 
    Enter choice between 1 to 3''')

