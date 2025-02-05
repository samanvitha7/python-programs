"""You are given a integer, N. Write a program to determine if N is an element of the Fibonacci
 Sequence.The first few elements of Fibonacci sequence are 0,1,1,2,3,5,8,13...... A Fibonacci 
 sequence is one where every element is a sum of the previous two elements in the sequence.
   The first two elements are 0 and 1."""

def isfib(n):
    temp=check(5*n*n-4) or check(5*n*n+4)
    if temp==1:
        print("isfibo")
    else:
        print("isnotfibo")

def check(n):
    square_root=n**0.5
    return square_root.is_integer()
__name__
l=[]
testcases=int(input("Enter no. of testcases:"))
for i in range(testcases):
    num=int(input("enter number"))
    l.append(num)
for i in range(len(l)):
    isfib(l[i])