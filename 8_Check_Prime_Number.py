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
    
  
# OR
def prime(num):
        factors=[i for i in range(2,num) if num%i==0]
        if len(factors)==0:
            return True
        else:
            return False
    
print(prime(10))
print(prime(9))
print(prime(5))
print(prime(3))


