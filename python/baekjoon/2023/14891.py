from collections import deque

tobs = []
for _ in range(4):
    string = input()
    tob = deque([])
    for i in range(8):
        tob.append(int(string[i]))
    tobs.append(tob)

k = int(input())
cmds = deque([])
for _ in range(k):
    cmd = list(map(int, input().split()))
    cmd[0] -= 1
    cmds.append(cmd)

# d : 영향 받은 톱니위치  (왼 : -1, 오 : 1, init : 0)
# n : 톱니 번호 (왼쪽부터 0, 1, 2, 3)
# r : 회전 방향 (반시계 : -1, 시계 : 1)
def rotate(d, n, r):
    global tobs
    if n > 0 and d != -1:
        if tobs[n-1][2] != tobs[n][6]:
            rotate(1, n-1, -r)
    if n < 3 and d != 1:
        if tobs[n][2] != tobs[n+1][6]:
            rotate(-1, n+1, -r)

    if r == -1:
        tobs[n].append(tobs[n].popleft())
    elif r == 1:
        tobs[n].appendleft(tobs[n].pop())


def main():
    global cmds, tobs
    result = 0
    while len(cmds) > 0:
        cmd = cmds.popleft()
        rotate(0, cmd[0], cmd[1])
    for i in range(len(tobs)):
        if tobs[i][0] == 1:
            result += 2 ** i
    print(result)

if __name__ == '__main__':
    main()