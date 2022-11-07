def solution(my_string):
    for letter in ['a', 'e', 'i', 'o', 'u']:
        my_string = my_string.replace(letter, '')
    return my_string