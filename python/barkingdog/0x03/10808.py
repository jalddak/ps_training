s = input()

answer = [0 for _ in range(26)]
for a in s:
    answer[ord(a) - ord('a')] += 1

print(*answer)