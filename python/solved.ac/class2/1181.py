N = int(input())
l = [input() for _ in range(N)]

l = list(set(l))
l.sort()
sl = []
for w in l:
    sl.append([len(w), w])
sl.sort()

for l, w in sl:
    print(w)

# N = int(input())

# l = []
# for _ in range(N):
#     word = input()
#     check = 0
#     if word in l:
#         continue
#     for i in range(len(l)):
#         if len(l[i]) > len(word):
#             l.insert(i, word)
#             check = 1
#             break
#         elif len(l[i]) == len(word):
#             for j in range(len(l[i])):
#                 if l[i][j] > word[j]:
#                     l.insert(i, word)
#                     check = 1
#                     break
#                 elif l[i][j] == word[j]:
#                     continue
#                 else:
#                     break
#             if check == 1:
#                 break
#     if check != 1:
#         l.append(word)

# for w in l:
#     print(w)