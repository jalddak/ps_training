N, K = list(map(int, input().split()))

l = []
for _ in range(N):
    W, V = list(map(int, input().split()))
    l.append([W, V])

l.sort(key = lambda x:x[0])

dp = []
for i in range(N):
    W, V = l[i]
    dic = {}
    
    if i > 0:
        before = dp[i-1]
        for key in before:
            dic[key] = before[key]
        for key in before:
            weight = key + W
            if weight <= K:
                if weight not in dic:
                    dic[weight] = before[key] + V
                else:
                    dic[weight] = max(before[weight], before[key]+V)
    
    if W <= K:
        if W not in dic:
            dic[W] = V
        else:
            dic[W] = max(dic[W], V)
    dp.append(dic)

value = list(dp[-1].values())
if len(value) == 0:
    print(0)
else:
    print(max(list(dp[-1].values())))