from itertools import combinations

while True:
    l = list(map(int, input().split()))
    k = l[0]
    if k == 0:
        break
    S = l[1:]
    candidates = list(map(list,combinations(S, 6)))
    for c in candidates:
        for n in c:
            print(n, end = ' ')
        print()
    print()
    
