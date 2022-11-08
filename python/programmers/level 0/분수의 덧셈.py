def solution(denum1, num1, denum2, num2):
    denum = denum1 * num2 + denum2 * num1
    num = num1 * num2
    
    temp = 2
    num_소인수체크 = num
    num_list = []
    while num_소인수체크 != 1:
        if num_소인수체크 % temp == 0:
            num_list.append(temp)
            num_소인수체크 = num_소인수체크 // temp
            temp = 2
        else:
            temp += 1
    
    for temp in num_list:
        if denum % temp == 0 and num % temp == 0:
            denum = denum // temp
            num = num // temp
    answer = [denum, num]
    return answer