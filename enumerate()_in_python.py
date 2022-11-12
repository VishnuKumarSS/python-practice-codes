a="starz"
b=enumerate(a,1)
print(list(b))

c="kumar"
print(list(enumerate(c,1)))

d=['a','b','c','d']
e=enumerate(d,1) # if we dont give any number in the place of 1, it will consider it as 0 by default.
# for example
f=enumerate(d) # by default it will be considered as zero
print(list(e))
print(list(f)) 