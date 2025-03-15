#Write a program to show the grade of the student.
subject1=int(input("Enter the marks you obtained in sub1:"))
subject2=int(input("Enter the marks you obtained in sub2:"))
subject3=int(input("Enter the marks you obtained in sub3:"))
total=(subject1+subject2+subject3)/3
print(" Your total percentage is ", total)
if total>=80:
    print("Your grade is = A")
elif total>=70:
    print("Your grade is = B")
elif total>=60: 
    print("Your grade is = C")
else:
    print("Your grade is = D")