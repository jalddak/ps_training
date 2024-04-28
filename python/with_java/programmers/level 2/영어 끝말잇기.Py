def solution(n, words):
    before = words[0]
    already = set([words[0]])
    for i in range(1, len(words)):
        if before[-1] != words[i][0] or words[i] in already:
            return [i%n+1, i//n+1]
        before = words[i]
        already.add(words[i])
    return [0, 0]