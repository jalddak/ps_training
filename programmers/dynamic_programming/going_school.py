m = 4
n = 3
puddles = [[2,2]]

def solution(m, n, puddles):
    answer = 0
    location = [[0 for col in range(m)] for row in range(n)]
    for puddle in puddles:
        location[puddle[1]-1][puddle[0]-1] = -1
    location[0][0] = 1
    x = 0
    y = 0
    while y < n:
        while x < m:
            if location[y][x] > 0:
                if x < m-1:
                    if location[y][x+1] != -1:
                        location[y][x+1] += location[y][x]
                        location[y][x+1] = location[y][x+1] % 1000000007
                if y < n-1:
                    if location[y+1][x] != -1:
                        location[y+1][x] += location[y][x]
                        location[y+1][x] = location[y+1][x] % 1000000007
            x += 1
        x = 0
        y += 1
    answer = location[n-1][m-1]
    return answer

# def solution(m, n, puddles):
#     answer = 0
#     location_list = [[1,1]]
#     while True:
#         index = len(location_list) - 1
#         after_location_list = []
#         while len(location_list) != 0:
#             x = location_list[index][0]
#             y = location_list[index][1]
#             location_list.pop()
#             if [x+1, y] not in puddles and x+1 <= m:
#                 after_location_list.append([x+1, y])
#             if [x, y+1] not in puddles and y+1 <= n:
#                 after_location_list.append([x, y+1])
#             index -= 1
#         location_list = after_location_list
#         if [m, n] in location_list:
#             break
#     for location in location_list:
#         if location[0] == m and location[1] == n:
#             answer += 1
#     answer = answer % 1000000007
#     return answer

solution(m, n, puddles)