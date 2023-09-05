def solution(phone_book):
    answer = True
    pb_dict = {}
    for num in phone_book:
        pb_dict[num] = 0
    for num in phone_book:
        temp = ''
        for i in range(len(num)-1):
            temp += num[i]
            if temp in pb_dict:
                return False
    return answer

# 탐색을 하는 경우에도 list 보단 dict가 낫다. hash table 이용해서 그런듯.