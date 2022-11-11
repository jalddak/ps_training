def solution(arr):
    answer = 1
    factorization = []
    for num in arr:
        fact_num = []
        temp = 2
        while num != 1:
            if num % temp == 0:
                num = num // temp
                fact_num.append(temp)
                temp = 2
                continue
            temp += 1
        factorization.append(fact_num)
    
    for i in range(len(factorization)):
        for num in factorization[i]:
            answer *= num
            for j in range(i+1, len(factorization)):
                if num in factorization[j]:
                    factorization[j].remove(num)
                
    return answer