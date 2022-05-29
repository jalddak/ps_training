def solution(clothes):
    answer = 0
    hash = {}
    for item in clothes:
        if item[1] in hash:
            hash[item[1]] += 1
        else:
            hash[item[1]] = 1

    array = list(hash.values())
    temp = 1
    for i in array:
        temp = temp * (i+1)
    answer = answer + temp - 1
    return answer