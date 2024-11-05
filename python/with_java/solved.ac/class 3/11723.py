# import sys
# input = sys.stdin.readline

# n = int(input())
# s = [0 for _ in range(21)]
# answer = []

# for _ in range(n):
#     cmd = list(input().split())
#     command = cmd[0]
#     if len(cmd) == 2:
#         num = int(cmd[1])
#     if command == "add":
#         s[num] = 1
#     elif command == "remove":
#         s[num] = 0
#     elif command == "check":
#         answer.append(s[num])
#     elif command == "toggle":
#         s[num] = 0 if s[num] == 1 else 1
#     elif command == "all":
#         for i in range(1, 21):
#             s[num] = 1
#     elif command == "empty":
#         for i in range(1, 21):
#             s[num] = 0

# for a in answer:
#     print(a)

import sys
input = sys.stdin.readline

n = int(input())
s = set()
answer = []

for _ in range(n):
    cmd = list(input().split())
    command = cmd[0]
    if len(cmd) == 2:
        num = int(cmd[1])
    if command == "add":
        s.add(num)
    elif command == "remove":
        if num in s:
            s.remove(num)
    elif command == "check":
        answer.append(1 if num in s else 0)
    elif command == "toggle":
        if num in s:
            s.remove(num)
        else:
            s.add(num)
    elif command == "all":
        for i in range(1, 21):
            s.add(i)
    elif command == "empty":
        s.clear()

for a in answer:
    print(a)