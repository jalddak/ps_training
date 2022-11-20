from collections import deque

def solution(elements):
    sums = []
    elements = deque(elements)
    for i in range(len(elements)):
        for j in range(1, len(elements)+1):
            subset = list(elements)[0:j]
            sums.append(sum(subset))
        elements.append(elements.popleft())
    sums = set(sums)
    return len(sums)