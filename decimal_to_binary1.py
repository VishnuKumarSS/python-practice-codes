decimal = 8
a1 = decimal%2 #remainder
d1 = decimal//2 #divide
a2 = d1%2
d2 = d1//2
a3 = d2%2
d3 = d2//2
a4 = d3%2
d4 = d3//2
binary = (f"{a4}{a3}{a2}{a1}")
print(binary)
