def solution(dots):
    for i in range(len(dots)):
        for j in range(i+1, len(dots)):
            index_list = [index for index in range(len(dots))]
            index_list.remove(i)
            index_list.remove(j)
            
            x = dots[i][0] - dots[j][0]
            y = dots[i][1] - dots[j][1]
            
            비교x = dots[index_list[0]][0] - dots[index_list[1]][0]
            비교y = dots[index_list[0]][1] - dots[index_list[1]][1]
            
            if x / y == 비교x / 비교y:
                return 1
            
            
    return 0