# A B C D E F G H I J K L M  |  N O P Q R S T U V W X Y Z
# 1 2 3 4 5 6 7 8 9 0 1 2 3  |  4 5 6 7 8 9 0 1 2 3 4 5 6

# 아래에 주석으로 써놓은 코드는 그리드 방식.
# 그리드 방식 문제라고 해놓고 완전탐색으로 풀어야 답이 풀린다.
# 그리드는 최적해를 구할 수 없기 때문에 문제 자체에서 오류다

name = "AABBAAAAAAABBBB"

def solution(name):
    answer = 0
    name_int = []
    for alphabet in name:
        name_int.append(ord(alphabet))

    check = 0
    index_list = []
    for index in range(len(name_int)):
        if name_int[index] != 65 and index != 0:
            index_list.append(index)
            check += 1
    
    for num in name_int:
        if num > 77:
            answer += (91 - num)
        else:
            answer += (num - 65)

    if check == 1:
        answer += min(rightend(index_list), leftend(name_int, index_list))
    elif check > 1:
        answer += min(rightend(index_list), leftend(name_int, index_list), 
        right_left_best(name_int, index_list),
        left_right_best(name_int, index_list))

    print(answer)
    return answer

def rightend(index_list):
    return index_list[len(index_list)-1]

def leftend(name_int, index_list):
    return len(name_int) - index_list[0]

def right_left_best(name_int, index_list):
    temp_list = []
    for i in range(len(index_list) - 1):
        temp_list.append((index_list[i]*2) + len(name_int) - index_list[i+1])
    temp_list.sort()
    return temp_list[0]

def left_right_best(name_int, index_list):
    temp_list = []
    index_list.sort(reverse = True)
    for i in range(len(index_list) - 1):
        temp_list.append(((len(name_int) - index_list[i])*2) + index_list[i+1])
    temp_list.sort()
    return temp_list[0]

solution(name)

# def solution(name):
#     answer = 0
#     name_int = []
#     for alphabet in name:
#         name_int.append(ord(alphabet))

#     check = 0
#     for not_A in name_int:
#         if not_A != 65:
#             check += 1
    
#     for num in name_int:
#         if num > 77:
#             answer += (91 - num)
#         else:
#             answer += (num - 65)
    
#     index = 0

#     while check != 0:
#         if index == 0 and name_int[index] != 65:
#             name_int[index] = 65
#             check -= 1
#         front = 0
#         back = 0
#         for i in range(1, len(name_int)):
#             local_index = index + i
#             if local_index >= len(name_int):
#                 local_index -= len(name_int)
#             if name_int[local_index] != 65:
#                 front += 1
#                 break;
#             front += 1

#         for i in range(1, len(name_int)):
#             local_index = index - i
#             if local_index < 0:
#                 local_index += len(name_int)
#             if name_int[local_index] != 65:
#                 back += 1
#                 break;
#             back += 1

#         before_index = index

#         if front <= back:
#             index += front
#             if index >= len(name_int):
#                 index -= len(name_int)
#         else:
#             index -= back
#             if index < 0:
#                 index += len(name_int)

#         check -= 1
#         name_int[index] = 65
#         answer += min(front, back)
#         print(name_int)
#         print(front, back, before_index, answer)

#     return answer
