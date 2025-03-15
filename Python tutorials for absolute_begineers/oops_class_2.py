class student:
    leave=15
    def printdetails(self):
        return f"Name is {self.name}. Standard is {self.std}, age is {self.age} and language is {self.language}"
        
    def __init__(self,aname,aage,astd,alanguage) -> None:
        self.name=aname
        self.age=aage
        self.std=astd
        self.language=alanguage

    @classmethod
    def change_leaves(cls,newleaves):
        cls.leave=newleaves

    @classmethod
    def from_dash(cls,string):
        # params=string.split('-')
        # print(params)
        # return cls(params[0],params[1],params[2],params[3])
        return cls(*string.split('-'))    

arnav=student('Arnav',10,5,'Java')
harry=student('Harry',16,12,'Python')
karan=student.from_dash("Karan-14-10-C++")
harry.change_leaves(85)
print(karan.age)