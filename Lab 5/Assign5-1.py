#Maximizing XOR
l_num=int(input())  #entering lower bound number
u_num=int(input())  #entering upper bound
max=0
for i in range(l_num,u_num+1):
    for j in range(i,u_num+1):
        xor=i^j
        if(xor>max):
            max=xor
        else:
            continue
print(max)


