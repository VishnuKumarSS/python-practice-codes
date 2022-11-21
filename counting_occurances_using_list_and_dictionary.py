
MyList = ["b", "a", "a", "c", "b", "a", "c",'a','c','f','k']
lis=[]

print("Finding occurances Using list:   ")
for i in MyList:
    if i not in lis:
        count=0
        for j in MyList:
            if i == j:
                count+=1
        lis.append(i)
        print(i,count)    # print(i,count,end=" ")  # to print in single line


print()


print("Finding occurances Using dictionary:   ")
MyList = ["b", "a", "a", "c", "b", "a", "c",'a']
duplicate_dict={} # a dictionary to store each of them.
for i in MyList:#loop through them.
    duplicate_dict[i]=MyList.count(i)
print(duplicate_dict)
