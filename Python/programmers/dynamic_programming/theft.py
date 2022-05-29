def solution(money):
    answer = 0
    # 마지막 집 버리고 생각
    money_except_last = money[:-1]
    first_best_list = []
    for m in money_except_last:
        if len(first_best_list) == 0:
            best_money = m
        elif len(first_best_list) == 1:
            best_money = max(m, first_best_list[0])
        else:
            best_money = max(m + first_best_list[len(first_best_list)-2], first_best_list[len(first_best_list)-1])
        first_best_list.append(best_money)
        
    # 첫번째 집 버리고 생각
    money_except_first = money[1:]
    last_best_list = []
    for m in money_except_first:
        if len(last_best_list) == 0:
            best_money = m
        elif len(last_best_list) == 1:
            best_money = max(m, last_best_list[0])
        else:
            best_money = max(m + last_best_list[len(last_best_list)-2], last_best_list[len(last_best_list)-1])
        last_best_list.append(best_money)

    answer = max(first_best_list.pop(), last_best_list.pop())
    return answer

# from collections import deque

# def solution(money):
#     answer = 0
#     import_first = money[:-1]
#     import_last = money[1:]
    
#     # 첫번째 집 포함 최적
#     first_list = deque([[import_first[0],0]])
#     while first_list[0][1] < len(import_first) - 2:
#         pop_info = first_list.popleft()
#         first_list.append([pop_info[0]+import_first[pop_info[1]+2], pop_info[1]+2])
#         if pop_info[1] < len(import_first) - 3:
#             first_list.append([pop_info[0]+import_first[pop_info[1]+3], pop_info[1]+3])
#     sort_first = list(first_list)
#     sort_first.sort(key=lambda x:x[0], reverse=True)

#     second_list = deque([[import_first[1],1]])
#     while second_list[0][1] < len(import_first) - 2:
#         pop_info = second_list.popleft()
#         second_list.append([pop_info[0]+import_first[pop_info[1]+2], pop_info[1]+2])
#         if pop_info[1] < len(import_first) - 3:
#             second_list.append([pop_info[0]+import_first[pop_info[1]+3], pop_info[1]+3])
#     sort_second = list(second_list)
#     sort_second.sort(key=lambda x:x[0], reverse=True)

#     first_best = max(sort_first[0][0], sort_second[0][0])

#     # 마지막 집 포함 최적
#     first_list = deque([[import_last[0],0]])
#     while first_list[0][1] < len(import_last) - 2:
#         pop_info = first_list.popleft()
#         first_list.append([pop_info[0]+import_last[pop_info[1]+2], pop_info[1]+2])
#         if pop_info[1] < len(import_last) - 3:
#             first_list.append([pop_info[0]+import_last[pop_info[1]+3], pop_info[1]+3])
#     sort_first = list(first_list)
#     sort_first.sort(key=lambda x:x[0], reverse=True)

#     second_list = deque([[import_last[1],1]])
#     while second_list[0][1] < len(import_last) - 2:
#         pop_info = second_list.popleft()
#         second_list.append([pop_info[0]+import_last[pop_info[1]+2], pop_info[1]+2])
#         if pop_info[1] < len(import_last) - 3:
#             second_list.append([pop_info[0]+import_last[pop_info[1]+3], pop_info[1]+3])
#     sort_second = list(second_list)
#     sort_second.sort(key=lambda x:x[0], reverse=True)

#     last_best = max(sort_first[0][0], sort_second[0][0])

#     answer = max(first_best, last_best)
#     print(answer)
#     return answer

money = [1, 1, 4, 1, 4]
solution(money)

# print(solution([1,2,3,1]), 4)
# print(solution([1,1,4,1,4]), 8)
# print(solution([1000,0,0,1000,0,0,1000,0,0,1000]), 3000)
# print(solution([1000,1,0,1,2,1000,0]), 2001)
# print(solution([1000,0,0,0,0,1000,0,0,0,0,0,1000]), 2000)
# print(solution([1,2,3,4,5,6,7,8,9,10]), 30)
# print(solution([0,0,0,0,100,0,0,100,0,0,1,1]), 201)
# print(solution([11,0,2,5,100,100,85,1]), 198)
# print(solution([1,2,3]), 3)
# print(solution([91,90,5,7,5,7]), 104)
# print(solution([90,0,0,95,1,1]), 185)
# print(solution([1, 5, 1, 5, 1]), 10)