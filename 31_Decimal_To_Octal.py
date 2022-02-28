# Decimal_Num=394
# 394//8= 49 and 394%8=2
# 49//8=6  and 49%8 = 1
# 6//8=6 and 6%8=6
# Modulo Ones In reverese manner = 612
# Octal Number = 612
dec_num=int(input("Enter : "))
oct_num=[]
while(dec_num!=0):
    rem=dec_num%8
    dec_num=dec_num//8
    oct_num.append(rem)
num=oct_num[::-1]
for i in num:
    print(i,end='')
