a = 1
even = 0
odd = 0
zero = 0

while (a<=10):
    x = int(input(f"Enter number {a} : "))
    a+=1
    
    if x == 0:
        print("The number is zero")
        zero += 1
    elif x%2 == 0:
        print("The number is even")
        even += 1
    elif x%2 != 0:
        print("The number is odd")
        odd += 1
    else:
        print("Enter the correct number")
        
print("even :",even)
print("odd :",odd)
print("zero :",zero)