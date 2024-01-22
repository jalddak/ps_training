import sys
input = sys.stdin.readline

n = int(input())

A, B, C, D = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

def makeSum(l, r):
    d = {}
    for n in l:
        for m in r:
            d[n+m] = d.get(n+m, 0) + 1
    return d

ld = makeSum(A, B)
rd = makeSum(C, D)

ll = sorted(list(ld.keys()))
rl = sorted(list(rd.keys()))

left, right = 0, len(rl)-1

result = 0
while left < len(ll) or right >= 0:
    ln, rn = ll[left], rl[right]
    if ln + rn == 0:
        result += ld[ln] * rd[rn]
        left += 1
        right -= 1
    elif ln + rn < 0:
        left += 1
    else:
        right -= 1

print(result)

# def bs(num, l):
#     global n
#     left, right = 0, len(l)-1

#     while left <= right:
#         mid = (left + right) // 2
#         if l[mid] == num:
#             return [True, l[mid]]
#         elif l[mid] < num:
#             left = mid + 1
#         else:
#             right = mid - 1
    
#     return [False, 0]

# result = 0
# for ln in ld:
#     find, rn = bs(-ln, rl)
#     if find:
#         result += ld[ln] * rd[rn]