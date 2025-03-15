import matplotlib.pyplot as plt

x1=[1,2,3]
y1=[2,4,1]

plt.plot(x1,y1,label="line 1")

x2=[1,2,3]
y2=[4,1,3]

plt.plot(x2,y2,label="line 2")

import matplotlib.pyplot as plt

n=int(input("How many do you want to read?"))
pulse=[]
height=[]
for i in range(n):
    x= int(input("PULSE-->"))
    pulse.append(x)
    y=float(input('Height-->'))
    height.append(y)
plt.plot(pulse,height)
plt.xlabel('PULSE')
plt.ylabel('Height')
plt.title('Pulse-Height Graph')
plt.show()
