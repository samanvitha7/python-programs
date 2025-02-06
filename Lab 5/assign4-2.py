#sherlock and squares

T = int(input())  #enter number of test cases
for _ in range(T):
    A, B = map(int, input().split())  
    cnt = 0  
    
    for i in range(A, B + 1):  
        temp = i ** 0.5  
        if int(temp) ** 2 == i:  
            cnt += 1  
    print(cnt)  


