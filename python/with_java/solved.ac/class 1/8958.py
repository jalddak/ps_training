import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    cmd = input()
    score = 0
    plus = 1
    for c in cmd:
        if c == 'O':
            score += plus
            plus += 1
        else:
            plus = 1
    print(score)