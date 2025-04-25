n, m = map(int, input().split())

def recursion(depth, result, start):
    if depth == m:
        print(" ".join(map(str, result)))
        return
    
    for i in range(start, n+1):
        result.append(i)
        recursion(depth + 1, result, i)
        result.pop()

recursion(0, [], 1)