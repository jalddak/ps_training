tcCnt = int(input())

def recursion(nums, n, k, index, cur):
    result = 0
    for i in range(index, n):
        next = cur + nums[i]
        if next > k:
            break
        if next == k:
            result += 1
            continue
        result += recursion(nums, n, k, i + 1, next)

    return result

answer = []
for tc in range(1, tcCnt + 1):
    n, k = map(int, input().split())

    nums = list(map(int, input().split()))
    nums.sort()
    result = recursion(nums, n, k, 0, 0)

    sb = "#" + str(tc) + " " + str(result)
    answer.append(sb)

print("\n".join(answer))