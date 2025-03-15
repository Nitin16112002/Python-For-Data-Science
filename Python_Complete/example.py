# Write a program to read n integers and display them as histograms.
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

n=int(input("How many do you want to read?"))
alist=[]

for i in range(n):
    x=int(input('-->'))
    alist.append(x)
num_bins=10
n,bins,patches = plt.hist(alist,num_bins,facecolor='blue', alpha=0.5)
plt.show()