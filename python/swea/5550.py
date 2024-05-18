T = int(input())

for t in range(1, T+1):
    answer = 0
    d = {'c':0, 'r':0, 'o':0, 'a':0, 'k':0}
    need = {'c':'k', 'r':'c', 'o':'r', 'a':'o', 'k':'a'}
    command = list(input())
    for c in command:
        if c == 'c':
            answer += 1
            if d[need[c]] != 0:
                d[need[c]] -= 1
                answer -= 1
            d[c] += 1
        elif d[need[c]] > 0:
            d[need[c]] -= 1
            d[c] += 1
        else:
            answer = -1
            break
    if answer != -1 and answer != d['k']:
        answer = -1
    print("#"+str(t), answer)