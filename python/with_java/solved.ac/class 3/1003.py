t = int(input())

temp = [(1, 0), (0, 1)]

for i in range(2, 41):
    a, b = temp[i-1][0] + temp[i-2][0], temp[i-1][1] + temp[i-2][1]
    temp.append((a, b))
for _ in range(t):
    n = int(input())
    print(temp[n][0], temp[n][1])