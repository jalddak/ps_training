def solution(sizes):
    answer = 0
    big_big = 0
    small_big = 0
    for size in sizes:
        if size[0] > size[1]:
            if size[0] > big_big:
                big_big = size[0]
            if size[1] > small_big:
                small_big = size[1]
        else:
            if size[1] > big_big:
                big_big = size[1]
            if size[0] > small_big:
                small_big = size[0]
                
    answer = big_big * small_big
    
    return answer