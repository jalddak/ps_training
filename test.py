N = 8
number = 53

def solution(N, number):
    answer = 0
    dp = [[[N, 0],'n']]
    answer += 1
    dp_len = len(dp)
    index_start = 0
    if N != number:
        answer = search(N, number, dp, answer, dp_len, index_start)
    print(answer)
    return answer

def search(N, number, dp, answer, dp_len, index_start):
    answer += 1
    if answer > 8:
        answer = -1
        return answer
    index = index_start
    while index < dp_len:
        before_num = dp[index][0][0]
        express = dp[index][1]
        if index == index_start:
            if (before_num*10) + N == number:
                return answer
            dp.append([[(before_num*10) + N, 0], 'n'])

        if before_num + N == number:
            return answer
        dp.append([[before_num + N, 0], '+'])
        if express == '*':
            if (before_num/N) * (N + N) == number:
                return answer
            dp.append([[(before_num/N) * (N + N), 0], '+'])
        if express == '/':
            if ((before_num*N) + dp[index][0][1]) / (N + N) == number:
                return answer
            dp.append([[((before_num*N) + dp[index][0][1]) / (N + N), 0], '+'])

        if before_num - N == number:
            return answer
        dp.append([[before_num - N, 0], '-'])
        if express == '*':
            if (before_num/N) * (N - N) == number:
                return answer
            dp.append([[(before_num/N) * (N - N), 0], '-'])

        if before_num * N == number:
            return answer
        dp.append([[before_num * N, 0], '*'])
        if express == '+':
            if (before_num-N) + (N * N) == number:
                return answer
            dp.append([[(before_num-N) + (N * N), 0], '*'])
        if express == '-':
            if (before_num+N) - (N * N) == number:
                return answer
            dp.append([[(before_num+N) - (N * N), 0], '*'])

        if before_num / N == number:
            return answer
        dp.append([[before_num / N, before_num % N], '/'])
        if express == '+':
            if (before_num-N) + (N / N) == number:
                return answer
            dp.append([[(before_num-N) + (N / N), 0], '*'])
        if express == '-':
            if (before_num+N) - (N / N) == number:
                return answer
            dp.append([[(before_num+N) - (N / N), 0], '*'])

        index += 1
    
    index_start = index
    dp_len = len(dp)
    answer = search(N, number, dp, answer, dp_len, index_start)

    return answer

solution(N, number)