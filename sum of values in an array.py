def simpleArraySum(ar):
    c = 0
    for i in range(ar):
        c = c + array[i]
    return c


n = int(input("Enter how many values to be performed to sum : "))
array = list(map(int, input("Enter the values to be added : ").split()))[:n]
print(simpleArraySum(n))

