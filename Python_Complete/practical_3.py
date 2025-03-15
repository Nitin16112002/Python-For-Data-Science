# Write a Python program to find the maximum of a list of numbers.

list1 = []

num= int(input("\n Enter number of  elements in the list:- " ))

for i in range(num):
   element = int(input("Enter elements:- "))
   list1.append(element)

maxval=max(list1)
print("Largest element is: ", max(list1) )
list1.remove(maxval)
print(f"Second largest no. is {max(list1)}")