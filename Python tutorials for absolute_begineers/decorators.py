# def func1():
#     return"hello everone"
# func2=func1
# del func1
# print(func2())
 
# def func1(num):
#      if num==0:
#          return print
#      if num==1:
#          return int
# a=func1(1)
# print(a)

def dec1(func1):
    print("Code is executing")
    func1()
    print("Code has been executed")
    return dec1
@dec1
def harry():
    print("Harry is a coder")

