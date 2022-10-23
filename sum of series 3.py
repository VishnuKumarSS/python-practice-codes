# sum of series (i.e) 5^3 + 10^3 + 15^3 + ... + n^3
a = int(input("Enter a number for sum of series :"))
b = 1
sum = 0
sample = 0
while(b<=a):
    if b % 5 == 0: 
        sample = b**3  
        sum += sample
    b += 1
print("The sum of power of values which are divisible by 5 :",sum)