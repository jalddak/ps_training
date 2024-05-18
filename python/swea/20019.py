T = int(input())

for t in range(1, T+1):
    answer = "YES"
    word = input()
    l, m, r = 0, len(word)//2, len(word)-1
    mr, ml = m - 1, m + 1
    while l <= mr:
        if len({word[l], word[r], word[mr], word[ml]}) != 1:
            answer = "NO"
            break
        l += 1
        r -= 1
        mr -= 1
        ml += 1
    print("#" + str(t), answer)