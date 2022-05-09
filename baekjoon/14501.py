def main():
    N = int(input())
    max_incomes = [0 for _ in range(N + 1)]
    for i in range(N):
        term, income = map(int, input().split())
        if i > 0:
            max_incomes[i] = max(max_incomes[i], max_incomes[i-1])
        day = term + i
        if day < N + 1:
            max_incomes[day] = max((income + max_incomes[i]), max_incomes[day])
    max_incomes[len(max_incomes) - 1] = max(max_incomes[len(max_incomes) - 2], max_incomes[len(max_incomes) - 1])
    print(max_incomes[len(max_incomes) - 1])

    


if __name__ == '__main__':
    main()