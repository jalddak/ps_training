def solution(phone_book):
    answer = True
    p_dict = {}
    for num in phone_book:
        if num not in p_dict:
            p_dict[num] = 1
    for num in phone_book:
        temp = ''
        for index in range(len(num)-1):
            temp += num[index];
            if temp in p_dict:
                return False
    return answer