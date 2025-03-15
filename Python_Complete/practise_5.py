# # s = {20.5, 20.58, "20"}
# # print(s)
# # print(len(s)) 
# # s={}     # It is dictionary
# # a= type(s)
# # print(a)
# mydict={}
# a=input('Enter your favourite language chinu ')
# b=input('Enter your favourite language chinu ')
# c=input('Enter your favourite language chotu ')
# d=input('Enter your favourite language avinash ')
# e=input('Enter your favourite language arnav ')
# mydict['chinu']=a
# mydict['chinu']=b
# mydict['chotu']=c
# mydict['avinash']=d
# mydict['arnav']=e
# print(mydict.items())

# set= {8,7,12,"harry",5,6}
# print(set)

# a=int(input('Enter your age : '))
# if a>18:
#     print('You are adult')
# else:
#     print('GET LOST KIDDO')


number1=int(input('Enter no. 1 '))
number2=int(input('Enter no. 2 '))
number3=int(input('Enter no. 3 '))
number4=int(input('Enter no. 4 '))
if (number1>number4):
    g1=number1
else:
      g1=number4
if(number2>number3):
    g2=number2
else:
    g2=number3
if(g1>g2):
    print("The gratest no. is ", g1)
else:
    print("The grestest no. is ", g2)
if(g1==g2):
           print("No. ", g1 &g2, "are same")
