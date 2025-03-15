# cook your dish here
a=int(input())
while(t>0):
    s=str(input())
    t=str(input())
    
    r=''
    n=len(s)
    for i in range(0,n):
        if(s[i]==t[i]):
            r +='g'
        else:
            r +='b'
    print(r)
    a-=1