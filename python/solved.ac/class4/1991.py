N = int(input())

tree = {}
for _ in range(N):
    node, left, right = input().split()
    tree[node] = [left, right]

def preorder(node):
    global tree
    print(node, end = "")
    left, right = tree[node]
    if left != ".":
        preorder(left)
    if right != ".":
        preorder(right)
    
def inorder(node):
    global tree
    left, right = tree[node]
    if left != ".":
        inorder(left)
    print(node, end = "")
    if right != ".":
        inorder(right)

def postorder(node):
    global tree
    left, right = tree[node]
    if left != ".":
        postorder(left)
    if right != ".":
        postorder(right)
    print(node, end = "")
    

preorder("A")
print()
inorder("A")
print()
postorder("A")
print()