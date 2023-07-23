N = int(input())

dp = {}
for i in range(N):
    rgb = list(map(int, input().split()))
    if i == 0:
        for j in range(3):
            dp[j] = rgb[j]
    else:
        new = {}
        for key in dp:
            index_list = [0, 1, 2]
            index_list.pop(key)
            if index_list[0] in new:
                new[index_list[0]] = min(new[index_list[0]], dp[key] + rgb[index_list[0]])
            else:
                new[index_list[0]] = dp[key] + rgb[index_list[0]]
            if index_list[1] in new:
                new[index_list[1]] = min(new[index_list[1]], dp[key] + rgb[index_list[1]])
            else:
                new[index_list[1]] = dp[key] + rgb[index_list[1]]
        dp = new

print(min(list(dp.values())))


# dp로 배열 형식으로 푼 다른사람 코드의 핵심 내용
# 위에서 밑으로 내려가면서 자신을 제외한 j중에서 더 작은 값으로 더하기

# for i in range(1, n):
#     dp[i][0] = min(dp[i-1][1] + dp[i][0], dp[i-1][2] + dp[i][0])
#     dp[i][1] = min(dp[i-1][0] + dp[i][1], dp[i-1][2] + dp[i][1])
#     dp[i][2] = min(dp[i-1][0] + dp[i][2], dp[i-1][1] + dp[i][2])
