from itertools import permutations
import math

def solution(numbers):
    answer = 0
    num_list = []
    int_list = []
    for n in numbers:
        num_list.append(n)
        
    for i in range(len(numbers)):
        i_num = set(list(permutations(num_list, i+1)))
        for s in i_num:
            num = ''
            for n in s:
                num += n
            num = int(num)
            int_list.append(num)
    int_list = list(set(int_list))
    
    for num in int_list:
        if num > 1:
            answer += 1
            for n in range(2, int(math.sqrt(num) + 1)):
                if num % n == 0:
                    answer -= 1
                    break
    
    
    return answer