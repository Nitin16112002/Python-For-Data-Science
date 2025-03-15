# number=['5','9','3']
# number=list(map(int,number))
# # for i in range(len(number)):
# #     number[i]=int(number[i])
# a=number[1]+52
# print(a)

# num=[1,5,2,3,83,9,6,8]
# def square(a):
#     return a*a
# square=list(map(square,num))
# print(square)

# num=[1,5,2,3,83,9,6,8]
# square=list(map(lambda a:a*a,num))#using lambda
# print(square)

def square(a):  
    return a*a
def cube(a):
    return a*a*a
func=[square,cube]
for i in range(5):
    val=list(map(lambda x:x(i),func))
    print(val)
################## filter ############
# l1=[2,8,6,9,7,2,3,4,5,9,6]
# def greater_than_5(a):
#         return a>5
# gr_than_5=list(filter(greater_than_5,l1))
# print(gr_than_5)

################# reduce ####################

# list=[5,6,47,8]
# from functools import reduce
# num=reduce(lambda x,y:x+y,list)
# print(num)

