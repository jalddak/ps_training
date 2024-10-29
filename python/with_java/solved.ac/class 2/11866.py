n, k = map(int, input().split())

arr = [i for i in range(1, n+1)]
r = k - 1
x = 0
answer = []
while len(arr) > 0:
    x += r
    while x >= len(arr):
        x -= len(arr)
    answer.append(arr.pop(x))

print("<" + ", ".join(map(str, answer)) + ">")