import heapq

def solution(plans):
    answer = []
    heap = []
    for name, start, playtime in plans:
        start = start.split(":")
        start = int(start[0]) * 60 + int(start[1])
        playtime = int(playtime)
        heapq.heappush(heap, (start, playtime, name))
    
    stops = [list(heapq.heappop(heap))]
    while heap:
        n_info = heapq.heappop(heap)
        while stops:
            c_info = stops[-1]
            if c_info[0] + c_info[1] <= n_info[0]:
                answer.append(c_info[2])
                stops.pop()
                if stops:
                    stops[-1][0] = c_info[0] + c_info[1]
            else:
                c_info[1] -= (n_info[0] - c_info[0])
                break
        stops.append(list(n_info))
    temp = []
    for stop in stops:
        temp.append(stop[2])
    temp.reverse()
    answer += temp
            
        
    return answer