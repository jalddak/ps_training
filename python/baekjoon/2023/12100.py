global result
result = 0

def move(board, len, cnt):
    global result
    if cnt == 5:
        return cnt
    # 위, 아래, 왼, 오
    for d in range(4):
        b_copy = [[0 for _ in range(len)] for _ in range(len)]
        if d == 0:
            for i in range(len):
                list = []
                for j in range(len):
                    list.append(board[j][i])
                for a in range(len):
                    if list[a] != 0:
                        for b in range(a+1, len):
                            if list[b] == 0:
                                continue
                            elif list[a] == list[b]:
                                list[a] *= 2
                                if result < list[a]:
                                    result = list[a]
                                list[b] = 0
                                break
                            else:
                                break
                index = 0
                for a in range(len):
                    if list[a] != 0:
                        b_copy[index][i] = list[a]
                        index += 1
            move(b_copy, len, cnt + 1)
        
        elif d == 1:
            for i in range(len):
                list = []
                for j in range(len):
                    list.append(board[(len-1)-j][i])
                for a in range(len):
                    if list[a] != 0:
                        for b in range(a+1, len):
                            if list[b] == 0:
                                continue
                            elif list[a] == list[b]:
                                list[a] *= 2
                                if result < list[a]:
                                    result = list[a]
                                list[b] = 0
                                break
                            else:
                                break
                index = len-1
                for a in range(len):
                    if list[a] != 0:
                        b_copy[index][i] = list[a]
                        index -= 1
            move(b_copy, len, cnt + 1)

        elif d == 2:
            for i in range(len):
                list = []
                for j in range(len):
                    list.append(board[i][j])
                for a in range(len):
                    if list[a] != 0:
                        for b in range(a+1, len):
                            if list[b] == 0:
                                continue
                            elif list[a] == list[b]:
                                list[a] *= 2
                                if result < list[a]:
                                    result = list[a]
                                list[b] = 0
                                break
                            else:
                                break
                index = 0
                for a in range(len):
                    if list[a] != 0:
                        b_copy[i][index] = list[a]
                        index += 1
            move(b_copy, len, cnt + 1)

        elif d == 3:
            for i in range(len):
                list = []
                for j in range(len):
                    list.append(board[i][(len-1)-j])
                for a in range(len):
                    if list[a] != 0:
                        for b in range(a+1, len):
                            if list[b] == 0:
                                continue
                            elif list[a] == list[b]:
                                list[a] *= 2
                                if result < list[a]:
                                    result = list[a]
                                list[b] = 0
                                break
                            else:
                                break
                index = len-1
                for a in range(len):
                    if list[a] != 0:
                        b_copy[i][index] = list[a]
                        index -= 1
            move(b_copy, len, cnt + 1)


def main():
    len = int(input())
    board = []
    global result
    for i in range(len):
        board.append(list(map(int, input().split())))
        max_num = max(board[i])
        if result < max_num:
            result = max_num
    move(board, len, 0)
    return result

if __name__ == '__main__':
    main()
    print(result)