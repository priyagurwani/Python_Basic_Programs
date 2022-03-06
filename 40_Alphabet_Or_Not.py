print(ord("A"))   #For Understanding

#1. Using ASCII values: 
ch=input("Enter a character: ")
if 65<=ord(ch)<=90 or 96<=ord(ch)<122:
    print(f"{ch} is a character")
else:
    print(f"{ch} is not a character")


# 2.Using alphabets:
ch=input("Enter a character: ")
if 'a'<=ch<='z' or 'A'<=ch<='Z':
    print(f"{ch} is a character")
else:
    print(f"{ch} is not a character")
