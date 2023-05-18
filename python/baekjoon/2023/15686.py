from itertools import combinations

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

chickens = []
houses = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            houses.append([i, j])
        elif city[i][j] == 2:
            chickens.append([i, j])

candidates = list(combinations(chickens, m))

mins = (n*2)*n*n
for candidate in candidates:
    som = 0
    for h in houses:
        least = n * 2
        for c in candidate:
            distance = abs(h[0]-c[0]) + abs(h[1]-c[1])
            if distance < least:
                least = distance
        som += least
    mins = min(mins, som)

print(mins)