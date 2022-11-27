# append() function is used to append the elements insides a list
# extend() function is used to extend the list, but the parameters inside the extend function should also be a list or string. ( or ) any iterables.

# extend() :
# it iterates through the list of elements and adds the elements to the list.
# we can't iterate through a integer so it will show error.


a=[1,2,3]
b=4
c="star"
list1=[]
list2=[]
list1.append(a)
list1.append(b)
list1.append(c)
print(list1)

list2.extend(a)
list2.extend(b) # this will show error
list2.extend(c)
print(list2)