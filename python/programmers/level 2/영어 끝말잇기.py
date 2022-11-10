def solution(n, words):
    using = []
    turn = [1, 1]
    for word in words:
        if len(using) > 0 and using[-1][-1] != word[0]:
            return turn
        elif word in using:
            return turn
        else:
            using.append(word)
            turn[0] += 1
            if turn[0] // (n + 1) > 0 :
                turn[1] += 1
                turn[0] = turn[0] % n
    return [0, 0]