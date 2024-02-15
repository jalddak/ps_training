import sys

alphabet_check = {}
for i in range(26):
    alphabet = chr(i+65)
    if alphabet == 'J':
        continue
    alphabet_check[alphabet] = alphabet_check.get(alphabet, False)

message = input()
key = input()

board_key = []
for i in range(len(key)):
    if alphabet_check[key[i]]:
        continue
    alphabet_check[key[i]] = True
    board_key.append(key[i])

for i in range(26):
    alphabet = chr(i+65)
    if alphabet == 'J' or alphabet_check[alphabet]:
        continue
    board_key.append(alphabet)

board = [[board_key[i*5+j] for j in range(5)] for i in range(5)]

alphabet_loca = {}
for i in range(5):
    for j in range(5):
        alphabet_loca[board[i][j]] = (i, j)

mi = 0
ml = len(message)
mt = []
while mi < ml:
    if mi == ml-1:
        mt.append(message[mi]+'X')
        mi += 1
        continue
    if message[mi] != message[mi+1]:
        mt.append(message[mi]+message[mi+1])
        mi += 2
        continue
    elif message[mi] == 'X':
        mt.append(message[mi]+'Q')
    else:
        mt.append(message[mi]+'X')
    mi += 1

final_token = []

for t in mt:
    fy, fx = alphabet_loca[t[0]]
    sy, sx = alphabet_loca[t[1]]

    if fy == sy:
        fx = fx+1 if fx+1 < 5 else fx+1-5
        sx = sx+1 if sx+1 < 5 else sx+1-5
    elif fx == sx:
        fy = fy+1 if fy+1 < 5 else fy+1-5
        sy = sy+1 if sy+1 < 5 else sy+1-5
    else:
        temp = fx
        fx = sx
        sx = temp

    final_token.append(board[fy][fx] + board[sy][sx])

print("".join(final_token))
        
    
