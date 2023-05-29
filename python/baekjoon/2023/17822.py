from collections import deque

n, m, t = list(map(int, input().split()))
pan = [deque(list(map(int, input().split()))) for _ in range(n)]
rotate_method = [list(map(int, input().split())) for _ in range(t)]

def rotate(pan, x, d, k):
    global n, m, t
    for i in range(n):
        if (i+1) % x == 0:
            for _ in range(k):
                if d == 0:
                    pan[i].appendleft(pan[i].pop())
                else:
                    pan[i].append(pan[i].popleft())

def check(pan):
    global n, m, t
    copy = []
    for i in range(n):
        copy.append(deque(list(pan[i])))
    dy = [0, 1]
    dx = [1, 0]

    method = 0
    for i in range(n):
        for j in range(m):
            for k in range(2):
                ny = i + dy[k]
                nx = j + dx[k]
                if nx == m:
                    nx -= m
                if ny < n and pan[i][j] != 0 and pan[i][j] == pan[ny][nx]:
                    method = 1
                    copy[i][j] = 0
                    copy[ny][nx] = 0

    if method == 0:
        cnt = 0
        numsum = 0
        for i in range(n):
            for j in range(m):
                if copy[i][j] != 0:
                    cnt += 1
                    numsum += copy[i][j]

        if cnt != 0:
            average = numsum / cnt
            for i in range(n):
                for j in range(m):
                    if copy[i][j] != 0:
                        if copy[i][j] > average:
                            copy[i][j] -= 1
                        elif copy[i][j] < average:
                            copy[i][j] += 1
    
    return copy

def main():
    global n, m, t, pan, rotate_method

    for i in range(t):
        x, d, k = rotate_method[i]
        rotate(pan, x, d, k)
        pan = check(pan)
    
    result = 0
    for i in range(n):
        for j in range(m):
            result += pan[i][j]
    print(result)

if __name__ == '__main__':
    main()