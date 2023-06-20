def solution(commands):
    answer = []
    board = [["EMPTY" for _ in range(50)] for _ in range(50)]
    merge = [[[] for _ in range(50)] for _ in range(50)]
    
    for command in commands:
        command = command.split()
        
        if command[0] == 'UPDATE':
            if len(command) == 4:
                r, c, value = int(command[1])-1, int(command[2])-1, command[3]
                board[r][c] = value
                for (mr, mc) in merge[r][c]:
                    board[mr][mc] = value
                    
            elif len(command) == 3:
                value1, value2 = command[1], command[2]
                for i in range(50):
                    for j in range(50):
                        if board[i][j] == value1:
                            board[i][j] = value2
                

        elif command[0] == 'MERGE':
            r1, c1, r2, c2 = int(command[1])-1, int(command[2])-1, int(command[3])-1, int(command[4])-1
            if (r1, c1) == (r2, c2):
                continue
            elif (r1, c1) in merge[r2][c2]:
                continue

            mr, mc = r1, c1
            sr, sc = r2, c2
            if board[r1][c1] == "EMPTY" and board[r2][c2] != "EMPTY":
                mr, mc = r2, c2
                sr, sc = r1, c1
            
            for (r, c) in merge[sr][sc]:
                board[r][c] = board[mr][mc]
                merge[r][c] += merge[mr][mc]
                merge[r][c] += [(mr, mc)]
            
            for (r, c) in merge[mr][mc]:
                merge[r][c] += merge[sr][sc]
                merge[r][c] += [(sr, sc)]
            
            board[sr][sc] = board[mr][mc]
            copy = merge[mr][mc][:]
            merge[mr][mc] += merge[sr][sc] + [(sr, sc)]
            merge[sr][sc] += copy + [(mr, mc)]

            
        elif command[0] == 'UNMERGE':
            r, c = int(command[1])-1, int(command[2])-1
            for (dr, dc) in merge[r][c]:
                board[dr][dc] = "EMPTY"
                merge[dr][dc] = []
            merge[r][c] = []


        elif command[0] == 'PRINT':
            r, c = int(command[1])-1, int(command[2])-1
            answer.append(board[r][c])
        
    return answer

print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))
# print(solution(["UPDATE 1 1 menu", "MERGE 1 1 1 2", "MERGE 1 1 1 3", "MERGE 1 1 1 4", "MERGE 1 2 1 3", "UPDATE 1 1 hansik", "PRINT 1 1", "PRINT 1 2", "PRINT 1 3", "PRINT 1 4"]))
# print(solution(["UPDATE 1 1 A", "UPDATE 2 2 B", "UPDATE 3 3 C", "UPDATE 4 4 D", "MERGE 1 1 2 2", "MERGE 3 3 4 4", "MERGE 1 1 4 4", "UNMERGE 3 3", "PRINT 1 1", "PRINT 2 2", "PRINT 3 3", "PRINT 4 4"]))
# print(solution(["MERGE 1 1 2 2", "UPDATE 1 1 A", "UNMERGE 1 1", "PRINT 1 1","PRINT 2 2"]))
# print(solution(["MERGE 1 1 1 2", "MERGE 1 1 1 3", "UNMERGE 1 2"]))