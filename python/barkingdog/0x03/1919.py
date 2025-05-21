f = input()
s = input()

fl = [0 for _ in range(26)]
sl = [0 for _ in range(26)]

for a in f:
    fl[ord(a) - ord('a')] += 1

for a in s:
    sl[ord(a) - ord('a')] += 1

answer = 0
for i in range(26):
    answer += abs(fl[i] - sl[i])

print(answer)

