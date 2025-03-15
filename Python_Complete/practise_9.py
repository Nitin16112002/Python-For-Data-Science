# with open ("abc.txt","r") as f:
#       a=f.read()
# # print(a)
# if 'twinkle' in a:
#     print("present")
# else:
#     print("absent")

# # with open ("abc.txt") as f:
# #     a=f.read()
# # print(a)
# # if  'arnav' in a:
# #     print('arnav is present')
# # else:
# #     print('not present')

# point=(int(input('Enter your score : \n')))
# def game():
#     return point
# score=game()
# with open ('highscore.txt','r') as f:
#     highscoreStr=f.read()
# if highscoreStr == '' :
#   with open ('highscore.txt','w') as f:
#     f.write(str(score))
# elif int(highscoreStr)<score:
#     with open ('highscore.txt','w') as f:
#         f.write(str(score))
#         print("\nYou broke the highscore record     ")
# elif int(highscoreStr)>score:
#      with open ('highscore.txt','r') as f:
#          print("Your score is less than the highest score\n")
#         #  f.write(str(score))
# print('\nHighscore is ' )
# with open ('highscore.txt') as f:
#  a=f.read()
# print(a)

# for i in range(2, 21):
#     with open(f"tables/Multiplication_table_of_{i}.txt", 'w') as f:
#         for j in range(1, 11):
#             f.write(f"{i}X{j}={i*j}")
#             if j!=10:
#                 f.write('\n')

# import sys
# sys.getrecursionlimit()

# Example of F STRING
# score=30
# run=5854
# book="junglebook"
# with open ('highscore.txt','w') as f:
# #         f.write(f"{score},{run},{book}")
# import matplotlib.pyplot as plt
# age={3,3,3,6,6,6,5,5,5,4,4,4,7,7,7,8,8,8,9,9,9,5,5,5,6,6,6,4,.4,4,8,8,8}
# plt.hist(age,bins=5)
# plt.show()


# def game():
#     return 55

# score = game()
# with open("highscore.txt") as f:
#     highScoreStr=f.read()

# if highScoreStr == '':
#     with open("highscore.txt",'w') as f:
#         f.write(str(score))

# elif int(highScoreStr)<score :
#          with open("highscore.txt",'w') as f:
#            f.write(str(score))
# import random
# def game():
#     score=random.randint(1,100)
#     print(f'The high score is {score}')
#     return score

# score = game()
# with open("highscore.txt") as f:
#     highScoreStr = f.read()
    
# if highScoreStr=='':
#     with open("highscore.txt", "w") as f:
#         f.write(str(score))

# elif int(highScoreStr)<score :
#     with open("highscore.txt", "w") as f:
#         f.write(str(score))

# with open("arnav.txt") as f:
#     t=f.read()
# if 'donkey' in t:
#     print('Donkey is present') 

# else :
#     print("Donkey is not present")

# t=t.replace('donkey','######')
# with open("arnav.txt",'w') as f:
#      f.write(t)

# with open("arnav.txt") as f:
#     t=f.read()
# with open("arnav2.txt",'w') as g:
#         g.write(t)

# with open("arnav.txt") as f:
#     t=f.read()
# with open("arnav2.txt") as f:
#     s=f.read()
# if t==s:
#     print("files are identical")
# else:
#     print("Not matched")
import os
oldfile=input(" Enter the name of the oldfile to replace")
newfile=input(" Enter the name of the new file")
with open(oldfile) as f:
    t=f.read()
with open(newfile,'w') as f:
    g=f.write(t)
os.remove(oldfile)