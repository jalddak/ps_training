n, m = map(int, input().split())
answer = []

def back(depth, start, result):
    global n, m
    if depth == m:
        answer.append(" ".join(map(str, result)))
        return
    
    for i in range(start, n+1):
        result.append(i)
        back(depth + 1, i + 1, result)
        result.pop()

back(0, 1, [])
for a in answer:
    print(a)