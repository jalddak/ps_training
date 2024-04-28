def solution(brown, yellow):
    answer = []
    for c in range(1, int(yellow ** 0.5)+1):
        if yellow % c != 0:
            continue
        r = yellow // c
        if r*2 + c*2 + 4 == brown:
            answer = [r+2, c+2]
            break
    return answer