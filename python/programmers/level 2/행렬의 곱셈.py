def solution(arr1, arr2):
    arr2_trans = []
    for j in range(len(arr2[0])):
        array = []
        for i in range(len(arr2)):
            array.append(arr2[i][j])
        arr2_trans.append(array)
    
    answer = []
    for i in range(len(arr1)):
        array = []
        for j in range(len(arr2_trans)):
            num = 0
            for k in range(len(arr1[i])):
                num += arr1[i][k] * arr2_trans[j][k]
            array.append(num)
        answer.append(array)
                
    return answer