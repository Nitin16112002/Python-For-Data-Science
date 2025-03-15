# def is_palindrome(input_string):
# 	# We'll create two strings, to compare them
# 	new_string = (input_string.lowercase)
# 	reverse_string = ""
# 	# Traverse through each letter of the input string
# 	for ___:
# 		# Add any non-blank letters to the 
# 		# end of one string, and to the front
# 		# of the other string. 
# 		if ___:
# 			new_string = ___
# 			reverse_string = ___
# 	# Compare the strings
# 	if ___:
# 		return True
# 	return False

# print(is_palindrome("Never Odd or Even")) # Should be True 
# print(is_palindrome("abc")) # Should be False
# print(is_palindrome("kayak")) # Should be True

# def replace_ending(sentence, old, new):
# 	# Check if the old string is at the end of the sentence 
# 	if old.endswith(new):
# 		# Using i as the slicing index, combine the part
# 		# of the sentence up to the matched string at the 
# 		# end with the new string
# 		a=len(new)
# 		b=len(old)
# 		z=b-a
# 		print(z)
# 		i =old.slice(0,z)
# 		print(i)
# 		new_sentence = i+new
# 		# return new_sentence

# 	# Return the original sentence if there is no match 
# 	# return sentence
	
# print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# # Should display "It's raining cats and dogs"
# # print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# # # Should display "She sells seashells by the seashore"
# # print(replace_ending("The weather is nice in May", "may", "april")) 
# # # Should display "The weather is nice in May"
# # print(replace_ending("The weather is nice in May", "May", "April")) 
# # # Should display "The weather is nice in April"



# old="cat and cat"
# new="cat"
# print(old.endswith(new))

# filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# # Generate newfilenames as a list containing the new filenames
# # using as many lines of code as your chosen method requires.
# newfilenames=[]

# for i in filenames:
#     if (i.endswith(".hpp")):
#         i=i.replace(".hpp",".h")
#         newfilenames.append(i)
#     else:
#         newfilenames.append(i)

# print(newfilenames) 
# # Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

# def pig_latin(text):
#   # Separate the text into words
#   words = text.split()
#   say = []
#   for word in words:
    
#         word=word[1:]+ word[0]+ 'ay'
#         say.append(word)
#         return ' '.join(say)  


    
# print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
# print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"

# def pig_latin(text):
#   say = ""
#   words = text.split()
#   for word in words:
#     endString = str(word[1]).upper()+str(word[2:])
#     them = endString, str(word[0:1]).lower(), 'ay'
#     word = ''.join(them)
#     return word

# print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
# print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"


# def guest_list(guests):
# 	for guest in guests:
# 		name, age, job = guest
# 		print("{} is {} years old and works as {}".format(name, age, job))

# guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

# #Click Run to submit code
# """
# Output should match:
# Ken is 30 years old and works as Chef
# Pat is 35 years old and works as Lawyer
# Amanda is 25 years old and works as Engineer
# """


# def email_list(domains):
# 	emails = []
# 	for domain in domains:
# 	  for user in domains[domain]:
# 	      emails.append("{}@{}".format(user,domain))
# 	return(emails)

# print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))


# def groups_per_user(group_dictionary):
# 	user_groups = {}
# 	# Go through group_dictionary
# 	for group, users in group_dictionary.items():
# 		# Now go through the users in the group
# 		for user in users:
# 			if user not in user_groups:
# 				user_groups[user] = []
# 			user_groups[user].append(group)
# 			# Now add the group to the the list of
# # groups for this user, creating the entry
# # in the dictionary if necessary

# 	return((user_groups))

# print(groups_per_user({"local": ["admin", "userA"],
# 		"public":  ["admin", "userB"],
# 		"administrator": ["admin"] }))

# wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
# new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
# wardrobe.update(new_items)
# print(wardrobe)


# def format_address(address_string):
#     st,num,st2 = address_string.split(' ',2)
#     # return f"house number {num} on street named {st}"
#     print(num)
#     print(st)
#     print(st2)

# print(format_address("123 Main Street a"))

# def format_address(address_string):
#   # Declare variables
#   housen=''
#   streetn=""

#   # Separate the address string into parts

#   # Traverse through the address parts
#   for i in address_string:
#     if i.isdigit():
#       housen+=i
#     else:
#       streetn+=i
#     # Determine if the address part is the
#     # house number or part of the street name

#   # Does anything else need to be done 
#   # before returning the result?
  
#   # Return the formatted string  
#   return "house number {} on street named {}".format(housen,streetn)

# print(format_address("123 Main Street"))
# # Should print: "house number 123 on street named Main Street"

# print(format_address("1001 1st Ave"))
# # Should print: "house number 1001 on street named 1st Ave"

# print(format_address("55 North Center Drive"))
# # Should print "house number 55 on street named North Center Drive"



# class Person:
#     apples = 0
#     ideas = 0

# johanna = Person()
# johanna.apples = 1
# johanna.ideas = 1

# martin = Person()
# martin.apples = 2
# martin.ideas = 1

# def exchange_apples(you, me):

#     temp=you.apples
#     you.apples=me.apples
#     me.apples=temp
#     return you.apples, me.apples
    
# def exchange_ideas(you, me):

#     you.ideas +=me.ideas
#     me.ideas=you.ideas
#     return you.ideas, me.ideas

# exchange_apples(johanna, martin)
# print("Johanna has {} apples and Martin has {} apples".format(johanna.apples, martin.apples))
# exchange_ideas(johanna, martin)
# print("Johanna has {} ideas and Martin has {} ideas".format(johanna.ideas, martin.ideas))

class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom=bottom
        self.top=top
        self.current=current
    def up(self):
        """Makes the elevator go up one floor."""
        self.current+=1
        return self.current
    def down(self):
        """Makes the elevator go down one floor."""
        self.current-1
        return self.current
    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        return self.floor

elevator = Elevator(-1, 10, 0)



