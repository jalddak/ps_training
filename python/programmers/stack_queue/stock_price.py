from collections import deque

# deque 안쓰고 리스트로 prices 써서 pop(0) 하면 효율성 안됨.

def solution(prices):
    answer = []
    prices = deque(prices)
    while len(prices) != 0:
        price = prices.popleft()
        time = 0
        for after in prices:
            time += 1
            if price > after:
                break
        answer.append(time)
    return answer

# def solution(prices):
#     answer = []
#     for i in range(len(prices)):
#         time = 0
#         for j in range(i+1, len(prices)):
#             time += 1
#             if prices[i] > prices[j]:
#                 break
#         answer.append(time)
#     return answer