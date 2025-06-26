n, m = map(int, input().split())
answer = []

def back(depth, result):
    global n, m
    if depth == m:
        answer.append(" ".join(map(str, result)))
        return
    
    for i in range(1, n+1):
        result.append(i)
        back(depth + 1, result)
        result.pop()

back(0, [])
for a in answer:
    print(a)