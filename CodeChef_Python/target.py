# # cook your dish here
# t = int(input())
# while (t > 0):
#     n, m = map(int,input().split())
#     z=5*n+7*m
#     print(z)
#     t -= 1

# n,a,b=map(int,input().split())
# x=n-a
# z=n-b-a
# print(f"{x} {z}")

t=int(input())
while(t>0):
    x,y,m=map(int,input().split())
    a=x*m
    if(a<y):
        print("Yes")
    else:
        print("No")
    t-=1