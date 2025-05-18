def solution(n, left, right):
    answer = []
    for num in range(left, right+1):
        몫 = (num+1) // n
        나머지 = (num+1) % n
        
        if 나머지 == 0:
            answer.append(n)
        elif 나머지 <= 몫:
            answer.append(1 + 몫)
        else:
            answer.append(나머지)
    return answer

# def solution(n, left, right):
#     answer = []
#     arrays = [[ max(i,j) for j in range(1, n+1)] for i in range(1, n+1)]
#     arr = []
#     for array in arrays:
#         arr += array
#     for index in range(left, right+1):
#         answer.append(arr[index])
#     print(arrays)
#     return answer