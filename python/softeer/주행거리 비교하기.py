import sys

A, B = map(int, input().split())
if A == B:
    print("same")
    exit()
print('A') if A > B else print('B')