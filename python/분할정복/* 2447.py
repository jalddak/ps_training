N = int(input())

def recursion(n):
    if n == 1:
        return '*'
    
    small = recursion(n//3)
    new = []
    for pattern in small:
        new.append(pattern * 3)
    for pattern in small:
        new.append(pattern + ' ' * len(pattern) + pattern)
    for pattern in small:
        new.append(pattern * 3)
    
    return new

board = recursion(N)
for i in range(N):
    print("".join(board[i]))