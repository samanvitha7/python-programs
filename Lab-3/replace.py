#replace
s='abcdef'
replace_by='def'
start=int(input("enter the starting index"))
end=int(input("enter the ending index"))
r=list(replace_by)  #converting to list
l=list(s)
for i in range(start, end + 1):
    if i - start < len(r):  # To Ensure replacement fits within bounds
        l[i] = r[i - start]

string_final = ''
for ch in l:
    string_final += ch

print(string_final)




