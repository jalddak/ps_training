def solution(n, stations, w):
    answer = 0

    head = stations[0]-1-w
    tail = n-stations[-1]-w
    length = 2*w+1
    if head > 0:
        answer += head // length
        answer += 1 if head % length != 0 else 0
    if tail > 0:
        answer += tail // length
        answer += 1 if tail % length != 0 else 0
    for i in range(len(stations)-1):
        need = stations[i+1]-stations[i]-1-2*w
        if need > 0:
            answer += need // length
            answer += 1 if need % length != 0 else 0
        
    
    return answer