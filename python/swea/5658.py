from collections import deque

T = int(input())
for t in range(1, T+1):
    n, k = map(int, input().split())
    nums = list(input())
    answer = 0
    num_length = n // 4
    num_set = set()
    for _ in range(num_length):
        for i in range(0, n, num_length):
            num_set.add(int("".join(nums[i:i+num_length]), 16))
        nums = deque(nums)
        nums.append(nums.popleft())
        nums = list(nums)
    candidate = list(num_set)
    candidate.sort(reverse=True)
    answer = candidate[k-1]
    print("#" + str(t) + " " + str(answer))