import sys
input = sys.stdin.readline

M = int(input())

"""
add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
all: S를 {1, 2, ..., 20} 으로 바꾼다.
empty: S를 공집합으로 바꾼다.
"""

S = set([])
for _ in range(M):
    command = input().split()
    if command[0] == "add":
        S.add(int(command[1]))
    elif command[0] == "remove":
        if int(command[1]) in S:
            S.remove(int(command[1]))
    elif command[0] == "check":
        if int(command[1]) in S:
            print(1)
        else:
            print(0)
    elif command[0] == "toggle":
        if int(command[1]) in S:
            S.remove(int(command[1]))
        else:
            S.add(int(command[1]))
    elif command[0] == "all":
        S = set([i for i in range(1, 21)])
    elif command[0] == "empty":
        S.clear()