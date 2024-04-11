def solution(food_times, k):
    answer = 0
    sorted_times = sorted(food_times, key=lambda x:-x)
    complete = 0
    length = len(sorted_times)
    while 0 < length <= k:
        next = sorted_times[-1]
        gap = next - complete
        if k >= gap * length:
            k -= gap * length
            complete = next
            while sorted_times and complete == sorted_times[-1]:
                sorted_times.pop()
                length -= 1
        else:
            k %= length
            
    if length == 0:
        return -1
    
    for i in range(len(food_times)):
        ft = food_times[i]
        if ft <= complete:
            continue
        if k == 0:
            answer = i+1
            break
        k -= 1
        
    return answer