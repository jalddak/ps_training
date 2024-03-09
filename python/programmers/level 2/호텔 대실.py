import heapq

def solution(book_time):
    answer = 0
    heap = []
    for s, e in book_time:
        s = s.split(':')
        e = e.split(':')
        s = list(map(int, s))
        e = list(map(int, e))
        s = s[0] * 60 + s[1]
        e = e[0] * 60 + e[1] + 10
        heapq.heappush(heap, (s, e))
    
    rooms = []
    while heap:
        s, e = heapq.heappop(heap)
        if rooms and rooms[0] <= s:
            t = heapq.heappop(rooms)
        heapq.heappush(rooms, e)
    
    answer = len(rooms)
    return answer