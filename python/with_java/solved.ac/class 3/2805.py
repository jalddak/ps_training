def binary_search(m, trees):
    l, r = 0, trees[0]
    result = 0
    while l + 1 < r:
        mid = (l + r) // 2
        temp = 0
        for t in trees:
            if t <= mid:
                break
            temp += t - mid
        if temp >= m:
            l = mid
        else:
            r = mid
    result = l
    return result


def main():
    n, m = map(int, input().split())
    trees = list(map(int, input().split()))
    trees.sort(reverse = True)
    answer = binary_search(m, trees)
    print(answer)


if __name__ == "__main__":
    main()