L, C = map(int, input().split())

l = list(input().split(' '))

l.sort()

candidate = []

def loof(index, password):
    global L, C, l, candidate
    if len(password) < L:
        for i in range(index, C):
            password += l[i]
            loof(i+1, password)
            password = password[:-1]
    else:
        check = 0
        for a in password:
            if a in ['a','i','u','e','o']:
                check += 1
        if check >= 1 and L-check >= 2:
            candidate.append(password)

if __name__ == '__main__':
    loof(0, '')
    for c in candidate:
        print(c)