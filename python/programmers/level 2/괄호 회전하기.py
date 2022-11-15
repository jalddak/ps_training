from collections import deque

def solution(s):
    answer = 0
    
    s = deque(s)
    
    for _ in range(len(s)):
        s.append(s.popleft())
        stack = []
        for letter in s:
            if letter in ['[', '{', '(']:
                stack.append(letter)
            elif len(stack) > 0:
                if letter == ']' and stack[-1] == '[':
                    stack.pop()
                elif letter == '}' and stack[-1] == '{':
                    stack.pop()
                elif letter == ')' and stack[-1] == '(':
                    stack.pop()
                else:
                    answer -= 1
                    stack = []
                    break
            else:
                answer -= 1
                stack = []
                break
                
        if len(stack) != 0:
            answer -= 1
            
        answer += 1
        
    
    return answer