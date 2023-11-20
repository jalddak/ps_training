# from itertools import combinations

# T = int(input())

# for round in range(1, T+1):
#     rstr = "#" + str(round) + " "
#     N = int(input())
#     nl = list(map(int, input().split()))
#     d = set([0])
#     for n in range(1, N+1):
#         ts = set(map(sum, list(combinations(nl, n))))
#         print(ts)
#         d = d.union(ts)
#     print(rstr + str(len(d)))


T = int(input())

for round in range(1, T+1):
    rstr = "#" + str(round) + " "
    N = int(input())
    nl = list(map(int, input().split()))
    visited = [0 for _ in range(sum(nl) + 1)]
    visited[0] = 1
    result = [0]
    for n in nl:
        for r in result[:]:
            print(n+r)
            if visited[n+r] == 0:
                visited[n+r] = 1
                result.append(n+r)
    print(rstr + str(len(result)))

