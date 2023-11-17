N = int(input())
dp = [[1, 1, 1]]

for _ in range(1, N):
    e, l, r = dp.pop()
    ne = e + l + r
    nl = e + r
    nr = e + l
    dp.append([ne, nl, nr])

print(sum(dp[0])%9901)

# n = next, b = before
# next = ne + nl + nr == 2 (e + l + r) + e = 2 (e + l + r) + (be + bl + br) = 2(now) + before