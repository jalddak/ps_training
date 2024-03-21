def solution(k, ranges):
    answer = []
    loca = [(0, k)]
    x = 1
    while k != 1:
        if k % 2 == 0:
            k = k // 2
        else:
            k = k * 3 + 1
        loca.append((x, k))
        x += 1
    sum_dp = [0]
    n = len(loca)
    for i in range(n-1):
        x1, y1 = loca[i]
        x2, y2 = loca[i+1]
        area = max(y1, y2) - abs(y1-y2) / 2
        sum_dp.append(sum_dp[-1]+area)
    
    for r in ranges:
        left, right = r
        candidate = -1.0
        if n-1+right >= 0 and left < n and n-1+right >= left:
            candidate = sum_dp[n-1+right]-sum_dp[left]
        answer.append(candidate)
    return answer