#PROGRAM TO FIND THE FACTORIAL OF A NUMBER

num=input("enter number whose factorial is to be found ")    # Taking input
num=int(num)
i=1      # Initialising
fact=1
while i<=num :

    fact=fact*i      #logic
    i+=1
print("Factorial of the entered number is ",fact)  # printing the value


