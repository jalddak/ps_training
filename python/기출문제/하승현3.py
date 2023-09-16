def main(r, c):
    result = [[0 for _ in range(c)] for _ in range(r)]

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    cnt = 1
    infi = 2
    direct = 3
    stack = []
    stack.append([0, c-1])
    
    while len(stack) != 0:
        y, x = stack.pop()
        result[y][x] = cnt
        cnt += 1
        ny = y + dy[direct]
        nx = x + dx[direct]
        if 0 <= ny < r and 0 <= nx < c and result[ny][nx] == 0:
            stack.append([ny, nx])
        elif infi > 0:
            infi -= 1
            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]
                if 0 <= ny < r and 0 <= nx < c and result[ny][nx] == 0:
                    stack.append([ny, nx])
                    direct = d
        else:
            infi = 2
            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]
                if 0 <= ny < r and 0 <= nx < c and result[ny][nx] == 0:
                    result[ny][nx] = cnt
                    cnt += 1
                    for d2 in range(4):
                        nny = ny + dy[d2]
                        nnx = nx + dx[d2]
                        if d != d2 and 0 <= nny < r and 0 <= nnx < c and result[nny][nnx] == 0:
                            stack.append([nny, nnx])
                            direct = d2

    print(result)
    return result

main(5, 4)
main(3, 5)
