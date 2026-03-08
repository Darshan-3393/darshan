s = input("Enter sentence: ")
word=""
longest=""
for ch in s+" ":
    if ch!=" ":
        word+=ch
    else:
        if len(word)>len(longest):
            longest=word
        word=""
print("Longest word =",longest)