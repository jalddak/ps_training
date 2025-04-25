import sys
input = sys.stdin.readline

from collections import deque

t = int(input())
answers = []

for _ in range(t):
    p = input()
    n = int(input())
    temp = input()[1:-2].split(",")
    nums = []
    if temp[0].isdigit():
        nums = deque(map(int, temp))
    d = 1
    flag = True

    for cmd in p:
        if cmd == "R":
            d = -d
        elif cmd == "D":
            if not nums:
                flag = False
                break
            if d == 1:
                nums.popleft()
            elif d == -1:
                nums.pop()
    
    if flag:
        if d == -1:
            nums.reverse()
        answers.append("[" + ",".join(map(str, nums)) + "]")
    else:
        answers.append("error")

for a in answers:
    print(a)
    