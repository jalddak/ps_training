def solution(babbling):
    able = ["aya", "ye", "woo", "ma"]
    answer = 0
    for b in babbling:
        for a in able:
            start = b.find(a)
            if start != -1:
                b = b[:start] + ' ' + b[start+len(a):]
                b = b.strip()
        if len(b) == 0:
            answer += 1
    return answer

# 문제 다시 읽어보니까 아래처럼 구현하면 replace에서 한단어를 여러번 사용해도 통과하게됨. 그래서 코드 수정함.
# 문제에선 각 단어를 단 한번만 사용가능함.

def solution(babbling):
    able = ["aya", "ye", "woo", "ma"]
    answer = 0
    for b in babbling:
        for a in able:
            b = b.replace(a, ' ')
            b = b.strip()
            if len(b) == 0:
                answer += 1
                break
    return answer