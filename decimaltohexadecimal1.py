decimal = 256
a1 = decimal%16 #remainder
d1 = decimal//16 #divide
a2 = d1%16
d2 = d1//16
a3 = d2%16
d3 = d2//16
hexa = (f"{a3}{a2}{a1}")
print("Hexadecimal value :",hexa)
