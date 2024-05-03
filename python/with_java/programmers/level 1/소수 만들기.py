def solution(nums):
    answer = 0
    max_sum = sum(sorted(nums)[-3:])
    checked = [False for _ in range(max_sum+1)]
    prime_nums = set()
    for num in range(2, max_sum+1):
        if checked[num]:
            continue
        prime_nums.add(num)
        for m in range(num, max_sum+1, num):
            checked[m] = True
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] in prime_nums:
                    answer += 1
    return answer