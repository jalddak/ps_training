import heapq

def solution(operations):
    answer = []
    min_heap = []
    max_heap = []
    num_list = []
    for op in operations:
        op = op.split()
        if op[0] == 'I':
            heapq.heappush(min_heap, int(op[1]))
            heapq.heappush(max_heap, -int(op[1]))
        elif op[0] == 'D' and op[1] == '1' and len(max_heap) != 0:
            min_heap.remove(-heapq.heappop(max_heap))
        elif op[0] == 'D' and op[1] == '-1' and len(min_heap) != 0:
            max_heap.remove(-heapq.heappop(min_heap))
    if len(max_heap) > 0:
        answer.append(-max_heap[0])
        answer.append(min_heap[0])
    else:
        answer = [0, 0]
    return answer

if __name__ == '__main__':
    solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])