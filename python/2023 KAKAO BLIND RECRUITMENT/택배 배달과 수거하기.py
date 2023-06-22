# 며칠 지나고 다시 봤는데 대충 기억나서 풀어진다

def solution(cap, n, deliveries, pickups):
    d_cap = 0
    p_cap = 0
    answer = 0
    for i in range(n-1, -1, -1):
        d_cap -= deliveries[i]
        while d_cap < 0:
            d_cap += cap
            p_cap += cap
            answer += 2 * (i+1)
        p_cap -= pickups[i]
        while p_cap < 0:
            d_cap += cap
            p_cap += cap
            answer += 2 * (i+1)
                
    return answer