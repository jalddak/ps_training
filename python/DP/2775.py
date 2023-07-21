T = int(input())

apart = [[i for i in range(15)]]
for i in range(1, 15):
    layer = [0]
    for j in range(1, 15):
        n = apart[i-1][j] + layer[j-1]
        layer.append(n)
    apart.append(layer)

for _ in range(T):
    k = int(input())
    n = int(input())
    print(apart[k][n])

