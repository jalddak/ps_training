def main():
    str1 = input()
    str2 = input()

    len1 = len(str1)
    len2 = len(str2)

    board = [["" for _ in range(len2 + 1)] for _ in range(len1 + 1)]

    for i in range(len1):
        for j in range(len2):
            if str1[i] == str2[j]:
                board[i+1][j+1] = board[i][j] + str1[i]
            else:
                board[i+1][j+1] = board[i+1][j] if len(board[i+1][j]) > len(board[i][j+1]) else board[i][j+1]

    print(len(board[len1][len2]))
    print(board[len1][len2])

if __name__ == "__main__":
    main()