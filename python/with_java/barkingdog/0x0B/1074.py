w = [[0, 1], [2, 3]]
answer = 0

def rc(n, r, c):
    global answer
    if n == 0:
        return
    temp = 2 ** (n - 1)
    answer += temp ** 2 * w[r//temp][c//temp]
    rc(n-1, r%temp, c%temp)

def main():
    global answer
    n, r, c = map(int, input().split())
    rc(n, r, c)
    print(answer)

if __name__ == "__main__":
    main()