from collections import deque

number = '4177252841'
k = 4

def solution(number, k):
    answer = ''
    str_num = deque()
    for num in number:
        str_num.append(num)
    index = 0
    print(str_num)
    while k != 0 and index < len(str_num):
        if int(str_num[0]) < int(str_num[1]):
            str_num.popleft()
            k -= 1
            if index == 0:
                index -= 1
                str_num.rotate()
            else:
                index -= 2
                str_num.rotate()
                str_num.rotate()
        index += 1
        str_num.rotate(-1)
        if k != 0 and index == len(str_num)-1:
            index = 0
            str_num.rotate(-1)
            while k != 0:
                str_num.pop()
                k -= 1
            break
    while index != 0:
        str_num.rotate()
        index -= 1
    for num in str_num:
        answer += num
    print(answer)
    return answer

solution(number, k)

# 다른 사람 코드 보면서 느낀점
def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        # 숫자로만 된 스트링은 그냥 하나로 나와도 숫자처럼 크기 계산이 가능하구나
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        # 이런식으로 한번에 남은자리 잘라버릴수가 있구나
        stack = stack[:-k]
    # join 으로 리스트를 스트링으로 합성이 가능하구나.
    return ''.join(stack)