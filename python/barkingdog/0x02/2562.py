maxN = 0
index = -1
for i in range(9):
    n = int(input())
    if n > maxN:
        maxN = n
        index = i + 1

print(maxN)
print(index)