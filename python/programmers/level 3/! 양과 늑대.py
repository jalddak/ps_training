# https://blog.encrypted.gg/1029
# 바킹독님 아이디어 참고

def make_edges(n, edges):
    result = [[] for _ in range(n)]
    for p, c in edges:
        result[p].append(c)
    return result

def recursion(node, info, edges, sheep, wolf, candidates, visited, result):
    if info[node] == 0:
        sheep += 1
    if info[node] == 1:
        wolf += 1
    if sheep <= wolf:
        return result
    
    result = max(result, sheep)
    for i in range(len(edges[node])):
        candidates.append(edges[node][i])
    for next in candidates:
        if visited[next]:
            continue
        visited[next] = True
        result = recursion(next, info, edges, sheep, wolf, candidates, visited, result)
        visited[next] = False
    for i in range(len(edges[node])):
        candidates.pop()
    
    return result

def recursion_with_bit_masking(node, info, edges, sheep, wolf, candidates, visited, result, bit_masking):
    if info[node] == 0:
        sheep += 1
    if info[node] == 1:
        wolf += 1
    if sheep <= wolf:
        return result
    
    result = max(result, sheep)
    for i in range(len(edges[node])):
        candidates.append(edges[node][i])
    for next in candidates:
        if visited[next] == '1':
            continue
        visited[next] = '1'
        
        # 추가
        if bit_masking[int(''.join(visited), 2)]:
            visited[next] = '0'
            continue
        bit_masking[int(''.join(visited), 2)] = True
        result = recursion_with_bit_masking(next, info, edges, sheep, wolf, candidates, visited, result, bit_masking)
        visited[next] = '0'
    for i in range(len(edges[node])):
        candidates.pop()
    
    return result

def solution(info, edges):
    answer = 0
    n = len(info)
    edges = make_edges(n, edges)
    visited = [False for _ in range(n)]
    # answer = recursion(0, info, edges, 0, 0, [], visited, answer)
    
    # 바킹독 문제 풀이
    # 비트마스킹을 사용해서 똑같이 방문한적 있던 모양의 트리는 중복해서 탐색하지 않게해야함 
    # 그렇지 않으면 시간초과 날 수 있음.
    bit_masking = [False for _ in range(2**n)]
    visited = ['0' for _ in range(n)]
    visited[0] = '1'
    bit_masking[int(''.join(visited), 2)] = True
    answer = recursion_with_bit_masking(0, info, edges, 0, 0, [], visited, answer, bit_masking)
    
    
    return answer