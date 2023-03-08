def solution(numbers):
    answer = ''
    s_nums = []
    for n in numbers:
        s_nums.append(str(n))
    s_nums.sort(key=lambda x:x*4, reverse=True)
    for n in s_nums:
        answer += n
    answer = str(int(answer))
    return answer