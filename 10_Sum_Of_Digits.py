# Here ENter more than one digit number
# Eg: you Entered = 69 -->Output:15
# Eg: you Entered = 1269 -->Output:18
# 1. Using For Loop
a=input("Enter a three digit number: ")
sum=0
for i in a:
    sum+=int(i)
print(sum)


# 2. Using Reverse Method
num=1234
sum=0
while(num!=0):
    digit=num%10   #-->4-->3-->2-->1
    sum=sum+digit  #--->0+4=4-->4+3=7-->7+2=9-->9+1=10
    num=num//10
print(sum)

