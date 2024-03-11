for n in range(100, 1001):
    if n%2 != 0 and (n/2*3)%10 == 0:
        print(n, n%2, n/2*3)
    if n%3 != 0 and (n/3*4)%10 == 0:
        print(n, n%3, n/3*4)