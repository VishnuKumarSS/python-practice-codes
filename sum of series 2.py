# sum of series (i.e) 1+3+5+7...+n
a = int(input("Enter a number for sum of series :"))
b = 1
sum = 0
while(b<=a):
    if b % 2 != 0:    
        sum += b
    b += 1
print("The sum of odd values in this series :",sum)