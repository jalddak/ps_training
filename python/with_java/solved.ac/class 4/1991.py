n = int(input())
edges = dict()

for _ in range(n):
    p, lc, rc = input().split()
    edges[p] = [lc, rc]

result = [[] for _ in range(3)]

def solution(node):
    result[0].append(node)
    for i in range(2):
        if i == 1:
            result[1].append(node)
        if edges[node][i] == '.':
            continue
        solution(edges[node][i])
    result[2].append(node)


solution('A')

for r in result:
    print("".join(r))