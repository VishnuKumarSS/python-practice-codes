# infyTQ question.

arr = list(map(int,input().split(",")))
took = []
rep_arr = []
for i in arr:
    i = abs(i)
    i = str(i)
    if len(i) > 1:
        if i not in took:
            repeated = 0
            for j in range(len(arr)):
                string1 = i
                string2 = str(arr[j])
                if string1[0] == string2[0]:
                    repeated+=1
            took.append(i[0])
            rep_arr.append(repeated)
if len(rep_arr)>0:
    maxi = max(rep_arr)
    index_arr = []
    for i in range(len(rep_arr)):
        if maxi == rep_arr[i]:
            index_arr.append(arr[i])
else:
    maxi = 0
if maxi == 0:
    print(-1)
else:
    print(maxi)