maxNum = 0
index = -1
for i in range(9):
    n = int(input())
    if maxNum < n:
        maxNum = n
        index = i+1

print(maxNum)
print(index)