import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dna = [list(input())[:m] for _ in range(n)]

def calc(dna):
    while True:
        ndna = []
        visited = [False for _  in range(len(dna))]
        for i in range(len(dna)):
            if visited[i]:
                continue
            first = dna[i]
            visited[i] = True
            ndna.append(first)
            for j in range(i+1, len(dna)):
                if visited[j]:
                    continue
                second = dna[j]
                
                check = True
                result = []
                for index in range(m):
                    if first[index] != second[index] and first[index] != '.' and second[index] != '.':
                        check = False
                        break
                    alphabet = first[index] if first[index] != '.' else second[index]
                    result.append(alphabet)
                
                if check:
                    visited[j] = True
                    ndna.pop()
                    ndna.append(result)
                    break
                    
        if len(dna) == len(ndna):
            return len(ndna)
            break
        dna = ndna


answer = []
dna.sort(key=lambda x:([x[i] for i in range(m)]))
answer.append(calc(dna))
dna.sort(key=lambda x:[x[i] for i in range(m-1, -1, -1)])
answer.append(calc(dna))

print(min(answer))