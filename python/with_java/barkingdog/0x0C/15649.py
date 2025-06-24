answer = []

def back(n, m, check, depth, result):
    if depth == m:
        answer.append(" ".join(result))
        return
    for num in range(1, n + 1):
        if check[num]:
            continue
        check[num] = True
        result.append(str(num))
        back(n, m, check, depth + 1, result)
        result.pop()
        check[num] = False

def main():
    n, m = map(int, input().split())
    check = [False for _ in range(n + 1)]
    back(n, m, check, 0, [])
    for a in answer:
        print(a)

if __name__ == "__main__":
    main()