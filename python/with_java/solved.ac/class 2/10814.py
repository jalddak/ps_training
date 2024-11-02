import sys
input = sys.stdin.readline

n = int(input())
arr = []
d = dict()
for i in range(n):
    age, name = input().split()
    arr.append([int(age), i])
    d[i] = name

arr.sort(key=lambda x:(x[0], x[1]))
for i in range(n):
    age, name = arr[i][0], d[arr[i][1]]
    print(age, name)