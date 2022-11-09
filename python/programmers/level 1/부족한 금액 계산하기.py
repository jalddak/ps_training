def solution(price, money, count):
    need = 0
    for c in range(count):
        need += price * (c + 1)
    if money >= need:
        return 0
    else:
        return need - money