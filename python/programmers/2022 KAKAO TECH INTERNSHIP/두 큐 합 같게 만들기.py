from collections import deque

def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    sum_queue1 = sum(queue1)
    sum_queue2 = sum(queue2)
    
    sumOfQueue = sum_queue1 + sum_queue2
    if sumOfQueue % 2 == 1:
        return -1
    maxNum = max(max(queue1), max(queue2))
    if maxNum > sumOfQueue - maxNum:
        return -1
    
    while sum_queue1 != sum_queue2:
        if answer >= 600000:
            return -1
        answer += 1
        if sum_queue1 > sum_queue2:
            pop_num = queue1.popleft()
            sum_queue1 -= pop_num
            sum_queue2 += pop_num
            queue2.append(pop_num)
        elif sum_queue1 < sum_queue2:
            pop_num = queue2.popleft()
            sum_queue1 += pop_num
            sum_queue2 -= pop_num
            queue1.append(pop_num)
    
    return answer