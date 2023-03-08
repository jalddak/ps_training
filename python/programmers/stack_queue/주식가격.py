def solution(prices):
    answer = []
    for i in range(len(prices)):
        sec = 0
        for j in range(i, len(prices)):
            if i != j:
                sec += 1
            if prices[i] > prices[j]:
                break
        answer.append(sec)
    return answer