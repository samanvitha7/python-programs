#hallowen party

def pieces(num):
    num1=num//2
    num2=num-num1
    max=num1*num2
    return max

__name__
l=[]
testcases=int(input())     #enter no. of testcases
for i in range(testcases):
    k=int(input())       #enter no. of testcases
    l.append(k)
for i in l:
    chocolate_pieces=pieces(i)
    print(chocolate_pieces)
