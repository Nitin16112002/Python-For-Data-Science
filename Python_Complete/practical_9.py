# # Write a pyhton program to search in a list of elements using linear search technique.
# list1 = [1,2,3,4,5]
# key = int(input('Please enter the number you want to search : '))
# flag = 0
# for i in range(len(list1)):
#     if key == list1[i]:
#           flag = 1
# if flag == 0:
#     print("Key not found")    
# else:
#         print("Key found")   


# Write a pyhton program to search in a list of elements using linear search technique.
list1 = [1,2,3,4,5]
key = int(input('Please enter the number you want to search : '))
flag = 0
check= -1
for i in range(len(list1)):
    if key == list1[i]:
          flag = 1
          check= i
          break
if flag == 0:
    print("Key not found")    
else:
        print(f"Key found at index {check}")   
        
