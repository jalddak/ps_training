from collections import deque

def solution(A, B):
    if A == B:
        return 0
    
    A = deque(A)
    
    for result in range(len(A)):
        A.appendleft(A.pop())
        if ''.join(A) == B:
            return result + 1
    return -1