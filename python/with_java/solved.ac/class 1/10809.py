apb = [-1 for _ in range(26)]

s = input()
i = 0
for a in s:
    index = ord(a)-97
    if apb[index] == -1:
        apb[index] = i
    i += 1

print(*apb)