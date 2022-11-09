def solution(board, moves):
    answer = 0
    바구니 = []
    depth = len(board)
    for move in moves:
        col = move - 1
        for i in range(depth):
            if board[i][col] != 0:
                doll = board[i][col]
                board[i][col] = 0
                if len(바구니) > 0:
                    if 바구니[-1] == doll:
                        바구니.pop()
                        answer += 2
                    else:
                        바구니.append(doll)
                else:
                    바구니.append(doll)
                        
                break
                
                        
        
    return answer