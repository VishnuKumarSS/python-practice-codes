a_list=[1,2,3,4,5,6]
print(a_list)

print(*a_list) # This prints without the brackets and commas
  
print(*a_list, sep = ", ") # this seperates every element by comma

print(*a_list, end = ", ") # this prints comma at the end of the list
print()


b = [8,7,6,5,4]
print(' '.join(map(str, b)))
print(b[:2])
print(b[0:2])
print(b[1:2])
print(b[0:3])
print(b[1:3])
