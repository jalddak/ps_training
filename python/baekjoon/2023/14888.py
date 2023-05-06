n = int(input())
a = list(map(int, input().split()))

# + - * //
op = list(map(int, input().split()))

maxnum = -1000000000
minnum = 1000000000

def dfs(num, depth, op):
    global a, maxnum, minnum
    if depth == len(a):
        maxnum = max(num, maxnum)
        minnum = min(num, minnum)
    
    for i in range(4):
        opc = op[:]
        numc = num
        if op[i] == 0:
            continue
        if i == 0:
            numc += a[depth]
        elif i == 1:
            numc -= a[depth]
        elif i == 2:
            numc *= a[depth]
        elif i == 3:
            if numc // a[depth] < 0 and numc % a[depth] != 0:
                numc = numc // a[depth] + 1
            else:
                numc //= a[depth]
        opc[i] -= 1
        dfs(numc, depth + 1, opc)


if __name__ == '__main__':
    dfs(a[0], 1, op)
    print(maxnum)
    print(minnum)