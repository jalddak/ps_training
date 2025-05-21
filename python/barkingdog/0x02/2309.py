ls = []

for _ in range(9):
    ls.append(int(input()))

ls.sort()
sums = sum(ls)

result = []
for i in range(9):
    temp = sums
    for j in range(i + 1, 9):
        temp = sums - ls[i] - ls[j]
        if temp == 100:
            result = [i, j]
            break
    if temp == 100:
        break

answer = []
for i in range(9):
    if i in result:
        continue
    answer.append(ls[i])

answer.sort()
for a in answer:
    print(a)