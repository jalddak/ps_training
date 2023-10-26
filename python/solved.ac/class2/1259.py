while True:
    n = input()
    if n == '0':
        break
    temp = list(n)
    temp.reverse()
    temp = ''.join(temp)
    if n == temp:
        print('yes')
    else:
        print('no')