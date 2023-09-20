N = int(input())

dp = [0]
for i in range(1, N+1):
    if i % (i ** (1/2)) == 0:
        dp.append(1)
        continue
    else:
        min_cnt = -1
        for j in range(1, i//2+1):
            cnt = dp[j] + dp[i-j]
            if min_cnt == -1 or min_cnt > cnt:
                min_cnt = cnt
        dp.append(min_cnt)

print(dp[-1])

# 다른 사람 풀이를 보니, 전체를 구할 이유가 없다.

N = int(input())

dp = [0]
for i in range(1, N+1):
    if i % (i ** (1/2)) == 0:
        dp.append(1)
        continue
    else:
        min_cnt = -1
        for j in range(1, int(i ** (1/2))):
            cnt = 1 + dp[i - j*j]
            if min_cnt == -1 or min_cnt > cnt:
                min_cnt = cnt
        dp.append(min_cnt)

print(dp[-1])