# 최대공약수 최소공배수 : math.gcd, math.lcm

import sys
input = sys.stdin.readline
import math

M = int(input())
mod_n = 1000000007

ns = [list(map(int, input().split())) for _ in range(M)]

def solution(num, power):
    if power == 1:
        return num
    if power % 2 == 0:
        ban = solution(num, power // 2)
        return ban * ban % mod_n
    return num * solution(num, power - 1) % mod_n


result = 0
for n, s in ns:
    gcd = math.gcd(n, s)
    n //= gcd
    s //= gcd
    result = s * solution(n, mod_n-2) % mod_n
    result %= mod_n

print(result)