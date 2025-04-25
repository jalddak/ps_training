from collections import deque

answer = []

for _ in range(10):
    tc = int(input())
    sb = "#" + str(tc) + " "

    nums = deque(map(int, input().split()))

    x = 1
    while nums[-1] != 0:
        n = nums.popleft()
        n = n - x if n - x > 0 else 0
        x = x + 1 if x + 1 <= 5 else 1
        nums.append(n)
    
    sb += " ".join(map(str, nums))
    answer.append(sb)

for a in  answer:
    print(a)