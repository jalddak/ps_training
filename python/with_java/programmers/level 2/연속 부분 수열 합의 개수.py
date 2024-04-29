from collections import deque

def solution(elements):
    sums = set(elements)
    for _ in range(len(elements)):
        for l in range(2, len(elements)):
            sums.add(sum(elements[0:l]))
        
        elements = deque(elements)
        elements.append(elements.popleft())
        elements = list(elements)
    
    return len(sums)+1