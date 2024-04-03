def recursion(n, depth, location, visited, result):
    if depth == n:
        result += 1
    else:
        for i in range(n):
            if visited[i]:
                continue

            check = True
            for j in range(1, depth+1):
                if location[depth-j] in [i-j, i+j]:
                    check = False
                    break
            if not check:
                continue

            location[depth] = i
            visited[i] = True
            result = recursion(n, depth+1, location, visited, result)
            visited[i] = False
            location[depth] = -1
    
    return result

def solution(n):
    answer = 0
    visited = [False for _ in range(n)]
    location = [-1 for _ in range(n)]
    answer = recursion(n, 0, location, visited, answer)
        
    return answer