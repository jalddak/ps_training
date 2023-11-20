import sys
input = sys.stdin.readline

N = int(input())

l = [0 for i in range(10001)]

for _ in range(N):
    l[int(input())] += 1

for i in range(len(l)):
    for _ in range(l[i]):
        print(i)