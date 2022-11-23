a=int(input("Enter a binary value: "))
aa = a
i=0
b1=0
power=0
'''while(a!=0): # to get the length of given binary number
    a=a//10
    i=i+1'''
#print(i)
while i!=aa: # here start is 0 and i is 4
    a1=aa%10
    aa=aa//10
    #print(aa)
    b1=b1+(a1*2**power)
    #print("b1",b1)
    power=power+1
print("Decimal value:",b1)
    