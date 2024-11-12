import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    d = {}
    for _ in range(n):
        name, gear = input().split()
        if gear in d:
            d[gear].append(name)
        else:
            d[gear] = [name]
    
    answer = 1
    for gear in d:
        answer *= len(d[gear]) + 1
    print(answer - 1)