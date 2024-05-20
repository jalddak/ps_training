N = int(input())

temp = ['' for _ in range(8)]
words = []

for _ in range(N):
    word = list(input())
    length = len(word)
    word = (temp + word)[length:]
    word.reverse()
    words.append(word)

d = {}
for word in words:
    for i in range(len(word)):
        c = word[i]
        if c == '':
            break
        d[c] = d.get(c, 0) + 10 ** i

info = list(d.values())
info.sort(reverse=True)

n = 9
answer = 0
for num in info:
    answer += num * n
    n -= 1

print(answer)