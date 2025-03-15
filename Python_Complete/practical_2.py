# Python Program to find Power of a Number

number = int(input(" Please Enter any Positive Integer : "))
exponent = int(input(" Please Enter Exponent Value : "))
power = 1

for i in range(1, exponent + 1):
    power = power * number
    
print("The Result of {0} Power {1} = {2}".format(number, exponent, power))

            ## my method ##

# number = int(input(" Please Enter any Positive Integer : "))
# exponent = int(input(" Please Enter Exponent Value : "))
# power= number ** exponent
# print(f"The result of {number} power {exponent} is {power}")
