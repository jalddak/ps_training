def solution(array):
    cnt_dict = {}
    for num in array:
        if num not in cnt_dict:
            cnt_dict[num] = 1
        else:
            cnt_dict[num] += 1
    sort_tuple = sorted(cnt_dict.items(), key=lambda x:x[1], reverse=True)
    
    if len(sort_tuple) != 1:
        if sort_tuple[0][1] == sort_tuple[1][1]:
            return -1
    return sort_tuple[0][0]