tcCnt = int(input())

def bs(arr, target):
    l = -1
    r = len(arr)
    while l + 1 < r:
        mid = (l + r) // 2
        if arr[mid] < target:
            l = mid
        elif arr[mid] > target:
            r = mid
        else:
            break

    if r == len(arr):
        arr.append(target)
    else:
        arr[r] = target

answer = []
for tc in range(1, tcCnt + 1):
    n = int(input())
    nums = list(map(int, input().split()))

    arr = []
    for num in nums:
        bs(arr, num)

    result = len(arr)

    sb = "#" + str(tc) + " " + str(result)
    answer.append(sb)
print("\n".join(answer))