#rindex
s='abcdabhji'
sub='ab'
for i in range(len(s)-len(sub)+1):
    if s[i:i+len(sub)]==sub :
        rindex=i
print(rindex)
    