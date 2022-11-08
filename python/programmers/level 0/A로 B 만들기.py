def solution(before, after):
    after = list(after)
    for letter in before:
        if letter in after:
            after.remove(letter)
        else:
            return 0
    return 1