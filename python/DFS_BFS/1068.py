# DFS

N = int(input())
info = list(map(int, input().split()))
tree = [[] for _ in range(N)]
root = -1
for i in range(N):
    if info[i] != -1:
        tree[info[i]].append(i)
    else:
        root = i

d_num = int(input())

leaf_num = 0
stack = [root]
if root != d_num:
    while len(stack) != 0:
        n = stack.pop()
        check = 0
        if len(tree[n]) == 0:
            leaf_num += 1
            continue
        for node in tree[n]:
            if node != d_num:
                check = 1
                stack.append(node)
        if check == 0:
            leaf_num += 1

print(leaf_num)