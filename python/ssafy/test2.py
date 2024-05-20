def main():
    T = int(input())
    for t in range(1, T+1):
        N = int(input())
        answer = 0
        info = [list(map(lambda x:x-1, map(int, input().split()))) for _ in range(2)]
        flag = 0
        current = [i for i in range(N)]

        while True:
            answer += 1
            after = [-1 for _ in range(N)]
            like = info[flag]
            for i in range(N):
                after[like[i]] = current[i]

            print(current, after)
            bp = True
            for i in range(N):
                if after[i] != current[i]:
                    bp = False
            if bp:
                break
            flag = 1 if flag == 0 else 0
            current = after

        print("#"+str(t), answer)


if __name__ == "__main__":
    main()