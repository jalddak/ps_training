N = 1
number = 1121

def solution(N, number):
    answer = 0
    dp = [N]
    N_num = [[0]]
    answer += 1
    index_start = 0
    if N != number:
        answer = search(N, number, dp, N_num, answer, index_start)
    print(answer)
    return answer

def search(N, number, dp, N_num, answer, index_start):
    answer += 1
    if answer > 8:
        answer = -1
        return answer
    pairs = []
    for i in range(1, answer):
        pairs.append([i,answer-i])
    index = index_start
    index_list = []
    pairs.sort(key = lambda x : x[1])
    for pair in pairs:
        for i in N_num[pair[0]-1]:
            for j in N_num[pair[1]-1]:
                if pair[1] == 1 and i == N_num[pair[0]-1][0]:
                    if dp[i]*10 + dp[j] == number:
                        return answer
                    dp.append(dp[i]*10 + dp[j])
                    index += 1
                    index_list.append(index)
                if dp[i]+dp[j] == number:
                    return answer
                dp.append(dp[i]+dp[j])
                index += 1
                index_list.append(index)
                if dp[i]-dp[j] == number:
                    return answer
                dp.append(dp[i]-dp[j])
                index += 1
                index_list.append(index)
                if dp[i]*dp[j] == number:
                    return answer
                dp.append(dp[i]*dp[j])
                index += 1
                index_list.append(index)
                if dp[j] != 0:
                    if dp[i]/dp[j] == number:
                        return answer
                    dp.append(dp[i]/dp[j])
                    index += 1
                    index_list.append(index)
    index_start = index
    N_num.append(index_list)
    answer = search(N, number, dp, N_num, answer, index_start)
    return answer

solution(N, number)