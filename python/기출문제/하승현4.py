def main(P):
    answer = 0
    P.sort(reverse = True)
    candidates = []
    while len(P) != 0:
        n = P.pop()
        check = 0
        for c in candidates:
            if c[-1] < n:
                check = 1
                c.append(n)
                break
        if check == 0:
            candidates.append([n])

    for c in candidates:
        answer += len(c) - 1

    print(answer)
    return answer


main([3,2,1,4,5])
main([20,10,10,20])
main([103,101,103,103,101,102,100,100,101,104])

# 1~4번까지 5시 57분 시작 7시 9분 끝 73분 걸림