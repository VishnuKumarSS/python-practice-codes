a = int(input("Enter zeros and ones to get the appropriate decimal number: ")) 
a1 = a%10 #line 2 to line 8 is to get the terms or every number of integer specificly
a = a//10
a2 = a%10
a = a//10
a3 = a%10
a = a//10
a4 = a%10

b1 = a1*2**0
b2 = a2*2**1
b3 = a3*2**2
b4 = a4*2**3
binary = b1+b2+b3+b4
print(binary)