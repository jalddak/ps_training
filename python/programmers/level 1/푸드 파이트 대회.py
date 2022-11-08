def solution(food):
    answer = ''
    half = []
    for index in range(1,len(food)):
        for _ in range(food[index] // 2):
            half.append(str(index))
    another = reversed(half)
    answer = ''.join(half) + '0' + ''.join(another)
    return answer