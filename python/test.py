def gcd(a, b):
    r = 0
    while(b != 0):
        r = a % b
        a = b
        b = r
        print(a, b)
    return a

print(gcd(20, 24))