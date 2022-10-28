N=6
array = "11 6 3 10 4 12".split()[:N]
M=8
diff=[]
for i in array:
    diff.append(abs(M-int(i)))
diff.sort()
keydict = dict(zip(array, diff))
array.sort(key=keydict.get)
print(array)
disp=" ".join(array)
print(disp)