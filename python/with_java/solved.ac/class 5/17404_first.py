n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]
inf = 1000 * 1000 + 1
dp = [[[inf, costs[0][1] + costs[1][0], costs[0][2] + costs[1][0]], 
      [costs[0][0] + costs[1][1], inf, costs[0][2] + costs[1][1]], 
      [costs[0][0] + costs[1][2], costs[0][1] + costs[1][2], inf]]]

for i in range(2, n):
    before = dp.pop()
    print(before)

    next = []
    for j in range(3):
        temp = []
        for k in range(3):
            minCheck = []
            for a in range(3):
                if j == a:
                    continue
                minCheck.append(before[a][k])
            temp.append(min(minCheck) + costs[i][j])
        next.append(temp)
    dp.append(next)

result = []
for i in range(3):
    for j in range(3):
        if i == j:
            continue
        result.append(dp[-1][i][j])

answer = min(result)
print(answer)