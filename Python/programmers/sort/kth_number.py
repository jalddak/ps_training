array = [1, 5, 2, 6, 3, 7, 4]
commands = 	[[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def solution(array, commands):
    answer = []
    for command in commands:
        sort_array = array[command[0]-1:command[1]]
        sort_array.sort()
        answer.append(sort_array[command[2]-1])
    return answer

solution(array, commands)