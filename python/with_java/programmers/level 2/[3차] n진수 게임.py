d = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
for n in range(10):
    d[n] = str(n)
    
def change(num, n):
    result = []
    while num > 0:
        result.append(num % n)
        num = num // n
    result.reverse()
    result = ''.join(map(lambda x:d[x], result))
    return result

def solution(n, t, m, p):
    length = t * m
    game = '0'
    num = 1
    while length > len(game):
        game += change(num, n)
        num += 1
    answer = ''
    for i in range(p-1, len(game), m):
        answer += game[i]
        if len(answer) == t:
            break
    return answer