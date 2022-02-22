# n=6 , m=28
# Divisor of 6 are 1, 2, 3, 6.
# Divisor of 28 are 1, 2, 4, 7, 14, 28. Sum of divisor of 6 and 28 are 12 and 56 respectively. Abundancy index of 6 and 28 are 2. So they are friendly pair.
# n=18 , m=7
# They are not friendly pair.

#Program:
a,b=(input("Enter num: ").split(","))
a=int(a)
b=int(b)
factors_a=[i for i in range(1,a+1) if a%i==0]
factors_b=[i for i in range(1,b+1) if b%i==0]
def sum_factors(num):
    sum=0
    for i in num:
        sum+=i
    return sum
x=sum_factors(factors_a)
y=sum_factors(factors_b)

c=[i for i in factors_a if i in factors_b and i!=1]
# print(c)
check_pair=["Friendly pair" if c!=[] else "Not Friendly pair"]
print(check_pair)
