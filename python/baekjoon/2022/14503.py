# 이 문제로 배운 점 : 문제 대충 읽지 말자
# 1. 바라보는 방향은 북동남서 순서고, 회전하는 방향은 서쪽이다. 그래서 하나의 변수로 다 커버가 안된다
# 2. 1인 곳은 벽이였다. 난 벽이 아닌줄 알았다 그냥 청소된 곳인 줄 알았다.


def make_board():
    row, col = map(int, input().split())
    board = [[0 for _ in range(col)] for _ in range(row)]
    y, x, direction = map(int, input().split())
    for i in range(row):
        board_row = list(map(int, input().split()))
        for j in range(col):
            board[i][j] = board_row[j]
    return board, y, x, direction


def clean(board, y, x, direction, count):
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]
    if direction % 2 == 1:
        direction += 2
        if direction >= 4:
            direction -= 4
    
    if board[y][x] == 0:
        board[y][x] = 2
        count += 1

    if board[y][x] == 1:
        return count
    
    for i in range(4):
        i += (direction + 1)
        if i >= 4:
            i -= 4
            
        if x+dx[i] < 0 or x+dx[i] > len(board[0])-1 or y+dy[i] < 0 or y+dy[i] > len(board)-1:
            continue
        else:
            if board[y + dy[i]][x + dx[i]] == 0:
                direction_after = i
                if i % 2 == 1:
                    direction_after = i + 2
                    if direction_after >= 4:
                        direction_after -= 4
                count = clean(board, y+dy[i], x+dx[i], direction_after, count)
                break
            else:
                if i == direction:
                    back = i + 2
                    if back >= 4:
                        back -= 4
                    if x+dx[back] < 0 or x+dx[back] > len(board[0])-1 or y+dy[back] < 0 or y+dy[back] > len(board)-1:
                        break
                    else:
                        if direction % 2 == 1:
                            direction += 2
                            if direction >= 4:
                                direction -= 4
                        count = clean(board, y+dy[back], x+dx[back], direction, count)
    return count


def main():
    board, y, x, direction = make_board()
    count = clean(board, y, x, direction, 0)
    print(count)
    return count


if __name__ == '__main__':
    main()