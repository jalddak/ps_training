def solution(s, n):
    answer = ''
    for letter in s:
        if letter == ' ':
            answer += ' '
        else:
            if letter.isupper():
                if ord(letter) + n > ord('Z'):
                    answer += chr(ord('A') + ord(letter) + n - ord('Z') - 1)
                else:
                    answer += chr(ord(letter) + n)
            else:
                if ord(letter) + n > ord('z'):
                    answer += chr(ord('a') + ord(letter) + n - ord('z') - 1)
                else:
                    answer += chr(ord(letter) + n)
    return answer