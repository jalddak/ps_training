n = int(input())
nums = list(map(int, input().split()))
sortL = sorted(list(set(nums)))
d = {}
pn = 0
for num in sortL:
    if num not in d:
        d[num] = pn
        pn += 1

answer = []
for num in nums:
    answer.append(d[num])

print(" ".join(map(str, answer)))