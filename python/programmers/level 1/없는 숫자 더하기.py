def solution(numbers):
    answer = [0,1,2,3,4,5,6,7,8,9]
    for num in numbers:
        answer.remove(num)
    answer = sum(answer)
    return answer