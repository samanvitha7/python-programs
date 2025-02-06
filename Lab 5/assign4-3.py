#panagram

def is_panagram(text):
    text=text.lower()
    unique=set(c for c in text if c.isalpha())

    if(len(unique)==26):
        return "panagram"
    else:
        return "not a panagram"

text=input("enter the sentence")
print(is_panagram(text))