l=[1,2,3,4,5,6,7,8,9,10]

# l2=[ item for item in l if item==2 or item==4 or item==6]
# print(l2)

for index, i in enumerate(l):
    if index==2 or index==4 or index==6:
        print(index,i)
