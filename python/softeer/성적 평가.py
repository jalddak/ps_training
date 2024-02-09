import sys
import heapq

input = sys.stdin.readline

N = int(input())
answer = []
final = [0 for _ in range(N)]

def calc_prize(scores):
    heap = [(-scores[i], i) for i in range(N)]
    heapq.heapify(heap)
    result = [0 for _ in range(N)]
    prize = 1
    before = -heap[0][0]
    cnt = 0
    while heap:
        score, index = heapq.heappop(heap)
        score = -score
        final[index] += score
        if before == score:
            result[index] = prize
            cnt += 1
        else:
            before = score
            prize += cnt
            cnt = 1
            result[index] = prize

    return result

for _ in range(3):
    scores = list(map(int, input().split()))
    answer.append(calc_prize(scores))
answer.append(calc_prize(final))

for a in answer:
    print(' '.join(map(str, a)))
    