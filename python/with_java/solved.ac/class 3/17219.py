import sys
input = sys.stdin.readline

n, m = map(int ,input().split())

pwds = dict()
for _ in range(n):
    site, pwd = input().split()
    pwds[site] = pwd

for _ in range(m):
    print(pwds[input()[:-1]])