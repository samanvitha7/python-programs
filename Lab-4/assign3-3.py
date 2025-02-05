'''The Utopian tree goes through 2 cycles of growth every year. The first growth cycle occurs
 during the monsoon, when it doubles in height. The second growth cycle occurs during the summer
 , when its height increases by 1 meter.Now, a new Utopian tree sapling is planted at the onset
 of the monsoon. Its height is 1 meter. Can you find the height of the tree after N growth 
cycles?Input'''

def growth(n):
    height=1
    for i in range(1,n+1):
        if i%2==1:
           height*=2
        else:
           height+=1
    print(height)

    
__name__
l=[]

testcases=int(input("Enter no. of testcases"))
for i in range(testcases):
    l.append(int(input("enter number")))
for i in range(len(l)):
    growth(l[i])
    
   

       