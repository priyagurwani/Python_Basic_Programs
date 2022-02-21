# Automorhpic:  (Last digit of square should be same of number entered)
# 5 = square = 25 = True
# 25 = square = 625 = True
#6 = square = 36 = True
# 7 = square = 49 = False 
# 8 = square = 64 = False
# 1.Using if elif:

n=int(input("Enter n: "))
square=n*n
rev=str(square)
print(rev)
# print(rev[-1])
# print(rev[-2])
# print(str(n)[-1])
# print(str(n)[-2])

if len(str(n))==1:
    if(rev[-1]==str(n)[-1]):
        print("True")
    else:
        print("False")
elif len(str(n))==2:
     if(rev[-1]==str(n)[-1] and rev[-2]==str(n)[-2]):
         print("True")
     else:
        print("False")
else:
    print("False")


# Or
# 2. using conversion:

n=int(input("Enter num: "))
x=n*n
a=str(n)
b=str(x)
y=len(a)
z=len(b)
print(b)
if(z-b.find(a)==y):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")

# OR
# 3. using string methods:

num=int(input("Enter num: "))
square=str(num*num)
ans=["Automorhpic" if square.endswith(str(num)) else "Not an Automorhpic"]
print(ans)
