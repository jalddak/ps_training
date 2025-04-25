n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))


# 5퍼틀 나옴.
# 아래 반례.
# 100
# 13 29 50 36 2 27 45 2 9 10 4 29 37 17 34 34 84 90 92 83 43 25 54 12 29 53 100 74 89 25 87 84 75 45 1 12 10 51 11 7 27 38 10 40 2 41 83 3 87 45 35 44 35 20 73 44 73 22 64 18 100 33 3 20 61 82 61 69 94 20 20 2 3 33 25 30 51 46 18 47 60 55 52 94 74 86 8 50 67 24 36 41 67 23 16 19 62 37 68 10 
# 100
# 57 96 52 17 39 62 25 49 12 14 55 100 65 42 65 83 29 67 75 18 60 25 40 67 22 25 95 36 69 51 94 49 50 18 92 65 91 15 22 25 77 23 55 53 30 54 12 45 26 15 96 84 60 19 93 45 1 20 27 26 42 37 20 89 16 57 64 68 72 17 43 6 38 94 46 16 21 56 9 64 45 47 4 81 50 51 60 92 14 84 83 7 1 61 69 41 54 64 64 44 

result = []
checked = [False for _ in range(m)]

for i in range(n):
    for j in range(m):
        if a[i] == b[j]:
            if checked[j]:
                continue
            while result and result[-1][0] < a[i] and (len(result) == 1 or result[-2][0] < a[i] or result[-2][1] < j):
                num, index = result.pop()
                checked[index] = False
            if result and result[-1][1] >= j:
                continue
            result.append([a[i], j])
            checked[j] = True
            break

print(len(result))
if result:
    print(" ".join(map(str, map(lambda x:x[0], result))))


# 반례 해결해보자 - 해결함.
result = []
checked = [False for _ in range(m)]

for i in range(n):
    for j in range(m):
        if a[i] == b[j]:
            if checked[j]:
                continue
            depth = 1
            while len(result) >= depth and result[-depth][0] < a[i]:
                depth += 1

            if len(result) >= depth and result[-depth][1] >= j:
                continue

            for k in range(1, depth):
                checked[result[-k][1]] = False
            if depth > 1:
                result = result[:-depth+1]


            result.append([a[i], j])
            checked[j] = True
            break

print(len(result))
if result:
    print(" ".join(map(str, map(lambda x:x[0], result))))


# set 활용 코드 - 정답

result = []
temp = set(a) & set(b)
while temp:
    maxN = max(temp)
    result.append(maxN)
    a = a[a.index(maxN)+1:]
    b = b[b.index(maxN)+1:]
    temp = set(a) & set(b)

print(len(result))
if result:
    print(" ".join(map(str, result)))