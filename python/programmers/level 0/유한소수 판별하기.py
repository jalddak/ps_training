def solution(a, b):
    b_list = []
    소인수 = 2
    while b != 1:
        if b % 소인수 == 0:
            b_list.append(소인수)
            b = b // 소인수
            소인수 = 2
        else:
            소인수 += 1
    
    print(b_list)
    for b in b_list:
        if b == 2 or b == 5:
            continue
        else:
            if a % b != 0:
                return 2
            else:
                a = a // b
    return 1