n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

answer = [1 for _ in range(n)]

for i in range(n-1):
    for j in range(i, n):
        if arr[i][0] > arr[j][0] and arr[i][1] > arr[j][1]:
            answer[j] += 1
        elif arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            answer[i] += 1

for a in answer:
    print(a)