import heapq

def solution(operations):
    heap = []
    status = -1
    for op in operations:
        command, num = op.split()
        num = int(num)
        if command == "I":
            if status == 1:
                num = -num
            heapq.heappush(heap, num)
        if command == "D":
            if num != status:
                heap = list(map(lambda x:-x, heap))
                heapq.heapify(heap)
                status = num
            if heap:
                heapq.heappop(heap)
    answer = []
    if heap:
        if status == 1:
            answer.append(-heap[0])
            heap = list(map(lambda x:-x, heap))
            heapq.heapify(heap)
            answer.append(heap[0])
        else:
            answer.append(heap[0])
            heap = list(map(lambda x:-x, heap))
            heapq.heapify(heap)
            answer.append(-heap[0])
        answer.sort(reverse=True)
    else:
        answer = [0, 0]
            
    return answer