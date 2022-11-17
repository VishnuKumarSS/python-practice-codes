decimal = int(input("Enter decimal value: "))
i=1
b = 0
power = 0
c=0
while i<=decimal:
    binary = decimal%2
    decimal = decimal//2
    #print(decimal)
    #b = binary
    #print(b)
    c =c+ binary*10**power
    power += 1
    
print(f"Binary value of the given decimal number is:",c)