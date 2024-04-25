def solution(price, money, count):
    need = 0
    for c in range(1, count+1):
        need += price * c
    return need - money if need > money else 0