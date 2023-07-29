# DFS

n = int(input())

tree = [[] for _ in range(n+1)]
l = [-1 for _ in range(n+1)]
l[1] = 1

for _ in range(n-1):
    f, s = list(map(int, input().split()))
    tree[f].append(s)
    tree[s].append(f)

stack = [(1, tree[1])]
while len(stack) != 0:
    parent, nums = stack.pop()
    for num in nums:
        if l[num] == -1:
            l[num] = parent
            stack.append((num, tree[num]))

for i in range(2, n+1):
    print(l[i])