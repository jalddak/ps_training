n = int(input())
dp = [list(map(int, input().split()))]

for _ in range(n-1):
    r, g, b = map(int, input().split())
    dp.append([r + min(dp[-1][1], dp[-1][2]), g + min(dp[-1][0], dp[-1][2]), b + min(dp[-1][0], dp[-1][1])])

print(min(dp[-1]))