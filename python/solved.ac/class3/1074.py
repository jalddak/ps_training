N, r, c = list(map(int, input().split()))

dy = [0, 0, 1, 1]
dx = [0, 1, 0, 1]

def f(y, x, num, length):
    if length == 1:
        print(num)
        exit()

    n_len = length // 2
    d = 0
    if r < y + n_len and c >= x + n_len:
        d = 1
    elif r >= y + n_len and c < x + n_len:
        d = 2
    elif r >= y + n_len and c >= x + n_len:
        d = 3

    increase = (length // 2) ** 2
    ny = y + dy[d] * (length // 2)
    nx = x + dx[d] * (length // 2)
    n_num = num + d * increase
    f(ny, nx, n_num, n_len)

f(0, 0, 0, 2**N)