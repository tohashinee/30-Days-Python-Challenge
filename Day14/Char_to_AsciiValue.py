# Write a function that converts a string into its ASCII code point array and back ("ABC" → [65, 66, 67])
def converter(text):
    charlist = []
    for i in range(len(text)):
        charlist.append(str(ord(text[i])))
    next
    print("These are the ascii code points: "+",".join(charlist))

    s = ""
    for i in charlist:
        s = s+(chr(int(i)))
    next
    print("This is: "+s)


line = input("Enter String: ")
converter(line)