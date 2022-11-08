def solution(s):
    answer = ''
    dict = {}
    for letter in s:
        if letter not in dict:
            dict[letter] = 1
        else:
            dict[letter] += 1
    for letter in dict:
        if dict[letter] == 1:
            answer += letter
    answer = list(answer)
    answer.sort()
    answer = ''.join(answer)
    return answer