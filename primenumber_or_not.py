n = int(input("Enter a number: "))
if n >= 1:
    for i in range(2, n):
        if (n % i) == 0:
            print("The number is not prime")
            break
    else:
        print(f"{n} is a prime number")
else:
    print("Enter a valid number")
