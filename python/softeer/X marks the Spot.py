import sys
input = sys.stdin.readline

N = int(input())

result = []
for _ in range(N):
    S, T = input().split()
    index = -1
    for i in range(len(S)):
        if S[i] in {'x', 'X'}:
            index = i
            break
    result.append(T[index].upper())

print("".join(result))
    
            