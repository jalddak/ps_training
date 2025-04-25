n, m = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort(reverse=True)

# 1번째 방법
def bs():
    s, e = 0, trees[0]

    answer = 0
    while s <= e:
        mid = (s + e) // 2

        check = 0
        for t in trees:
            if t <= mid:
                break
            check += t - mid

        if check >= m:
            s = mid + 1
            answer = mid
        elif check < m:
            e = mid - 1

    return answer

print(bs())


# 2번째 방법
def bs():
    s, e = 0, trees[0]

    while s + 1 < e:
        mid = (s + e) // 2

        check = 0
        for t in trees:
            if t <= mid:
                break
            check += t - mid

        if check >= m:
            s = mid
        elif check < m:
            e = mid
    
    return s

print(bs())

# 2번째 방법 - 체크함수 구현

def check(mid):
    temp = 0
    for t in trees:
        if t <= mid:
            break
        temp += t - mid
    return temp >= m

def bs():
    s, e = 0, trees[0]

    while s + 1 < e:
        mid = (s + e) // 2

        if check(mid):
            s = mid
        else:
            e = mid
    
    return s

print(bs())