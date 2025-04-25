n, m = map(int, input().split())

temp = list(map(int, input().split()))
tn = temp[0]
tInfo = temp[1:]

from collections import deque
q = deque()

checked = [False for _ in range(n+1)]
for num in tInfo:
    checked[num] = True
    q.append(num)


partys = []
pChecked = [False for _ in range(m)]
for _ in range(m):
    temp = list(map(int, input().split()))
    pn = temp[0]
    pInfo = set(temp[1:])
    partys.append(pInfo)

while q:
    num = q.popleft()
    for i in range(m):
        if num not in partys[i] or pChecked[i]:
            continue
        pChecked[i] = True
        for pnum in partys[i]:
            if checked[pnum]:
                continue
            checked[pnum] = True
            q.append(pnum)

answer = pChecked.count(False)
print(answer)