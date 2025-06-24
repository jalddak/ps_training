n, s = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
answer = 0

def back(start, result):
    global answer

    for i in range(start, n):
        result += nums[i]
        if result == s:
            answer += 1
        back(i + 1, result)
        result -= nums[i]

back(0, 0)
print(answer)