def solution(n, times):
    answer = 0
    min_t = 0
    max_t = max(times) * n
    while min_t <= max_t:
        able = 0
        mid_t = (min_t + max_t) // 2
        for t in times:
            able += mid_t // t
            if able >= n:
                break
        if able < n:
            min_t = mid_t + 1
        elif able >= n:
            answer = mid_t
            max_t = mid_t - 1
    return answer