from collections import deque

def make_board():
    board_n = int(input()) + 2
    board_with_wall = [['.' for _ in range(board_n)] for _ in range(board_n)]
    num_of_apple = int(input())
    apple_location = []
    for i in range(num_of_apple):
        y_x_list = input().split()
        for j in range(len(y_x_list)):
            y_x_list[j] = int(y_x_list[j])
        apple_location.append(y_x_list)

    for i in range(board_n):
        for j in range(board_n):
            if i == 0 or i == board_n - 1 or j == 0 or j == board_n - 1:
                board_with_wall[i][j] = '#'
            if [i, j] in apple_location:
                board_with_wall[i][j] = 'A'
    
    return board_with_wall

def move_snake(board):
    num_of_rotate = int(input())
    rotate_list = deque([])
    for i in range(num_of_rotate):
        rotate = input().split()
        for j in range(len(rotate)):
            if j == 0:
                rotate[j] = int(rotate[j])
        rotate_list.append(rotate)

    #   상 우 하 좌
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    snake_location = deque([[1,1]])
    board[1][1] = '#'
    time = 1
    direction = 1

    while True:
        snake_head = snake_location[0][:]
        snake_head[0] += dy[direction]
        snake_head[1] += dx[direction]

        # 이동하려는 곳이 벽이나 몸이면
        if board[snake_head[0]][snake_head[1]] == '#':
            break
        snake_location.appendleft(snake_head)
        # 이동한 곳이 사과가 아니라면
        if board[snake_head[0]][snake_head[1]] != 'A':
            snake_tail = snake_location.pop()
            board[snake_tail[0]][snake_tail[1]] = '.'
        board[snake_head[0]][snake_head[1]] = '#'

        if len(rotate_list) != 0:
            if time == rotate_list[0][0]:
                if rotate_list[0][1] == 'L':
                    if direction == 0:
                        direction = 3
                    else:
                        direction -= 1
                elif rotate_list[0][1] == 'D':
                    if direction == 3:
                        direction = 0
                    else:
                        direction += 1
                rotate_list.popleft()
        
        time += 1

    return time

def main():
    board = make_board()
    end_time = move_snake(board)
    print(end_time)
    return end_time

if __name__ == '__main__':
    main()

# for i in range(len(board)):
#     for j in range(len(board[i])):
#         print(board[i][j], end= '')
#     print()