import sys
input = sys.stdin.readline

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

def make_sum_sub(n, L):
    sumL = [0]
    subL = {}
    for i in range(n):
        num = L[i]
        sumL.append(sumL[-1]+num)
        for j in range(i+1):
            sub = sumL[i+1]-sumL[j]
            if sub not in subL:
                subL[sub] = 1
            else:
                subL[sub] += 1
    return sumL, subL

sumA, subA = make_sum_sub(n, A)
sumB, subB = make_sum_sub(m, B)

sortA = sorted(list(subA.keys()))
sortB = sorted(list(subB.keys()))

al = 0
br = len(sortB)-1
answer = 0
while True:
    t = sortA[al] + sortB[br]
    if t == T:
        answer += subA[sortA[al]] * subB[sortB[br]]
        al += 1
        br -= 1
        if al >= len(sortA) or br < 0:
            break
    elif t < T:
        al += 1
        if al >= len(sortA):
            break
    else:
        br -= 1
        if br < 0:
            break

print(answer)