a = 1
vowels = 0
consonants = 0

while (a<=10):
    x = input(f"Enter character {a} : ").lower()
    a+=1
    
    if x == "a" or x=="e" or x=="i" or x=="o" or x=="u":
        vowels += 1
    elif x == "":
        break
    elif x == " ":
        break
    else:
        consonants += 1
        

print(f"There is {vowels} vowels")
print(f"There is {consonants} consonants")