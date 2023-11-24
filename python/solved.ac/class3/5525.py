def soulution1():    
    N = int(input())
    M = int(input())

    check = input()

    P = ['IO' for _ in range(N)]
    P.append('I')
    P = ''.join(P)

    i = 0
    result = 0
    while i + 2*N + 1 <= len(check):
        if check[i:i + 2*N + 1] == P:
            result += 1
        i += 1

    print(result)

def solution2():
    N = int(input())
    M = int(input())

    before = ['O', 0]
    string = input()
    result = 0
    for c in string:
        if c == 'I':
            if before[0] == 'O':
                before = ['I', before[1]]
            else:
                before = ['I', 0]
        if c == 'O':
            if before[0] == 'I':
                before = ['O', before[1]+1]
            else:
                before = ['O', 0]
        if before[0] == 'I' and before[1] >= N:
            result += 1
    print(result)



if __name__ == '__main__':
    solution2()