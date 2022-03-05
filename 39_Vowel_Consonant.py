# 1. Using if-else
c=input("Enter an alphabet: ")
if c=='a' or c=='e' or c=='i' or c=='o' or c=='u' or c=='A' or c=='E' or c=='I' or c=='O' or c=='U':
    print(f" {c} is a vowel")
else:
    print(f"{c} is a consonant")

# 2.Using list and if-else:
ch=input("Enter a character: ")
l=['a','e','i','o','u','A','E','I','O','U']
if ch in l:
    print(f"{ch} is a vowel")
else:
    print(f"{ch} is a consonant")


# 3. using function: 
c=input("Enter: ")
def isUpper(c):
    return c=='A' or c=='E' or c=='I' or c=='O' or c=='U'
def isLower(c):
    return c=='a' or c=='e' or c=='i' or c=='o' or c=='u'
        

if not c.isalpha():
    print("Invalid Input")
elif isUpper(c) or isLower(c):
    print(f"{c} is a vowel")
else:
    print(f"{c} is a consonant")

