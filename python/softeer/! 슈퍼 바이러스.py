import sys

k, p, n = map(int, input().split())
n *= 10

def sub(p, n):
    if n == 1:
        return p
    
    subResult = sub(p, n//2)
    if n%2 == 0:
        return subResult * subResult % 1000000007
    else:
        return subResult * subResult * p % 1000000007

print(k * sub(p, n) % 1000000007)