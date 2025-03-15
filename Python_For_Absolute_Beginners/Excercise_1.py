dicr={
    "Zenitsu":"ThunderBreathing",
    "Tanjiro":"WaterBreathing"
}
print(type(dicr))
print(dicr.keys())
a=input("Enter the word of which u want meaning: ")

if a in dicr:
        print(dicr.get(a))
else:
    print("WordOutOfDictionary")

    # b=dicr.get(a)
    # print(b)

# print(dicr.values())