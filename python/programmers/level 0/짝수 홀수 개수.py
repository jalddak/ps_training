def solution(num_list):
    answer = []
    odd = 0
    even = 0
    for num in num_list:
        if num % 2 != 0:
            odd += 1
        else:
            even += 1
    answer = [even, odd]
    return answer