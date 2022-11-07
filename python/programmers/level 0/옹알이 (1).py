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