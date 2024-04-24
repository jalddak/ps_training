def solution(n):
    num = n-1
    answer = num
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            answer = i
            break
    return answer