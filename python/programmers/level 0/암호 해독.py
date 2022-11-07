def solution(cipher, code):
    answer = ''
    for index in range(len(cipher)):
        if (index + 1) % code == 0:
            answer += cipher[index]
    return answer