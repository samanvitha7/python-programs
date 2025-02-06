def check_pall(word):
    j = len(word) - 1
    word = list(word)
    operations = 0  # 
    for i in range(len(word) // 2):
        dif = ord(word[i]) - ord(word[j])
        if dif < 0:
            word[j] = chr(ord(word[j]) + dif)
            operations += 1  
        if dif > 0:
            word[i] = chr(ord(word[i]) - dif)
            operations += 1  
        
        j -= 1
    return operations

text = []
testcases = int(input())  #Enter no. of testcases
for i in range(testcases):
    input_string = input()#enter the word
    text.append(input_string)

for i in range(testcases):
     operations = check_pall(text[i])
     print(operations)
