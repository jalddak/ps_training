N = int(input())
default = ["" for _ in range(8)]

words = []
for _ in range(N):
    word = list(input())
    length = len(word)
    word = default + word
    word = word[length:]
    word.reverse()
    words.append(word)

score = {}
for i in range(8):
    for word in words:
        if word[i] == "":
            continue
        if word[i] not in score:
            score[word[i]] = 10 ** i
        else:
            score[word[i]] += 10 ** i

rank = list(score.items())
rank.sort(key=lambda x:x[1], reverse=True)

num = 9
info = {}
for r in rank:
    info[r[0]] = num
    num -= 1

for i in range(len(words)):
    word = words[i]
    for j in range(8):
        if word[j] == "":
            continue
        word[j] = str(info[word[j]])
    word.reverse()
    words[i] = "".join(word)

words = sum(map(int, words))
print(words)