a=int(input("Enter a number to check its prime or not: "))
prime=False
for i in range(2,a):
    if a%i==0:
        prime=True
        break

if(prime==True):
    print(f"{a} is Not a Prime Number")        
else:
    print(f"{a} is a Prime Number")

