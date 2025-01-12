#codedocs admin kidnap

test_cases=int(input("Enter number of test cases"))
boxes=input("enter number of boxes:")
pos=input("enter the box number of gold coin:")
swaps=input("enter number of swaps:")
boxes=int(boxes)
pos=int(pos)
swaps=int(swaps)
i=1
while i<=swaps:
    #taking input of two boxes which are to be swaped
    box1=int(input("enter the box number:"))
    box2=int(input("enter the box number:"))
    if pos==box1:
        pos=box2
    elif pos==box2:
        pos=box1
    
    temp=box1
    box1=box2
    box2=temp
    i+=1
print("gold coin is present at ",pos,"th position")




