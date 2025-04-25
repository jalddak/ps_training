# import sys
# sys.stdin = open('./python/with_java/swea/input.txt', 'r')



tcCnt = int(input())

hashCode = {
    211 : 0,
    221 : 1,
    122 : 2,
    411 : 3,
    132 : 4,
    231 : 5,
    114 : 6,
    312 : 7,
    213 : 8,
    112 : 9
}

def gcd(a, b):
    if a < b:
        a, b = b, a
    while (b != 0):
        a, b = b, a % b
    return a

answer = []
for tc in range(1, tcCnt + 1):
    sb = "#" + str(tc) + " "
    n, m = map(int, input().split())

    board = [list(input()) for _ in range(n)]

    # 암호 한줄씩 중복되는 줄은 제거
    rows = set()
    for i in range(n):
        row = []
        flag = False
        for j in range(m):
            if board[i][j] == '0':
                row.append('0000')
                continue
            flag = True
            binary = bin(int(board[i][j], 16))[2:]
            binary = '0' * (4 - len(binary)) + binary
            row.append(binary)
        row = "0" + "".join(row) + "0"
        if flag:
            rows.add(row)
    result = 0

    codes = set()
    for row in rows:
        code = ''
        check = []
        cur = row[0]
        cnt = 1
        for i in range(1, len(row)):
            if cur == row[i]:
                cnt += 1
                continue
            check.append(cnt)
            cur = row[i]
            cnt = 1

            if len(check) == 4:
                check = list(map(int, check))
                gcdResult = gcd(gcd(check[1], check[2]), check[3])
                check = list(map(lambda x: x//gcdResult, check))
                code += str(hashCode[check[1] * 100 + check[2] * 10 + check[3]])
                check = []
                if len(code) == 8:
                    codes.add(code)
                    code = ''
    
    for code in codes:
        temp = 0
        valid = 0
        for i in range(8):
            num = int(code[i])
            temp += num
            if i % 2 != 0:
                valid += num
            else:
                valid += num * 3
        
        if valid % 10 == 0:
            result += temp
    
    sb += str(result)
    print(sb)
    answer.append(sb)

for a in answer:
    print(a)