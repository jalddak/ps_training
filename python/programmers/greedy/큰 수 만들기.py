# 테스트케이스 10번이 안풀려서 이전 코드 봤음
# 스택형으로 쌓아서 푸는 방식이 시간복잡도가 더 낮았음
# 내가 시도했던 방법은 문자를 삭제하는 방식으로 해서 삭제할때마다 O(N)의 시간복잡도가 게속 발생해서 시간초과가 난 것같음
# 그리디 문제인데 좀 너무한것같음

def solution(number, k):
    number = list(number)
    
    answer = [number[0]]
    
    i = 1
    while i < len(number):
        while len(answer) > 0 and answer[-1] < number[i] and k > 0:
            k -= 1
            answer.pop()
        answer.append(number[i])
        i += 1
    answer = ''.join(answer)
    if k != 0:
        answer = answer[:-k]
    return answer

################# 내가 시도한 방법 ####################

def solution(number, k):
    answer = ''
    number = list(number)
    i = 0
    while True:
        if i == len(number) - 1:
            break
        if number[i] < number[i+1]:
            del number[i]
            k -= 1
            if i > 0:
                i -= 1
        else:
            i += 1
        if k == 0:
            break
    answer = ''.join(number)
    if k != 0:
        answer = answer[:-k]
    return answer