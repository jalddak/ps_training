def solution(n, k):
    answer = 0
    change_num = []
    while n > k:
        change_num.append(n % k)
        n = n // k
    change_num.append(n)
    change_num.reverse()
    change_num = ''.join(str(num) for num in change_num)
    candidates = change_num.split('0')
    print(candidates)
    
    for candidate in candidates:
        if candidate.isdigit():
            if candidate != '1':
                result = True
                for i in range(2, int(int(candidate) ** 0.5 + 1)):
                    if int(candidate) % i == 0:
                        result = False
                        break
                if result:
                    answer += 1
    return answer