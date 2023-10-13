# DFS

from itertools import combinations

N = int(input())

num = [i for i in range(1, N+1)]
population = [0] + list(map(int, input().split()))
tree = {}

for i in range(1, N+1):
    tree[i] = list(map(int, input().split()))[1:]

candidates = []
for i in range(1, N//2+1):
    candidates += list(map(list, list(combinations(num, i))))
    
result = -1

for A in candidates:
    B = list(set(num) - set(A))
    visited = [True] + [False for _ in range(N)]

    visited[A[0]] = True
    stackA = [A[0]]
    checkA = [A[0]]
    
    while len(stackA) != 0:
        n = stackA.pop()
        for i in tree[n]:
            if not visited[i] and i in A:
                visited[i] = True
                checkA.append(i)
                stackA.append(i)
    
    if set(A) == set(checkA):
        visited[B[0]] = True
        stackB = [B[0]]
        checkB = [B[0]]
        
        while len(stackB) != 0:
            n = stackB.pop()
            for i in tree[n]:
                if not visited[i] and i in B:
                    visited[i] = True
                    checkB.append(i)
                    stackB.append(i)

        if set(B) == set(checkB):
            popuA = 0
            popuB = 0
            for n in A:
                popuA += population[n]
            for n in B:
                popuB += population[n]
            AmB = abs(popuA - popuB)
            if result == -1:
                result = AmB
            else:
                result = min(AmB, result)

print(result)
