import sys
input = sys.stdin.readline

n = int(input())

nums = []
cnts = dict()
for _ in range(n):
    num = int(input())
    nums.append(num)
    cnts[num] = 1 if num not in cnts else cnts[num] + 1

nums.sort()
cnts = list(cnts.items())
cnts.sort(key=lambda x:(-x[1], x[0]))

s = sum(nums)
print(int(s/n + 0.5) if s > 0 else int(s/n - 0.5))
print(nums[n // 2])
print(cnts[0][0] if n == 1 or cnts[0][1] != cnts[1][1] else cnts[1][0])
print(nums[-1]-nums[0])