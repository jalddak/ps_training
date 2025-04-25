n, r, c = map(int, input().split())
length = 2 ** n
num = 0

while(length > 1):
    temp = length ** 2 // 4
    half = length // 2

    d = 0
    if r < half and c >= half:
        d = 1
    elif r >= half and c < half:
        d = 2
    elif r >= half and c >= half:
        d = 3
    

    num += temp * d
    if r >= half:
        r -= half
    if c >= half:
        c -= half

    length = half

print(num)