# t=int(input())
# while(t>0):
#     x,y,z=map(int,input().split())
#     a=z-y
#     b=a//x
#     print(b)
#     t -= 1

# t=int(input())
# while(t>0):
#     x=int(input())
#     a=(10*x)/100
#     # c=x-a
    
#     # print(a)
#     v=100
#     # b=x-v
#     if(a>v):
#         print(a)

#     else:
#         print(v)
#     t-= 1


t=int(input())
while(t>0):
    n,x=map(int,input().split())
    a=x*n
    b=a%4
    c=a//4
    if (b==0):
        print(c)
    elif(n==0 or x==0):
        print("0")
    else:
        print(c+1)
    t-=1