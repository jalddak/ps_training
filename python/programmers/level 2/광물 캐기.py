import heapq

def solution(picks, minerals):
    answer = 0
    dia, iron, stone = picks
    pick_cnt = sum(picks)
    heap = []
    index = 0
    while index < len(minerals) and pick_cnt:
        end = min(index+5, len(minerals))
        mineral = minerals[index:end]
        
        tired = []
        for m in mineral:
            if m == 'diamond':
                tired.append(25)
            elif m == 'iron':
                tired.append(5)
            else:
                tired.append(1)
        
        heapq.heappush(heap, (-sum(tired), tired))
        index += end - index
        pick_cnt -= 1
    
    while heap:
        temp, tired = heapq.heappop(heap)
        if dia > 0:
            p = 25
            dia -= 1
        elif iron > 0:
            p = 5
            iron -= 1
        else:
            p = 1
        for t in tired:
            answer += t//p
            answer += 1 if t//p == 0 else 0
        
    return answer