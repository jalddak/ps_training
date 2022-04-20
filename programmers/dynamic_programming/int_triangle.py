triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

def solution(triangle):
    answer = 0
    depth = len(triangle) - 1
    level = triangle[depth]
    while depth != 0:
        for index in range(len(triangle[depth-1])):
            level[index] = triangle[depth-1][index] + max(level[index], level[index+1])
        level.pop()
        depth -=1
    answer += level[0]
    print(answer)
    return answer

solution(triangle)






# triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

# def solution(triangle):
#     answer = 0
#     triangle.reverse()
#     save_list = []
#     height = 0
#     for index in range(len(triangle[height])):
#         save = [triangle[height][index], index]
#         save_list.append(save)
#     height += 1
#     if height != len(triangle):
#         save_list = recursion(triangle, save_list, height)
#     save_list.sort(key=lambda x:x[0], reverse = True)
#     answer = save_list[0][0]
#     print(save_list)
#     print(answer)
#     return answer

# def recursion(triangle, save_list, height):
#     index = 0
#     while index < len(save_list):
#         if save_list[index][1] == 0:
#             save_list[index][0] += triangle[height][0]
#         elif save_list[index][1] == len(triangle[height-1])-1:
#             save_list[index][0] += triangle[height][len(triangle[height])-1]
#             save_list[index][1] -= 1
#         else:
#             left = triangle[height][save_list[index][1]-1]
#             right = triangle[height][save_list[index][1]]
#             if max(left, right) == left:
#                 save_list[index][0] += left
#                 save_list[index][1] -= 1
#             else:
#                 save_list[index][0] += right
#         index += 1
#     height += 1
#     if height != len(triangle):
#         save_list = recursion(triangle, save_list, height)
#     return save_list

# solution(triangle)