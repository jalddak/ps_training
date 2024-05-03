def recursion(k, dungeons, visited, depth, result):
    for i in range(len(dungeons)):
        if visited[i]:
            continue
        need, use = dungeons[i]
        if k < need:
            continue
        k -= use
        visited[i] = True
        result = max(result, recursion(k, dungeons, visited, depth+1, depth+1))
        visited[i] = False
        k += use
    return result

def solution(k, dungeons):
    visited = [False for _ in range(len(dungeons))]
    return recursion(k, dungeons, visited, 0, 0)