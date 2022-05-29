# 이문제로 배운 점: 백준은 넘파이 사용하면 안된다.

def move(board, big, n, count):
    if count == 5:
        max_num = 0
        for i in range(n):
            for j in range(n):
                if board[i][j] > max_num:
                    max_num = board[i][j]
        return max_num
    count += 1
    big_list = []
        
    # 0 = up, 1 = down, 2 = left, 3 = right
    for direction in range(4):
        board_copy = []
        for i in range(n):
            board_copy.append(board[i][:])
        if direction == 0:
            for j in range(n):
                already = []
                for i in range(1, n):
                    while board_copy[i-1][j] == 0:
                        num = board_copy[i][j]
                        board_copy[i-1][j] = num
                        board_copy[i][j] = 0
                        i -= 1
                        if i == 0:
                            break
                    if i != 0 and board_copy[i-1][j] == board_copy[i][j]:
                        if i not in already:
                            board_copy[i-1][j] *= 2
                            board_copy[i][j] = 0
                            already.append(i)
            big_list.append(move(board_copy, big, n, count))
        
        elif direction == 1:
            for j in range(n):
                already = []
                for i in range(n-1, 0, -1):
                    while board_copy[i][j] == 0:
                        num = board_copy[i-1][j]
                        board_copy[i][j] = num
                        board_copy[i-1][j] = 0
                        i += 1
                        if i == n:
                            break
                    if i != n and board_copy[i][j] == board_copy[i-1][j]:
                        if i not in already:
                            board_copy[i][j] *= 2
                            board_copy[i-1][j] = 0
                            already.append(i)
            big_list.append(move(board_copy, big, n, count))
        
        elif direction == 2:
            for i in range(n):
                already = []
                for j in range(1, n):
                    while board_copy[i][j-1] == 0:
                        num = board_copy[i][j]
                        board_copy[i][j-1] = num
                        board_copy[i][j] = 0
                        j -= 1
                        if j == 0:
                            break
                    if j != 0 and board_copy[i][j-1] == board_copy[i][j]:
                        if j not in already:
                            board_copy[i][j-1] *= 2
                            board_copy[i][j] = 0
                            already.append(j)
            big_list.append(move(board_copy, big, n, count))
        
        elif direction == 3:
            for i in range(n):
                already = []
                for j in range(n-1, 0, -1):
                    while board_copy[i][j] == 0:
                        num = board_copy[i][j-1]
                        board_copy[i][j] = num
                        board_copy[i][j-1] = 0
                        j += 1
                        if j == n:
                            break
                    if j != n and board_copy[i][j] == board_copy[i][j-1]:
                        if j not in already:
                            board_copy[i][j] *= 2
                            board_copy[i][j-1] = 0
                            already.append(j)
            big_list.append(move(board_copy, big, n, count))
    
    return max(big_list)



def main():
    n = int(input())
    board = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        num = input().split()
        for j in range(n):
            board[i][j] = int(num[j])

    big = move(board, 0, n, 0)
    print(big)
    return big

if __name__ == '__main__':
    main()

# 넘파이 사용 코드
# import numpy as np

# def move(board, big, n, count):
#     count += 1
#     if count == 5:
#         board = board.reshape(n*n)
#         max_index = np.argmax(board)
#         return board[max_index]
    
#     big_list = []

#     # 0 = up, 1 = down, 2 = left, 3 = right
#     for direction in range(4):
#         board_copy = board.copy()

#         if direction == 0:
#             for i in range(1, n):
#                 for j in range(n):
#                     if board_copy[i-1][j] == board_copy[i][j]:
#                         board_copy[i-1][j] *= 2
#                         board_copy[i][j] = 0
#             for j in range(n):
#                 for i in range(1, n):
#                     while board_copy[i-1][j] == 0:
#                         num = board_copy[i][j]
#                         board_copy[i-1][j] = num
#                         board_copy[i][j] = 0
#                         i -= 1
#                         if i == 0:
#                             break
#             big_list.append(move(board_copy, big, n, count))
        
#         elif direction == 1:
#             for i in range(n-1, 0, -1):
#                 for j in range(n):
#                     if board_copy[i][j] == board_copy[i-1][j]:
#                         board_copy[i][j] *= 2
#                         board_copy[i-1][j] = 0
#             for j in range(n):
#                 for i in range(n-1, 0, -1):
#                     while board_copy[i][j] == 0:
#                         num = board_copy[i-1][j]
#                         board_copy[i][j] = num
#                         board_copy[i-1][j] = 0
#                         i += 1
#                         if i == n:
#                             break
#             big_list.append(move(board_copy, big, n, count))
        
#         elif direction == 2:
#             for j in range(1, n):
#                 for i in range(n):
#                     if board_copy[i][j-1] == board_copy[i][j]:
#                         board_copy[i][j-1] *= 2
#                         board_copy[i][j] = 0
#             for i in range(n):
#                 for j in range(1, n):
#                     while board_copy[i][j-1] == 0:
#                         num = board_copy[i][j]
#                         board_copy[i][j-1] = num
#                         board_copy[i][j] = 0
#                         j -= 1
#                         if j == 0:
#                             break
#             big_list.append(move(board_copy, big, n, count))
        
#         elif direction == 3:
#             for j in range(n-1, 0, -1):
#                 for i in range(n):
#                     if board_copy[i][j] == board_copy[i][j-1]:
#                         board_copy[i][j] *= 2
#                         board_copy[i][j-1] = 0
#             for i in range(n):
#                 for j in range(n-1, 0, -1):
#                     while board_copy[i][j] == 0:
#                         num = board_copy[i][j-1]
#                         board_copy[i][j] = num
#                         board_copy[i][j-1] = 0
#                         j += 1
#                         if j == n:
#                             break
#             big_list.append(move(board_copy, big, n, count))
    
#     return max(big_list)



# def main():
#     n = int(input())
#     board = []
#     for i in range(n):
#         num = input().split()
#         for j in range(n):
#             board.append(int(num[j]))
#     board = np.array(board)
#     board = board.reshape(n, n)

#     big = move(board, 0, n, 0)
#     print(big)
#     return big
    
#     for i in range(len(board)):
#         for j in range(len(board[i])):
#             print(board[i][j], end=' ')
#         print()

# if __name__ == '__main__':
#     main()

# 보드 모양 확인 코드
# for i in range(len(board)):
#     for j in range(len(board[i])):
#         print(board[i][j], end=' ')
#     print()
