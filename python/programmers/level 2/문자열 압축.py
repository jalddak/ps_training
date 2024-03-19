def solution(s):
    n = len(s)
    max_part = n // 2 + 1
    answer = n
    
    for i in range(1, max_part):
        arr = [[], 0]
        length = 0
        index = 0
        while index < n:
            temp = s[index:min(index+i, n)]
            if arr[0] == temp:
                arr[1] += 1
            else:
                if arr[1] > 1:
                    length += len(str(arr[1]))
                length += len(arr[0])
                arr[0] = temp
                arr[1] = 1
            index += i
        if arr[1] > 1:
            length += len(str(arr[1]))
        length += len(arr[0])
        answer = min(answer, length)
    return answer