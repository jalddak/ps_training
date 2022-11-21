def solution(n):
    answer = 0
    first = 1
    second = 2
    for i in range(n-2):
        sumfs = first + second
        first = second
        second = sumfs
            
    return sumfs % 1000000007