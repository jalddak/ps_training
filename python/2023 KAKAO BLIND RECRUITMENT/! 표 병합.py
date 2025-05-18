def solution(commands):
    answer = []
    board = [[[] for _ in range(50)] for _ in range(50)]
    value_dict = {}
    
    for command in commands:
        command = command.split()
        print(command)
        
        if command[0] == 'UPDATE':
            if len(command) == 4:
                r, c, value = int(command[1])-1, int(command[2])-1, command[3]
                
                if len(board[r][c]) == 1:
                    r, c = board[r][c][0]
                
                if len(board[r][c]) == 2:
                    if board[r][c][0] != '':
                        value_dict[board[r][c][0]].remove((r, c))
                    board[r][c][0] = value

                elif len(board[r][c]) == 0:
                    board[r][c] = [value, []]
                
                if value not in value_dict:
                    value_dict[value] = [(r, c)]
                else:
                    value_dict[value].append((r, c))
                    
            elif len(command) == 3:
                value1, value2 = command[1], command[2]
                value_dict[value2] = value_dict.pop(value1)
                for (r, c) in value_dict[value2]:
                    board[r][c][0] = value2
                
        elif command[0] == 'MERGE':
            r1, c1, r2, c2 = int(command[1])-1, int(command[2])-1, int(command[3])-1, int(command[4])-1
            if r1 == r2 and c1 == c2:
                continue

            mr, mc = r1, c1
            sr, sc = r2, c2
            if len(board[r1][c1]) != 0 and len(board[r2][c2]) != 0:
                if len(board[r1][c1]) == 1 and len(board[r2][c2]) == 1 and board[r1][c1][0] == board[r2][c2][0]:
                    continue
                elif len(board[r1][c1]) == 1 and board[r1][c1][0] == (r2, c2):
                    continue
                elif len(board[r2][c2]) == 1 and board[r2][c2][0] == (r1, c1):
                    continue
            
            elif len(board[r1][c1]) == 0 and len(board[r2][c2]) != 0:
                mr, mc = r2, c2
                sr, sc = r1, c1

            if len(board[mr][mc]) == 0:
                board[mr][mc] = ['', []]
            elif len(board[mr][mc]) == 1:
                mr, mc = board[mr][mc][0]
            
            if len(board[sr][sc]) != 0:
                if len(board[sr][sc]) == 1:
                    sr, sc = board[sr][sc][0]
                for (r, c) in board[sr][sc][1]:
                    board[r][c][0] = (mr, mc)
                    board[mr][mc][1].append((r, c))
                if board[sr][sc][0] != '':
                    value_dict[board[sr][sc][0]].remove((sr, sc))

            board[sr][sc] = [(mr, mc)]
            board[mr][mc][1].append((sr, sc))
            
        elif command[0] == 'UNMERGE':
            r, c = int(command[1])-1, int(command[2])-1
            value = ''
            if len(board[r][c]) == 2:
                value = board[r][c][0]
                dr, dc = r, c
            elif len(board[r][c]) == 1:
                pr, pc = board[r][c][0]
                value = board[pr][pc][0]
                dr, dc = pr, pc
            else:
                continue
            
            for (cr, cc) in board[dr][dc][1]:
                board[cr][cc] = []
            board[dr][dc] = []
            
            board[r][c] = [value, []]


        elif command[0] == 'PRINT':
            r, c = int(command[1])-1, int(command[2])-1
            if len(board[r][c]) == 0:
                answer.append("EMPTY")
            elif len(board[r][c]) == 1:
                pr, pc = board[r][c][0]
                answer.append(board[pr][pc][0])
            elif board[r][c][0] != '':
                answer.append(board[r][c][0])
            else:
                answer.append("EMPTY")
        
        for i in range(4):
            print(board[i][:5])
        print()
        print(value_dict)
        print('-----------------')
    return answer

# print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))
# print(solution(["UPDATE 1 1 menu", "MERGE 1 1 1 2", "MERGE 1 1 1 3", "MERGE 1 1 1 4", "MERGE 1 2 1 3", "UPDATE 1 1 hansik", "PRINT 1 1", "PRINT 1 2", "PRINT 1 3", "PRINT 1 4"]))
# print(solution(["UPDATE 1 1 A", "UPDATE 2 2 B", "UPDATE 3 3 C", "UPDATE 4 4 D", "MERGE 1 1 2 2", "MERGE 3 3 4 4", "MERGE 1 1 4 4", "UNMERGE 3 3", "PRINT 1 1", "PRINT 2 2", "PRINT 3 3", "PRINT 4 4"]))
# print(solution(["MERGE 1 1 2 2", "UPDATE 1 1 A", "UNMERGE 1 1", "PRINT 1 1","PRINT 2 2"]))
print(solution(["MERGE 1 1 1 2", "MERGE 1 1 1 3", "UNMERGE 1 2"]))