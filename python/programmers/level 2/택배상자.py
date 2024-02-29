def solution(order):
    answer = 0
    belt = [n for n in range(1, len(order)+1)]
    belt.reverse()
    
    stack = []
    for n in order:
        while belt and belt[-1] <= n:
            stack.append(belt.pop())
        if stack and stack[-1] != n:
            break
        stack.pop()
        answer += 1
        
    return answer