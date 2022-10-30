# WHERE WE TYPE OR USE VARIABLES ALSO MATTERS

string="hellow world"
s1=''
s2=''
for i in string:
    s1 = i + s1 # THIS REVERSES THE STRING
    s2 = s2 + i # BUT THIS DOESN'T
print('example 1: ',s1)
print('example 2: ',s2)