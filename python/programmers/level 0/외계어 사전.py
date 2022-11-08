def solution(spell, dic):
    answer = 0
    for word in dic:
        word = list(word)
        for letter in spell:
            if letter in word:
                word.remove(letter)
            else:
                word.append(letter)
        if len(word) == 0:
            return 1
    return 2