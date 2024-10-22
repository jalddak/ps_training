n = int(input())

arr = set()
for _ in range(n):
    word = input()
    l = len(word)
    arr.add((l, word))
arr = list(arr)
arr.sort(key = lambda x:(x[0], x[1]))

for i in range(len(arr)):
    print(arr[i][1])