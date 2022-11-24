from itertools import permutations

def solution(expression):
    num_stack = []
    op_stack = []
    num = ''
    for letter in expression:
        if letter.isdigit():
            num += letter
        else:
            num_stack.append(int(num))
            num = ''
            op_stack.append(letter)
    num_stack.append(int(num))
    
    op_types = list(set(op_stack))
    pers = list(permutations(op_types, len(op_types)))
    
    answer = 0
    for per in pers:
        op_copy = op_stack[:]
        num_copy = num_stack[:]
        
        for op in per:
            i = 0
            while i < len(op_copy):
                if op_copy[i] == op:
                    if op == '*':
                        num_copy[i] *= num_copy[i+1]
                    elif op == '+':
                        num_copy[i] += num_copy[i+1]
                    else:
                        num_copy[i] -= num_copy[i+1]
                    del num_copy[i+1]
                    del op_copy[i]
                    i -= 1
                i += 1
        candidate = abs(num_copy[0])
        if answer < candidate:
            answer = candidate
    
    return answer