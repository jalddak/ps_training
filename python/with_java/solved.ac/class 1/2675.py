import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    it, cmd = input().split()
    it = int(it)
    answer = ''
    for s in cmd:
        for _ in range(it):
            answer += s
    print(answer)