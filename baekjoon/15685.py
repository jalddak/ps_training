# 이 문제로 배운 점: 어떤 점을 한 꼭지점을 기준으로 90도 회전 시켰을 때의 점의 위치
# 참고 사이트: http://godingmath.com/rotation90

from collections import deque

def draw_dragon_curve(board, x, y, d, g, index):
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    locations = deque([(x + dx[d], y + dy[d]), (x,y)])
    board[y][x] = index
    board[y+dy[d]][x+dx[d]] = index
    for i in range(g):
        standard = locations[0]
        increase = 0
        for j in range(1, len(locations)):
            j += increase
            after_minus = (locations[j][0] - standard[0], locations[j][1] - standard[1])
            after_rotate = (-after_minus[1] + standard[0] , after_minus[0] + standard[1])
            locations.appendleft(after_rotate)
            increase += 1
            board[after_rotate[1]][after_rotate[0]] = index

def check_square(board):
    square = 0
    for i in range(len(board) - 1):
        for j in range(len(board[i]) - 1):
            if board[i][j] != 0 and board[i+1][j] != 0 and board[i][j+1] != 0 and board[i+1][j+1] != 0:
                square += 1
    return square


def main():
    board = [[0 for _ in range(101)] for _ in range(101)]
    num = int(input())
    for i in range(num):
        x, y, d, g = map(int, input().split())
        draw_dragon_curve(board, x, y, d, g, i+1)
    square_count = check_square(board)
    print(square_count)
    return square_count


if __name__ == '__main__':
    main()