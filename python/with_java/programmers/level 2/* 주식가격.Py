def solution(prices):
    answer = [0 for _ in range(len(prices))]
    stack = []
    for i in range(len(prices)):
        while stack and stack[-1][1] > prices[i]:
            info = stack.pop()
            answer[info[0]] = i - info[0]
        stack.append((i, prices[i]))
    while stack:
        info = stack.pop()
        answer[info[0]] = len(prices)-1-info[0]
    return answer

# O(N^2) 시간복잡도라 Prices의 길이가 10만이되면 타임아웃날듯.
def solution(prices):
    N = len(prices)
    answer = []
    for i in range(N):
        time = 0
        for j in range(i+1, N):
            time += 1
            if prices[i] > prices[j]:
                break
        answer.append(time)
    return answer