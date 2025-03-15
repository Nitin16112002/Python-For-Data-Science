# # Python program to find the factorial of a number  input taken from the user.

# num = int(input("Enter a number: "))

# factorial = 1

# if num < 0:
#    print("Sorry, factorial does not exist for negative numbers")
# elif num == 0:
#    print("The factorial of 0 is 1")
# else:
#    for i in range(1,num + 1):
#        factorial = factorial*i
#    print("The factorial of",num,"is",factorial)

def print_count_times(n):
 # set count to 0
 count = 0
#  n=5
 while count < n:
   print("Hello World!")
 # increment count
   count += 1

if __name__ == '__main__':
 # number of times we want to print 
 n = 10
 # call our function to print n times.
 print_count_times(n)