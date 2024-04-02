# linked List 까지는 알았는데, 파이썬에서 Node 구현하는 법 찾아봄

class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

def solution(n, k, cmd):
    answer = ['O' for _ in range(n)]
    node = Node(0)
    current = None
    for i in range(n):
        node.next = Node(i)
        temp = node
        node = node.next
        node.prev = temp
        if i == k:
            current = node
        
    deletes = []
    for command in cmd:
        if command[0] in ['U', 'D']:
            command = command.split()
            jump = int(command[1])
            for _ in range(jump):
                if command[0] == 'U':
                    current = current.prev
                elif command[0] == 'D':
                    current = current.next
            continue
        if command[0] == 'C':
            deletes.append(current)
            
            if current.prev != None:
                current.prev.next = current.next
            if current.next != None:
                current.next.prev = current.prev
                current = current.next
            else:
                current = current.prev
            continue
            
        if command[0] == 'Z':
            restore = deletes.pop()
            
            if restore.prev != None:
                restore.prev.next = restore
            if restore.next != None:
                restore.next.prev = restore
            continue
    
    for delete in deletes:
        answer[delete.data] = 'X'
    
    return "".join(answer)

class Node:
    def __init__(self, data, prev, next):
        self.delete = False
        self.data = data
        self.prev = prev
        self.next = next

def solution(n, k, cmd):
    answer = []
    table = [Node(i, i-1, i+1) for i in range(n)]
    table[0].prev = None
    table[n-1].next = None
    current = table[k]
    deletes = []
    for command in cmd:
        if command[0] in ['U', 'D']:
            command = command.split()
            jump = int(command[1])
            for _ in range(jump):
                if command[0] == 'U':
                    current = table[current.prev]
                elif command[0] == 'D':
                    current = table[current.next]
            continue
        if command[0] == 'C':
            current.delete = True
            deletes.append(current)
            
            if current.prev != None:
                table[current.prev].next = current.next
            if current.next != None:
                table[current.next].prev = current.prev
                current = table[current.next]
            else:
                current = table[current.prev]
            continue
            
        if command[0] == 'Z':
            restore = deletes.pop()
            restore.delete = False
            if restore.prev != None:
                table[restore.prev].next = restore.data
            if restore.next != None:
                table[restore.next].prev = restore.data
            continue
    
    for node in table:
        if not node.delete:
            answer.append('O')
        else:
            answer.append('X')
    
    return "".join(answer)