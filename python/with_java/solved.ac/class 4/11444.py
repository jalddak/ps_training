# 도가뉴 항등식이 뭐여

n = int(input())

checked = {}
def fibo(n):
    if n not in checked:
        if n == 0:
            checked[n] = 0
        elif n == 1:
            checked[n] = 1
        elif n % 2 == 0:
            fn = fibo(n//2)
            fnMinus1 = fibo(n//2-1)
            checked[n] = (fn * (fn + 2 * fnMinus1)) % 1000000007
        else:
            fn = fibo(n//2)
            fnPlus1 = fibo(n//2+1)
            checked[n] = (fn ** 2 + fnPlus1 ** 2) % 1000000007
    return checked[n]

print(fibo(n))