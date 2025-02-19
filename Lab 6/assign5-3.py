#lexicographically greater

def lexico(word):
    word=list(word)
    n=len(word)
    i=n-2
    while i>=0 and word[i]>=word[i+1]:
        i-=1
    if i==-1:
        return "no answer"
    j=n-1 
    while word[j]<=word[i]:
        j-=1
    word[i],word[j]=word[j],word[i]
    word=word[:i+1]+ sorted(word[i+1:])
    return"".join(word)
l=[]
test=int(input())
for i in range(test):
    word=input()
    l.append(word)
for j in range(test):
    print(lexico(l[j]))