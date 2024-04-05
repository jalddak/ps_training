import sys
sys.setrecursionlimit(10 ** 7)

class Node:
    def __init__(self, index, data, left=None, right=None):
        self.index = index
        self.data = data
        self.left = left
        self.right = right

def insert_node(parent, node):
    if node.data < parent.data:
        if parent.left != None:
            insert_node(parent.left, node)
        else:
            parent.left = node
    elif node.data > parent.data:
        if parent.right != None:
            insert_node(parent.right, node)
        else:
            parent.right = node

def preorder(node, result):
    result.append(node.index)
    if node.left != None:
        preorder(node.left, result)
    if node.right != None:
        preorder(node.right, result)

def postorder(node, result):
    if node.left != None:
        postorder(node.left, result)
    if node.right != None:
        postorder(node.right, result)
    result.append(node.index)
        
def make_tree(root, nodeinfo):
    for i in range(len(nodeinfo)):
        nx, ny, ni = nodeinfo[i]
        node = Node(ni, nx)
        insert_node(root, node)
        
        
def solution(nodeinfo):
    for i in range(len(nodeinfo)):
        num = i+1
        nodeinfo[i].append(num)
    nodeinfo.sort(key=lambda x:(-x[1], x[0]))
    
    rx, ry, ri = nodeinfo[0]
    root = Node(ri, rx)
    make_tree(root, nodeinfo)
    
    answer = []
    pre_result = []
    preorder(root, pre_result)
    post_result = []
    postorder(root, post_result)
    answer.append(pre_result)
    answer.append(post_result)
    
    return answer