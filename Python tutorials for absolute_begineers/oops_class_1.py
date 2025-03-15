class student:
    leave=10
    def printdetails(self):
        return f"Name is {self.name}. Standard is {self.std}, age is {self.age} and language is {self.language}"
        
    def __init__(self,aname,aage,astd,alanguage) -> None:
        self.name=aname
        self.age=aage
        self.std=astd
        self.language=alanguage
# harry=student()
# arnav=student()
arnav=student('Arnav',10,5,'Java')
harry=student('Harry',16,12,'Python')

# arnav.name='Arnav'
# harry.name='Harry'
# arnav.std=5
# harry.std=12
# harry.age=17
# arnav.age=10
# harry.language='python'
# arnav.language='java'
# print(arnav.language, arnav.age)
# print(arnav.__dict__)
# print(student.leave)
# arnav.leave=52
# print(arnav.leave)
# student.leave=56
# print(student.leave)

print(arnav.age)