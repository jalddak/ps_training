import sys

N, M, K = map(int, input().split())
rails = list(map(int, input().split()))

from itertools import permutations

rails_orders = list(permutations(rails, N))

answer = 2500
for ro in rails_orders:
    cnt = 0
    index = 0
    now = 0
    result = 0
    while cnt < K:
        now += ro[index]
        next = index + 1 if index + 1 < N else 0
        if now + ro[next] > M:
            cnt += 1
            result += now
            now = 0
        index = next
    answer = min(answer, result)

print(answer)