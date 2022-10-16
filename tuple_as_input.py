n=int(input("Enter how many numbers should be in tuple: "))
a = tuple(map(int,input("Enter the tuple elements followed by space: ").split()))[:n]
print("The tuple is: ",a)