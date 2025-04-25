def main():
    board = [list(map(int, list(input()))) for _ in range(9)]

    rowCheck = list(map(set, board))
    colCheck = []
    blockCheck = [set() for _ in range(9)]
    blanks = []

    for i in range(9):
        temp = set()
        for j in range(9):
            temp.add(board[j][i])
            if board[i][j] == 0:
                blanks.append((i, j))
        colCheck.append(temp)
    blanks.reverse()

    for i in range(9):
        for j in range(9):
            index = i // 3 * 3 + j // 3
            blockCheck[index].add(board[i][j])
    
    backTracking(board, rowCheck, colCheck, blockCheck, blanks)

    for i in range(9):
        print("".join(map(str, board[i])))

def backTracking(board, rowCheck, colCheck, blockCheck, blanks):

    result = False

    if not blanks:
        return True
    
    y, x = blanks.pop()
    blockIndex = y // 3 * 3 + x // 3
    for num in range(1, 10):
        if num in rowCheck[y] or num in colCheck[x] or num in blockCheck[blockIndex]:
            continue
        
        rowCheck[y].add(num)
        colCheck[x].add(num)
        blockCheck[blockIndex].add(num)

        board[y][x] = num
        result = backTracking(board, rowCheck, colCheck, blockCheck, blanks)

        rowCheck[y].remove(num)
        colCheck[x].remove(num)
        blockCheck[blockIndex].remove(num)
        if result:
            break

    blanks.append((y, x))
    return result

if __name__ == '__main__':
    main()