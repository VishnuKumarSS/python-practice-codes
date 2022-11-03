n = int(input("Enter a number to find prime numbers: "))
for num in range(1, n+1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)

#using function
'''def prime_finder(n):
    for num in range(1, n+1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)
            
            
n = int(input("Enter a number to find prime numbers: "))
print(prime_finder(n))'''

