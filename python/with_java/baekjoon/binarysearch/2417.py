n = int(input())

def binarySearch(s, e):
    while s + 1 < e:
        mid = (s+e) // 2
        if mid ** 2 < n:
            s = mid
        else:
            e = mid
    return e

print(binarySearch(-1, n))