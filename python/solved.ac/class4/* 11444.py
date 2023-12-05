# 도가뉴 항등식을 이용한 피보나치

n = int(input())

d = {}
def fibo(n):
    if n in d:
        return d[n]
    if n == 0:
        d[n] = 0
    elif n == 1:
        d[n] = 1
    elif n % 2 == 0:
        f = fibo(n//2)
        s = fibo(n//2-1)
        d[n] = (f * (f + 2*s)) % 1000000007
    else:
        f = fibo(n//2+1)
        s = fibo(n//2)
        d[n] = ((f**2) + (s**2)) %1000000007
    return d[n]

print(fibo(n)%1000000007)