def solution(s):
    p = 0
    y = 0
    for letter in s:
        if letter.lower() == 'p':
            p += 1
        elif letter.lower() == 'y':
            y += 1
    if p == y:
        return True
    else:
        return False