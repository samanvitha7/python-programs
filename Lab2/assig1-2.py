"""Write a program that generates 100 random integers that are either 0 or 1. Then find the longest run of zeros, the largest
 number of zeros in a row. For instance, the longest run of zeros in [1,0,1,1,0,0,0,0,1,0,0] is 4"""


import random
l=[]
for i in range(100):
    temp=random.randint(0,1)
    l.append(temp)
"""for i in range(10):
    print(l[i])"""
maximum=0
count=0

for i in range(100):
    if l[i]==0:
        count+=1
        if count>maximum:
            maximum=count
        
    else:
        count=0
print("max number of consecutive zeroes is:",maximum)
        



