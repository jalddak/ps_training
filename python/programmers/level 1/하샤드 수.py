def solution(x):
    str_x = str(x)
    numlist = [int(num) for num in str_x]
    if x % sum(numlist) == 0:
        return True
    return False