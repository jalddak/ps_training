import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

# 시간초과 -> stack으로 해결.
# 한번 오른쪽 자식 가진 노드들은 더 이상 오른쪽 자식을 못가지니 신경쓰지 않기 (다음 오른쪽 자식을 누구로 정할지 체크하는 짓을 안해도됨)
# 기존 코드는 현재 입력받기 바로 직전에 입력받은 노드의 위치부터 쭉 부모노드 타고 while문을 돌아서 오른쪽 자식이 있던 노드들까지 확인하고 maxN을 갱신한다.
n = int(input())

tree = {n : [0, 0, 0]}
root = n
stack = [root]

def postOrder(node):
    for i in range(1, 3):
        if tree[node][i] == 0:
            continue
        postOrder(tree[node][i])
    print(node)

while True:
    try:
        c = int(input())
        n = stack[-1]
        if c < n:
            tree[n][1] = c
        else:
            while stack and c > stack[-1]:
                n = stack.pop()
            tree[n][2] = c

        tree[c] = [n, 0, 0]
        stack.append(c)

    except:
        break

postOrder(root)