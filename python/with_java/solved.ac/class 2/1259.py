while True:
    n = input()
    if n == '0': break
    length = len(n)
    flag = True
    for i in range(length//2):
        if n[i] != n[length - (i+1)]:
            flag = False
            break
    if flag:
        print('yes')
    else:
        print('no')