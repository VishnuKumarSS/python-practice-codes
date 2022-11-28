n = "apple is a best in the taste"
m = n.split()
c=0
for word in m:
    if str(word[(range(len(m)))]) == "a":
        break
    else:
        c+=1
print(c)
        #print(c)
#print(c)        

