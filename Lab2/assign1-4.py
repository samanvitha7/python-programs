"""Take numbers from 1 to 10000. Create equivalence classes for modulo 5 on this set of numbers.
 Check the validity of your equivalence classes. [Hint: the union of all equivalence 
   should be the original set/list.]"""

# creating list to store its respective elements
l_rem_0=[]
l_rem_1=[]
l_rem_2=[]
l_rem_3=[]
l_rem_4=[]
#storing elements to the list
for i in range(1,10001):
    if i%5==0:
        l_rem_0.append(i)
    elif i%5==1:
        l_rem_1.append(i)
    elif i%5==2:
        l_rem_2.append(i)
    elif i%5==3:
        l_rem_3.append(i)
    elif i%5==4:
        l_rem_4.append(i)
l_sum=l_rem_0+l_rem_1+l_rem_2+l_rem_3+l_rem_4
l_original=list(range(1, 10001))
if sorted(l_sum) == l_original:
    print("Equivalence classes are valid")
else:
    print("Invalid equivalence classes")