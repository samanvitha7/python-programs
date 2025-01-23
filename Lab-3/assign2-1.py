'''Write a program that asks the user to enter a word and then capitalizes every other letter
 of that word. So, if the user enters rhinoceros, the program should print rHiNoCeRoS.'''

word = input("Enter the word: ")
# to store the modified word
final = ""
for i in range(len(word)):
    if i % 2 == 0:  # No change for even index
        final+= word[i].lower()
    else:           # capitalise the letter if the index is odd
        final+= word[i].upper()
print("The entered word after changes is as follows:")
print(final)
