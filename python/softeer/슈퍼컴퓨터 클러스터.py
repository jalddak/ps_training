import sys

N, B = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

def bs():
    global N, B, nums
    min_s = 1
    max_s = 2000000000
    result = min_s

    while min_s <= max_s:
        need = 0
        mid_s = (min_s + max_s) // 2
        for num in nums:
            if num >= mid_s:
                break
            need += (mid_s - num) ** 2
            if need > B:
                break
        if need > B:
            max_s = mid_s-1
        else:
            result = mid_s
            min_s = mid_s+1
    return result

print(bs())
            
    