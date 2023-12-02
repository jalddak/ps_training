# 지수 법칙
# A^m+n = A^m x A^n

# 나머지 분배 법칙
# (AxB)%C = (A%C) * (B%C) % C

a, b, c = map(int, input().split())

def solution(a,b,c):
    if b == 1:
        return a % c
    elif b == 2:
        return (a*a) % c
    else:
        if b % 2 == 0:
            return (solution(a, b//2, c) ** 2) % c
        else:
            return (solution(a, b//2, c) ** 2) * a % c
        
print(solution(a, b, c))