# 또 낚였다 그리디 문제가 아니라 완전탐색 문제이다.

# def solution(name):
#     answer = 0
#     i = 0
#     result = []
#     name = list(name)
#     for num in range(len(name)):
#         result.append('A')
        
#     while(True):
#         if name[i] is not chr(65):
#             answer += int(ord(name[i])) - 65
#             name[i] = 'A'
#         if str(result) == str(name):
#             break
#         else:
#             i, move = check(i, i, name)
#             answer += move
#     return answer
            
# def check(front, back, name):
#     result = 0
#     move = 0
#     while(True):
#         move += 1
#         front = front - 1 if front <= 0 else len(name) - 1
#         back = back + 1 if back >= len(name)-1 else 0
#         if name[back] is not chr(65):
#             result = back
#             break
#         elif name[front] is not chr(65):
#             result = front
#             break
    
#     return result, move

# if __name__ == '__main__':
#     solution("JEROEN")
