def solution(sizes):
    answer = 0
    min_big = 0
    max_big = 0
    for s in sizes:
        if s[0] < s[1]:
            if min_big < s[0]:
                min_big = s[0]
            if max_big < s[1]:
                max_big = s[1]
        else:
            if min_big < s[1]:
                min_big = s[1]
            if max_big < s[0]:
                max_big = s[0]
    answer = min_big * max_big

    return answer