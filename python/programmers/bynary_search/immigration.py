def solution(n, times):
    answer = 0
    min_time = 1
    max_time = max(times) * n
    
    while min_time <= max_time:
        human = 0
        mid_time = (max_time + min_time) // 2
        for time in times:
            human += mid_time // time
            if human >= n:
                break
        if human >= n:
            answer = mid_time
            max_time = mid_time - 1
        elif human < n:
            min_time = mid_time + 1
            
    return answer

# import numpy as np
# from collections import deque

# def solution(n, times):
#     times_dict = {}
#     for time in times:
#         if time not in times_dict:
#             times_dict[time] = 0
#     times_keys = list(times_dict.keys())
#     min_index = 0
#     while n > 0:
#         times_values = list(times_dict.values())
#         for i in range(len(times_values)):
#             times_values[i] += times_keys[i]
#         min_index = np.argmin(times_values)
#         times_dict[times_keys[min_index]] += times_keys[min_index]
#         n -= 1
#     times_values = list(times_dict.values())
#     answer = times_values[min_index]
#     return answer