n = int(input())
k = int(input())

def bs(s, e):
    while s + 1 < e:
        mid = (s + e) // 2
        
        temp = 0
        for i in range(1, n+1):
            temp += min(mid // i, n)
        
        if temp < k:
            s = mid
        else:
            e = mid
    return e

print(bs(0, n * n))
