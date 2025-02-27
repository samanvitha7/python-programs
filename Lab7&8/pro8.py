"""Decode the message:
A message containing the letters from A-Z can be encoded into the numbers using the mapping A-> 1, B-> 2, C-> 3, ..., Z-> 26. To decode an encoded message, you need to group the digits and do the reverse mapping. You are required to display all the possible decoded messages. For example: "11106" can be decoded into:
a. "AAJF" with the grouping (1 1 10 6)
b. "KJF" with the grouping (11 10 6)"""


def decode_ways(s, index=0, path="", results=None):
    if results is None:
        results = []
    
    if index == len(s):  # Base case: reached the end of the string
        results.append(path)
        return
    
    # to take a single digit (1-9)
    if s[index] != '0':  # Skip invalid numbers
        decode_ways(s, index + 1, path + chr(int(s[index]) + 64), results)
    
    # to take two digits (10-26)
    if index + 1 < len(s) and 10 <= int(s[index:index+2]) <= 26:
        decode_ways(s, index + 2, path + chr(int(s[index:index+2]) + 64), results)

    return results


s = "11106"
decoded_messages = decode_ways(s)
print(decoded_messages)  
