from collections import deque

def solution(operations):
    answer = []
    operations = deque(operations)
    queue = []
    while len(operations) != 0:
        command = operations.popleft()
        if command[0] == 'I':
            num = int(command[2:])
            queue.append(num)
            queue.sort()
        elif command[0] == 'D':
            if int(command[2:]) == 1:
                if len(queue) != 0:
                    queue.pop()
                else:
                    continue
            elif int(command[2:]) == -1:
                if len(queue) != 0:
                    queue.pop(0)
                else:
                    continue
    if len(queue) != 0:
        answer.append(queue[len(queue)-1])
        answer.append(queue[0])
    else:
        answer = [0,0]
    return answer