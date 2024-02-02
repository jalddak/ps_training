import sys

k, p, n = map(int, input().split())

result = k
for _ in range(n):
    result *= p
    result %= 1000000007

print(result)