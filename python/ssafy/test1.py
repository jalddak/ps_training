def main():
    T = int(input())
    for t in range(1, T+1):
        N = int(input())
        answer = 0
        string_list = list(input())
        before = string_list[0]
        for i in range(1, N):
            current = string_list[i]
            if before in ['a', 'b'] and current in ['a', 'b']:
                string_list[i] = ''
                answer += 1
            else:
                before = current

        print("#"+str(t), answer)


if __name__ == '__main__':
    main()