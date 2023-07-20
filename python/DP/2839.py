def main():
    w = int(input())
    n = w // 5
    for i in range(n, -1, -1):
        a = w - 5*i

        if a % 3 == 0:
            print(i+a//3)
            return 0
    print(-1)

if __name__ == '__main__':
    main()