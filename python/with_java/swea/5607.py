tcCnt = int(input())

mod = 1234567891

dp = [-1 for _ in range(1000001)]
dp[0] = 1
dp[1] = 1
for i in range(2, 1000001):
    dp[i] = dp[i-1] * i % mod

def pow(num, p):
    if p == 0:
        return 1
    if p == 1:
        return num
    temp = pow(num, p // 2)
    temp = temp * temp % mod
    if p % 2 == 1:
        temp = temp * num % mod
    return temp

answer = []
for tc in range(1, tcCnt + 1):
    n, r = map(int, input().split())

    c = dp[r] * dp[n-r] % mod
    result = dp[n] * pow(c, mod - 2) % mod

    sb = "#" + str(tc) + " " + str(result)
    answer.append(sb)
print("\n".join(answer))