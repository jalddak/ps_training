def solution(num_list, n):
    answer = []
    index = 0
    while index < len(num_list):
        result = []
        for _ in range(n):
            result.append(num_list[index])
            index += 1
        answer.append(result)
    return answer