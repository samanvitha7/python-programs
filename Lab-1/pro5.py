#TO REVERSE OF A GIVEN NO

num=input("Enter a number")
num=int(num)
rem=0
reverse=0
while num>0:
    rem=num%10
    reverse=reverse*10+rem
    num=num//10
print("Reverse of the entered number is ",reverse)