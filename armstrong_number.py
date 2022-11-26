a = int(input("Enter a number to find armstrong: "))
b = str(a)
c = len(b)
added = 0
for j in b:
    arms = int(j)**c
    added += arms
    print("Just to know what is happening: ",arms) # This line is just to know what is happening
if added == a:
    print(a,"is a armstrong number")
elif added != a:
    print(a,"is not armstrong number")

