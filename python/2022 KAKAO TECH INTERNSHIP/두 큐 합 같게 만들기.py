# 과거에 풀었던 방식이나 오늘 푼 방식이나 별반 다르지 않지만 그래도 과거에 풀었던 코드가 더 깔끔한듯.

# 2023-06-24
from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    if (sum1 + sum2) % 2 == 1:
        return -1
    i = 0
    while sum1 != sum2:
        i += 1
        if sum1 > sum2:
            if len(queue1) == 1:
                return -1
            num = queue1.popleft()
            queue2.append(num)
            sum1 -= num
            sum2 += num
        else:
            if len(queue2) == 1:
                return -1
            num = queue2.popleft()
            queue1.append(num)
            sum1 += num
            sum2 -= num
        if i > 600000:
            return -1
    return i

# 2022-11-05
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
    
    loof = 0
    while sum_queue1 != sum_queue2:
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
        loof += 1
        if loof > 600000:
            return -1
    return answer