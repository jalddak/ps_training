import sys
from collections import deque

input = sys.stdin.readline
N = int(input())

queue = deque([])
for _ in range(N):
    command = input().split()
    if command[0] == "push_front":
        queue.appendleft(int(command[1]))
    elif command[0] == "push_back":
        queue.append(int(command[1]))
    elif command[0] == "pop_front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif command[0] == "pop_back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop())
    elif command[0] == "size":
        print(len(queue))
    elif command[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif command[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])



"""
push_front X: 정수 X를 덱의 앞에 넣는다.
push_back X: 정수 X를 덱의 뒤에 넣는다.
pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 덱에 들어있는 정수의 개수를 출력한다.
empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
"""