import sys
input = sys.stdin.readline

n = int(input())
if n == 0:
    print(0)
    exit()

scores = []
for _ in range(n):
    scores.append(int(input()))

scores.sort()
l = len(scores)
e = (int) (l * 0.15 + 0.5)
print((int)(sum(scores[e:l-e]) / (l - 2*e) + 0.5))