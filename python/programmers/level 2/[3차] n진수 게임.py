def solution(n, t, m, p):
    answer = ''
    num = 0
    stack = []
    order = 1
    i = 0
    while i < t:
        num_copy = num
        while num >= n:
            stack.append(num % n)
            num = num // n
        stack.append(num)
        
        while len(stack) > 0:
            number = stack.pop()
            number = number if number < 10 else chr(number + 55)
            if order == p:
                answer += str(number)
                i += 1
                if i >= t:
                    break
            order = order + 1 if order < m else 1
            
        num_copy += 1
        num = num_copy
        
        
    return answer