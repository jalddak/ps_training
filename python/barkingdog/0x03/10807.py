n = int(input())
nums = list(map(int, input().split()))
t = int(input())

cnt = 0
for num in nums:
    if num == t:
        cnt += 1
print(cnt)