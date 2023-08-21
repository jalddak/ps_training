# BFS

from collections import deque

T = int(input())

for _ in range(T):
    A, B = list(map(int, input().split()))
    visited = [False for _ in range(10000)]

    queue = deque([[A, '']])
    visited[A] = True
    while len(queue) != 0:
        n, result = queue.popleft()
        copy = n
        check = 0
        for command in ['D', 'S', 'L', 'R']:
            n = copy
            if command == 'D':
                n *= 2
                n %= 10000
            elif command == 'S':
                if n == 0:
                    n = 9999
                else:
                    n -= 1
            elif command == 'L':
                first = n // 1000
                n %= 1000
                n *= 10
                n += first
            elif command == 'R':
                first = n % 10
                n //= 10
                n += (1000*first)
            if n == B:
                check = 1
                print(result+command)
                break
            if not visited[n]:
                visited[n] = True
                queue.append([n, result+command])
        if check == 1:
            break