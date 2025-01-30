#rsplit
l=[]
s='this is a program'
parameter=input("enter the parameter to split")
n=int(input("enter the no. of times we need to perform split:"))
#splitiing from end 
while n>0 and parameter in s:
    split_index=s.rfind(parameter) #Finding the last occurence of parameter
    #inserting the part after parameter of string to list
    l.insert(0,s[split_index+len(parameter):])
    s=s[:split_index]  #updating string to continue
    n=n-1

l.insert(0,s)   #adding remaining string at beginning

print(l)

