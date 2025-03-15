# a=77
# b=48

def gcd(a,b):
    if(a==0):
        return b
    if(b==0):
        return 
    if(a==b):
        return a
    if (a>b):
        return gcd(a-b,b)
    return gcd(a,b-a)

def lcm(a,b):
    return (a//c)*b

for i in range (int(input())):
    a,b= map(int,input().split())

# z=int(input())
# while (z>0):
#     a=int(input())
#     b=int(input())
#     z=-1


c=gcd(a,b)
d=lcm(a,b)

print(f"The gcd of {a} and {b} is {c} \n")
print(f"The lcm of {a} and {b} is {d} \n")
