a, b = map(int, input().split())

def gcd(a, b):
    while(b != 0):
        r = a % b
        a = b
        b = r
    return a

def lcm(a, b):
    return a*b // gcd(a, b)

print(gcd(a,b), lcm(a,b))