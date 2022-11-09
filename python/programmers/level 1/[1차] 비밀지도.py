def solution(n, arr1, arr2):
    answer = []
    bin1 = []
    bin2 = []
    
    for num in arr1:
        result = ''
        b = bin(num)[2:]
        for _ in range(n - len(b)):
            result += '0'
        result += b
        bin1.append(result)
        
    for num in arr2:
        result = ''
        b = bin(num)[2:]
        for _ in range(n - len(b)):
            result += '0'
        result += b
        bin2.append(result)
        
    for i in range(n):
        result = ''
        for j in range(n):
            if bin1[i][j] == '1' or bin2[i][j] == '1':
                result += '#'
            else:
                result += ' '
        answer.append(result)
    return answer