import sys
input = sys.stdin.readline

N = int(input())
ts = list(map(int, input().split()))
T, P = map(int, input().split())

a1 = 0
for t in ts:
    a1 += t // T
    a1 += 1 if t % T > 0 else 0
print(a1)
print(str(N//P) + " " + str(N%P))