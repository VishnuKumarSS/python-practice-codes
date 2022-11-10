n=int(input("Enter how many numbers should be in list: "))
a = tuple(map(int,input("Enter the list elements followed by space: ").split()))[:n]
print("The list is: ",a)