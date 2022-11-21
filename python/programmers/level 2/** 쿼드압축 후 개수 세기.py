def solution(arr):
    length = len(arr)
    answer = [0, 0]
    answer = recursion(0, 0, length, arr, answer)
    return answer

def recursion(y, x, length, arr, answer):
    init = arr[y][x]
    stop = False
    for i in range(y, y+length):
        for j in range(x, x+length):
            if arr[i][j] != init:
                length //= 2
                answer = recursion(y, x, length, arr, answer)
                answer = recursion(y + length, x, length, arr, answer)
                answer = recursion(y, x + length, length, arr, answer)
                answer = recursion(y + length, x + length, length, arr, answer)
                stop = True
                break
        if stop:
            answer[init] -= 1
            break
    answer[init] += 1
    return answer