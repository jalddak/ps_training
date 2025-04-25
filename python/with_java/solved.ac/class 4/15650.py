n, m = map(int, input().split())

def recursion(depth, result, start):
    if depth == m:
        print(" ".join(map(str, result)))
    
    for i in range(start, n+1):
        result.append(i)
        recursion(depth + 1, result, i+1)
        result.pop()

recursion(0, [], 1)