def solution(n, lost, reserve):
    answer = n - len(lost)
    lost.sort()
    reserve.sort()
    for num in lost:
        if num in reserve:
            answer += 1
            continue
        front = num - 1
        back = num + 1
        if front in reserve and front not in lost:
            reserve.remove(front)
            answer += 1
        elif back in reserve and back not in lost:
            reserve.remove(back)
            answer += 1
    
    return answer