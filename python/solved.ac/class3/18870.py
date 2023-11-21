N = int(input())

l = list(map(int, input().split()))

l_del_r = sorted(list(set(l)))

d = {}
for i in range(len(l_del_r)):
    d[l_del_r[i]] = i

for n in l:
    print(d[n], end = " ")