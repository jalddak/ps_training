tcCnt = 10

def recursion(arr, childs, node):
    result = ""
    if len(childs[node]) > 0:
        result += recursion(arr, childs, childs[node][0])
    result += arr[node]
    if len(childs[node]) > 1:
        result += recursion(arr, childs, childs[node][1])
    return result

answer = []
for tc in range(1, tcCnt+1):
    n = int(input())
    arr = ["" for _ in range(n+1)]
    childs = [[] for _ in range(n+1)]

    for _ in range(n):
        info = input().split()
        node = int(info[0])
        arr[node] = info[1]
        for i in range(len(info)-2):
            childs[node].append(int(info[i+2]))
    
    result = recursion(arr, childs, 1)

    sb = "#" + str(tc) + " " + result
    answer.append(sb)

print("\n".join(answer))