s=input("Enter string: ")
rev=""
for ch in s:
    rev=ch+rev
if s==rev:
    print(s,"is a Palindrome")
else:
    print(s,"is not a Palindrome")