def count_holl(lock, n):
    result = 0
    for i in range(n):
        for j in range(n):
            if lock[i][j] == 0:
                result += 1
    return result

def make_board(lock, n, m):
    board = [[-1 for _ in range(n + 2*(m-1))] for _ in range(n + 2*(m-1))]
    for i in range(n):
        for j in range(n):
            board[m-1+i][m-1+j] = lock[i][j]
    return board

def rotate_key(key, m):
    rotated = [[] for _ in range(m)]
    for i in range(m):
        for j in range(m):
            rotated[(m-1)-j].append(key[i][j])
    return rotated

def check_unlock(board, keys, n, m, holl):
    unlock = False
    for k in range(4):
        key = keys[k]
        for y in range(n+m-1):
            for x in range(n+m-1):
                cnt = 0
                bp = False
                for i in range(m):
                    for j in range(m):
                        if board[y+i][x+j] == -1:
                            continue
                        if board[y+i][x+j] == 0 and key[i][j] == 1:
                            cnt += 1
                            continue
                        if board[y+i][x+j] == key[i][j]:
                            bp = True
                            break
                    if bp:
                        break
                if cnt == holl and not bp:
                    unlock = True
                    break
            if unlock:
                break
        if unlock:
            break
    return unlock
                

def solution(key, lock):
    answer = False
    m, n = len(key), len(lock)
    holl = count_holl(lock, n)
    board = make_board(lock, n, m)
    keys = [key]
    for i in range(3):
        keys.append(rotate_key(keys[-1], m))
    answer = check_unlock(board, keys, n, m, holl)
    
    return answer