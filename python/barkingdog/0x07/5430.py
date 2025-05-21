from collections import deque

t = int(input())

answer = []
for _ in range(t):
    p = input()
    n = int(input())
    arr = input()[1:-1].split(",")
    nums = deque()
    if arr[0] != "":
        nums = deque(map(int, arr))
    d = -1

    flag = True
    for c in p:
        if c == "R":
            d = -d
        if c == "D":
            if not nums:
                flag = False
                break
            elif d == -1:
                nums.popleft()
            elif d == 1:
                nums.pop()

    if d == 1:
        nums.reverse()
    if not flag:
        answer.append("error")
    else:
        answer.append("[" + ",".join(map(str, nums)) + "]")

for a in answer:
    print(a)