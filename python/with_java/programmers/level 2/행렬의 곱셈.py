def solution(arr1, arr2):
    row_len = len(arr1)
    col_len = len(arr2[0])
    mix = len(arr2)
    answer = []
    for i in range(row_len):
        row = []
        for j in range(col_len):
            result = 0
            for k in range(mix):
                result += arr1[i][k] * arr2[k][j]
            row.append(result)
        answer.append(row)
    return answer