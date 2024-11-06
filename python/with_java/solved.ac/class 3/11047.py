import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

coins.sort(reverse=True)
answer = 0

for c in coins:
    answer += k // c
    k = k % c

print(answer)