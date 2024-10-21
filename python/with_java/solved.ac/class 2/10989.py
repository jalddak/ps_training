cnts = [0 for _ in range(10001)]
n = int(input())

for _ in range(n):
    cnts[int(input())] += 1

for i in range(10001):
    for _ in range(cnts[i]):
        print(i)