n, k = map(int, input().split())
l = [i for i in range(1, n+1)]
result = []

index = k-1
while len(result) != n:
    result.append(l.pop(index))
    index += k - 1
    while index >= len(l) and len(l) != 0:
        index -= len(l)

print("<", end = "")
for n in result:
    if result[-1] == n:
        print(str(n), end = "")
        break
    print(str(n), end = ", ")
print(">")