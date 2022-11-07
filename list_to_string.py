# to convert the string elements of list to string

array_str=["a","b","c","d","e"]
print("array_str : ",array_str)

string1=" ".join(array_str)
print("string 1: ",string1)


print()


# to convert the integer elements of list to string
array_int=[1,2,3,4,5]
print("array_int : ",array_int)

string2=""
for i in array_int:
    string2+=str(i)+" "
print("string 2: ",string2)
