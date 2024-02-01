import sys
input = sys.stdin.readline

n, k = map(int, input().split())
S = list(map(int, input().split()))
pSum = [0]
for score in S:
    pSum.append(pSum[-1] + score)

for _ in range(k):
    s, e = map(int, input().split())
    print("{:.2f}".format(int(((pSum[e]-pSum[s-1])/(e-s+1))*100 + 0.5) / 100))