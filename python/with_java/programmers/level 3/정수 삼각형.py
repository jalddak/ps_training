def solution(triangle):
    dp = []
    for row in triangle:
        if not dp:
            dp = row
            continue
        temp = []
        for i in range(len(row)):
            if i == 0:
                temp.append(dp[i] + row[i])
            elif i == len(row)-1:
                temp.append(dp[i-1] + row[i])
            else:
                temp.append(max(dp[i-1], dp[i]) + row[i])
        dp = temp
    return max(dp)