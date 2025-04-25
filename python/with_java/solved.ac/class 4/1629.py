a, b, c = map(int, input().split())

def dv(a, b, c):
    if b == 1:
        return a % c
    elif b == 2:
        return (a % c) * (a % c) % c
    else:
        if b % 2 == 0:
            return dv(a, b//2, c) ** 2 % c
        else:
            return dv(a, b//2, c) ** 2 * (a % c) % c

print(dv(a, b, c))