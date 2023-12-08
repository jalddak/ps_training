import sys
input = sys.stdin.readline

N, M = map(int, input().split())

facts = set(map(int, input().split()[1:]))

partys = [set(map(int, input().split()[1:])) for _ in range(M)]
checked = [False for _ in range(M)]

i = 0
while i < M:
    if partys[i] & facts and not checked[i]:
        checked[i] = True
        facts |= partys[i]
        i = -1
    i += 1

result = 0
for r in checked:
    if not r:
        result += 1

print(result)