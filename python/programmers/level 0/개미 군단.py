def solution(hp):
    장군 = 5
    병정 = 3
    
    answer = 0
    while True:
        if hp >= 장군:
            answer += hp // 장군
            hp -= 장군 * (hp // 장군)
        elif hp >= 병정:
            answer += hp // 병정
            hp -= 병정 * (hp // 병정)
        else:
            break
    answer += hp
    return answer