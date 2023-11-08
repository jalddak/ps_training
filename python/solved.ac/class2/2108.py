import sys
input = sys.stdin.readline

N = int(input())
l = [int(input()) for _ in range(N)]

n1 = sum(l)/len(l)
print(int(n1+0.5) if n1 > 0 else int(n1-0.5))
print(sorted(l)[len(l)//2])
dict = {}
for n in l:
    if n not in dict:
        dict[n] = 1
    else:
        dict[n] += 1
l2 = list(zip(dict.keys(),dict.values()))
l2.sort(key=lambda x:(-x[1], x[0]))
if len(l2) > 1 and l2[0][1] == l2[1][1]:
    print(l2[1][0])
else:
    print(l2[0][0])
print(max(l)-min(l))