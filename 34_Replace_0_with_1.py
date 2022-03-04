#1.  Using String methods
num=int(input("Enter num: "))
s=str(num)
n=''
n+=s.replace('0','1')
print(int(n))


#2.  using List
n=int(input("Enter num: "))
s=str(n)
l=[]
for i in s:
    if i=='0':
        l.append('1')
    else:
        l.append(i)
# print(l)
res=''
for i in l:
    res+=i
print(res)
