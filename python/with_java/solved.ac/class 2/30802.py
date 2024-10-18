# import sys
# input = sys.stdin.readline

# N = int(input())
# ts = list(map(int, input().split()))
# T, P = map(int, input().split())

# a1 = 0
# for t in ts:
#     a1 += t // T
#     a1 += 1 if t % T > 0 else 0
# print(a1)
# print(str(N//P) + " " + str(N%P))

n = int(input())
sizes = list(map(int, input().split()))
t, p = map(int, input().split())

a1 = 0

for s in sizes:
    a1 += s // t + (1 if s%t > 0 else 0)
print(a1)
print(str(n//p) + " " + str(n%p))