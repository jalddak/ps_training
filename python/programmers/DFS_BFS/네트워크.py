# 내 방식보단 다른 사람이 푼 bfs / dfs 방식이 훨씬 좋아보였음
# ----------------------------BFS--------------------------------------
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
                        queue.append(i)
    return answer
# ---------------------------------DFS------------------------------------
def solution(n, computers):
    answer = 0
    visited = []

    def newRoot (i,n,visited):
        for j in range(n):
            if computers[i][j] == 1 and j not in visited:
                visited.append(j)
                newRoot(j,n,visited)

    for i in range(n):
        if i not in visited :
            visited.append(i)
            answer = answer+1
            newRoot(i,n,visited)

    return answer
# -------------------------------내방식------------------------------------
def solution(n, computers):
    answer = 0
    networks = []
    for i in range(n):
        network = []
        union_check = 0
        union_index = []
        for j in range(n):
            if computers[i][j] == 1:
                network.append(j)
                for k in range(len(networks)):
                    if j in networks[k] and k not in union_index:
                        union_check = 1
                        union_index.append(k)
        union_index.sort()
        if union_check == 0:
            networks.append(network)
        else:
            for i in range(len(union_index)):
                network += networks.pop(union_index[i]-i)
            networks.append(list(set(network)))
    answer = len(networks)
    return answer

