from collections import deque
absBigNum = 101000

def solution(arr):
    n = len(arr) // 2 + 1
    deque_arr = deque(arr)
    num_list = []
    sym_list = []
    while len(deque_arr) > 1:
        num_list.append(int(deque_arr.popleft()))
        sym_list.append(deque_arr.popleft())
    num_list.append(int(deque_arr.popleft()))
    max_dp = [[-absBigNum for _ in range(n)] for _ in range(n)]
    min_dp = [[ absBigNum for _ in range(n)] for _ in range(n)]
        
    for i in range(n):
        for j in range(n-i):
            symbols = []
            if i == 0:
                max_dp[j][j] = num_list[j]
                min_dp[j][j] = num_list[j]
                continue
                
            for k in range(i):
                symbols.append(sym_list[j + k])
                
            for l in range(len(symbols)):
                r = len(symbols)-1 - l
                if symbols[l] == '+':
                    max_dp[j][j+i] = max(max_dp[j][j+i], max_dp[j][j+l] + max_dp[j+l+1][j+i])
                    min_dp[j][j+i] = min(min_dp[j][j+i], min_dp[j][j+l] + min_dp[j+l+1][j+i])
                else:
                    max_dp[j][j+i] = max(max_dp[j][j+i], max_dp[j][j+l] - min_dp[j+l+1][j+i])
                    min_dp[j][j+i] = min(min_dp[j][j+i], min_dp[j][j+l] - max_dp[j+l+1][j+i])
                    
    answer = max_dp[0][len(num_list)-1]
    return answer