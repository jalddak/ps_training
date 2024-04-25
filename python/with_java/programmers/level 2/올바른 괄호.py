def solution(s):
    flag = []
    for c in s:
        if c == '(':
            flag.append(1);
        elif c == ')':
            if not flag:
                return False
            flag.pop();
    if flag:
        return False
    return True