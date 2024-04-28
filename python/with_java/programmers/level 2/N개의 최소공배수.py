def calc(current, n):
    min_n = min(current, n)
    gcd = 1
    for num in range(1, min_n+1):
        if current % num == 0 and n % num == 0:
            gcd = num
    lcm = gcd * current//gcd * n//gcd
    return lcm

def solution(arr):
    min_n = min(arr)
    if len(arr) == 1:
        return arr[0]
    lcm = calc(arr[0], arr[1])
    for i in range(2, len(arr)):
        lcm = calc(lcm, arr[i])
        
    return lcm