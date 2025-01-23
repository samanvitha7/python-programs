'''You are given a number N, you need to print the number of positions where digits exactly
 divides N.'''
cnt=0
testcases=int(input("Enter no. of testcases"))
for i in range(testcases):
    num=input("Enter the number")
    cnt=0
    for digit in num : 
        if digit != '0':
            if int(num) % int(digit) == 0 :
                cnt+=1
    
    print("Number of positions where it is exactly divisible ",cnt)

