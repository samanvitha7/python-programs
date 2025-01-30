#count
cnt=0
num=int(input("enter the number u want to search"))
l=[1,4,6,7,7,4,7,2]
for i in l:
    if l[i]==num:
        cnt+=1

print("No. of times",num,"has appeared is",cnt)