# n = int(input())
# m = int(input())

# ip = list(input())

# from collections import deque
# temp = deque([])
# check = ""
# for i in range(n*2+1):
#     if i%2 == 0:
#         check += "I"
#     else:
#         check += "O"

# answer = 0
# for i in range(m):
#     temp.append(ip[i])
#     if len(temp) == n * 2 + 1:
#         if "".join(temp) == check:
#             answer += 1
#         temp.popleft()

# print(answer)

n = int(input())
m = int(input())

ip = input()

check = 'O'
cnt = 0
answer = 0
for c in ip:
    if c == 'I':
        if check == 'I':
            cnt = 0
        if cnt >= n:
            answer += 1
        check = 'I'
    elif c == 'O':
        if check == 'O':
            cnt = 0
        elif check == 'I':
            cnt += 1
        check = 'O'

print(answer)