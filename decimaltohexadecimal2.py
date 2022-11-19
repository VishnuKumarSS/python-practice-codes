decimal = int(input("Enter decimal value: "))
hexa=""
while decimal>0:
    remainder = decimal%16
    decimal = decimal//16
    if remainder==10:
        r= "A"
    elif remainder==11:
        r = "B"
    elif remainder==12:
        r = "C"
    elif remainder==13:
        r = "D"
    elif remainder==14:
        r = "E"
    elif remainder==15:
        r = "F"
    else:
        r = str(remainder)
        
    hexa = hexa + r
    #print(hexa)
    
    
print("Hexadecimal value :",hexa[::-1])