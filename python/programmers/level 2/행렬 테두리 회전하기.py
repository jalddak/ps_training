def solution(rows, columns, queries):
    answer = []
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    board = [[i*columns + j+1 for j in range(columns)] for i in range(rows)]
    for query in queries:
        y1, x1, y2, x2 = map(lambda x:x-1, query)
        y, x = y1, x1
        before = board[y][x]
        result = before
        while x != x2:
            x += 1
            temp = board[y][x]
            board[y][x] = before
            before = temp
            result = min(result, before)
        while y != y2:
            y += 1
            temp = board[y][x]
            board[y][x] = before
            before = temp
            result = min(result, before)
        while x != x1:
            x -= 1
            temp = board[y][x]
            board[y][x] = before
            before = temp
            result = min(result, before)
        while y != y1:
            y -= 1
            temp = board[y][x]
            board[y][x] = before
            before = temp
            result = min(result, before)
        answer.append(result)
        
        
    return answer