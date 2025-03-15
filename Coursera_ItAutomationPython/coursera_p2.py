# def print_prime_factors(number):
#   # Start with two, which is the first prime
#   factor = 2
#   # Keep going until the factor is larger than the number
#   while factor <= number:
#     # Check if factor is a divisor of number
#     if number % factor == 0:
#       # If it is, print it and divide the original number
#       print(factor)
#       number = number / factor
#     else:
#       # If it's not, increment the factor by one
#       factor+=1
#   return "Done"

# print_prime_factors(100)
# # Should print 2,2,5,5
# # DO NOT DELETE THIS COMMENT


# # def print_prime_factors(number):
# # # Start with two, which is the first prime
# #     factor = 2
# #     # Keep going until the factor is larger than the number
# #     while factor <= number:
# #     # Check if factor is a divisor of number
# #         if number % factor == 0:
# #     # If it is, print it and divide the original number
# #             print(factor)
# #             number = number / factor
# #         else:
# #     # If it's not, increment the factor by one
# #             factor += 1
# #             return "Done"
# # print_prime_factors(100)
# # # Should print 2,2,5,5
# # # DO NOT DELETE THIS COMMENT



# def sum_divisors(n):
#   sum = 0
#   a=1
#   if(n==0):
#     return 0
#   elif(n>1):
#     while(a<n):
#         if(n%a==0):
#             sum+=a
            
#         a+=1
#     else:
#             a+=1
#     return sum
    
#   # Return the sum of all divisors of n, not including n
  


# # def sum_divisors(n):
# #     i = 1
# #     sum = 0
# #     # Return the sum of all divisors of n, not including n
# #     while i < n:
# #      if n % i == 0:
# #         sum += i
# #      i +=1
# #     else:
# #      i+=1
# #     return sum

# print(sum_divisors(0))
# # 0
# print(sum_divisors(3)) # Should sum of 1
# # 1
# print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# # 55
# print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# # 114



# def factorial(n):
#     result = 1
#     for x in range(1,n+1):
#         result = result * x
#     return result

# for n in range(1,10):
#     print(n, factorial(n))


# def is_power_of(number, base):
#   # Base case: when number is smaller than base.
#   a= False
#   if number < base:
#       print(a)
#     # If number is equal to 1, it's a power (base**0).
#   else:
#     for i in range (base,number):
#       if(number==(base**i)):
#         return True

#   # Recursive case: keep dividing number by base.
#   return is_power_of(number,base)

# print(is_power_of(8,2)) # Should be True
# print(is_power_of(64,4)) # Should be True
# print(is_power_of(70,10)) # Should be False


# def is_power_of(number, base):
# # Base case: when number is smaller than base.
# 	if number ==1:
# 		return True
# 	if number < base:
# 	# If number is equal to 1, it's a power (base**0).
# 		return False
# 	number /= base
# 	# Recursive case: keep dividing number by base.

# 	return is_power_of(number, base)

# print(is_power_of(8,2)) # Should be True
# print(is_power_of(64,4)) # Should be True
# print(is_power_of(70,10)) # Should be False

# def digits(n):
# 	count = 0
# 	if n == 0:
# 	  return 1
# 	elif(n>0):
# 		for i in str(n):
# 			count=count+i		
# 	return count



# Complete the function digits(n) that returns how many digits the number has. For example: 25 has 2 digits and 144 has 3 digits. Tip: you can figure out the digits of a number by dividing it by 10 once per digit until there are no digits left.

# def digits(n):
# 	count=0
# 	if n==0:
# 		count=1
# 		return count
# 	while (n>0):
# 		count+=1
# 		n=n//10
# 		print
# 	return count

# print(digits(25)) # Should print 2
# print(digits(144)) # Should print 3
# print(digits(1000)) # Should print 4
# print(digits(0)) # Should print 1
# # Output: 2, 3, 4, 1


# def multiplication_table(start, stop):
# 	for x in range(start,(stop+1)):
# 		for y in range(start,(stop+1)):
# 			print(str(x*y), end=" ")
# 		print()

# multiplication_table(1, 3)
# # Should print the multiplication table shown above


# def counter(start, stop):
# 	x = start
# 	if start > stop:
# 		return_string = "Counting down: "
# 		while x >= stop:
# 			return_string += str(x) 
# 			if x > stop:
# 				return_string += ","
# 			x -= 1
# 	else:
# 		return_string = "Counting up: "
# 		while x <= stop:
# 			return_string += str(x) 
# 			if x < stop:
# 				return_string += ","
# 			x += 1
# 	return return_string

# print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
# print(counter(2, 1)) # Should be "Counting down: 2,1"
# print(counter(5, 5)) # Should be "Counting up: 5"


def votes(params):
	for vote in params:
	    print("Possible option:" + vote)


votes(['yes', 'no', 'maybe'])-