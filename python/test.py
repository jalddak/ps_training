n = int(input())
nums = list(map(int, input().split()))

def check(arr, index, num):
    return arr[index] < num

def bs(arr, num, s, e):
    while s + 1 < e:
        mid = (s+e) // 2
        if check(arr, mid, num):
            s = mid
        else:
            e = mid
    
    if e == len(arr):
        arr.append(num)
        return
    arr[e] = num


arr = []
for num in nums:
    bs(arr, num, -1, len(arr))

print(len(arr))