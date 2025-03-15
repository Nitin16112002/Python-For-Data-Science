import sys
file = open("monuments.txt","r+")
wordcount={}
for word in file.read().split():
    if word  not in wordcount:
        wordcount[word]=1
    else:
        wordcount[word]+=1
print(word,wordcount)
file.close()
