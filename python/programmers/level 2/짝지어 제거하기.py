def solution(s):
    stack = []
    for letter in s:
        if len(stack) != 0:
            if letter == stack[-1]:
                stack.pop()
            else:
                stack.append(letter)
        else:
            stack.append(letter)
    if len(stack) > 0:
        return 0
    return 1

# def solution(s):
#     copy_s = s
#     for letter in copy_s:
#         s = s.replace(letter+letter, '')
#     if len(s) == 0:
#         return 1
#     return 0

# def solution(s):
#     answer = -1
#     index = 0
#     while index < len(s) - 1:
#         if s[index] == s[index+1]:
#             s = s[:index] + s[index+2:]
#             index -= 2
#         index += 1
#         if index < 0:
#             index = 0
#     if len(s) == 0:
#         return 1
#     return 0