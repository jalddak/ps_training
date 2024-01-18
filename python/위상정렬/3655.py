import sys
input = sys.stdin.readline

T = int(input())

def switching(p, c):
    childs[p].remove(c)
    pcnt[p] += 1
    childs[c].add(p)
    pcnt[c] -= 1

result = []
for _ in range(T):
    n = int(input())
    ly = list(map(int, input().split()))
    childs = [set() for _ in range(n+1)]
    pcnt = [0 for _ in range(n+1)]
    for i in range(n):
        childs[ly[i]] = set(ly[i+1:])
        pcnt[ly[i]] = i

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        if a in childs[b]:
            switching(b, a)
        else:
            switching(a, b)

    pcnt = pcnt[1:]
    if len(pcnt) != len(set(pcnt)):
        result.append("IMPOSSIBLE")
    else:
        temp = list(zip(pcnt, [i for i in range(1, n+1)]))
        temp.sort(key=lambda x:x[0])
        result.append([temp[i][1] for i in range(n)])

for r in result:
    if r == "IMPOSSIBLE":
        print(r)
    else:
        print(" ".join(map(str, r)))
