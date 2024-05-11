def solution(n, m, section):
    cover = 0
    answer = 0
    for s in section:
        if cover < s:
            cover = s + m - 1
            answer += 1
    return answer