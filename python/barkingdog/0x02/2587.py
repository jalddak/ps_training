nums = []

for _ in range(5):
    nums.append(int(input()))

print(sum(nums) // len(nums))
nums.sort()
print(nums[len(nums) // 2])