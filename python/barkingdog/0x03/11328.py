n = int(input())

answer = []
for _ in range(n):
    f, s = input().split()
    if len(f) != len(s):
        result = "Impossible"
        answer.append(result)
        continue

    l = [0 for _ in range(26)]
    for a in f:
        l[ord(a) - ord('a')] += 1

    result = "Possible"

    for a in s:
        index = ord(a) - ord('a')
        if l[index] == 0:
            result = "Impossible"
            break
        l[index] -= 1
    answer.append(result)

for a in answer:
    print(a)