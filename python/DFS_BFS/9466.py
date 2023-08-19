# DFS

T = int(input())

for _ in range(T):
    n = int(input())
    members = list(map(lambda x:x-1, list(map(int, input().split()))))
    visited = [False for _ in range(n)]
    result = n
    for i in range(n):
        if not visited[i]:
            nlist = [i]
            visited[i] = True
            stack = [[i, 1]]
            while len(stack) != 0:
                n1, depth = stack.pop()
                n2 = members[n1]
                if not visited[n2]:
                    nlist.append(n2)
                    visited[n2] = True
                    stack.append([n2, depth+1])
                elif n2 in nlist:
                    result -= (depth - nlist.index(n2))

    print(result)