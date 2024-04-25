def solution(n, m):
    최대공약수 = 1
    for num in range(2, min(n, m)+1):
        if n%num==0 and m%num==0:
            최대공약수 = num
    최소공배수 = 최대공약수 * (n/최대공약수) * (m/최대공약수)
    answer = [최대공약수, 최소공배수]
    return answer