# How many number of ways can students be arranged in a given number of seats?
# Using Permutation


num_seats=int(input("Enter: "))
num_students=int(input("ENter: "))
def fact_num(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

ways=fact_num(num_students)-fact_num(num_students-num_seats)
print(ways)
