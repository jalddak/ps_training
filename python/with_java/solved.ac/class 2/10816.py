n = int(input())
arr = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))

d = dict()
for num in arr:
    d[num] = 1 if num not in d else d[num] + 1

answer = []
for num in nums:
    answer.append(d[num] if num in d else 0)

print(" ".join(map(str, answer)))