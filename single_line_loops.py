l = list(range(10))
print(l)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print([i for i in l if i % 2 == 0])
# [0, 2, 4, 6, 8]

print([i for i in l if i % 2 != 0])
# [1, 3, 5, 7, 9]

print(l)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]