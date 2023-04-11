def solution(n, computers):
    answer = 0

    queue = []
    visited = []

    for a in range(n):
        if a not in visited:
            queue.append(a)
            answer += 1

            while queue :
                now = queue.pop(0)    
                for i in range(n):
                    if computers[now][i] == 1 and i not in visited:
                        visited.append(i)
    print(answer)
    return answer


solution(4, [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 1, 0, 1]])
solution(6, [[1,1,0,0,0,1], [0,1,0,0,0,0], [0,0,1,0,1,0], [0,0,0,1,0,0], [0,0,1,0,1,0], [0,0,0,1,1,1]])