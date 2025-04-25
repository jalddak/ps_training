import sys
input = sys.stdin.readline

m = int(input())
k = 1000000007

def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a%b)

def divide(b, p):
    if p == 1:
        return b
    result = divide(b, p // 2)
    result = result * result % k
    if p % 2 != 0:
        return b * result % k
    return result

    
answer = 0
for _ in range(m):
    n, s = map(int, input().split())
    temp = gcd(n, s)
    n //= temp
    s //= temp
    answer += s * divide(n, k-2) % k
    answer %= k

print(answer)
