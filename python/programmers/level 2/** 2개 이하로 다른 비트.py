def solution(numbers):
    answer = []
    for number in numbers:
        num_2 = list(bin(number)[2:])
        num_2.reverse()
        num_2.append('0')
        for i in range(len(num_2)-1):
            if num_2[i] == '0':
                num_2[i] = '1'
                break
            elif num_2[i] == '1' and num_2[i+1] == '0':
                num_2[i] = '0'
                num_2[i+1] = '1'
                break
        num_2.reverse()
        num_2 = ''.join(num_2)
        answer.append(int(num_2, 2))
                    
    return answer

# def solution(numbers):
#     answer = []
#     for number in numbers:
#         num_2 = list(bin(number)[2:])
#         num_2.reverse()
#         x = number
#         while True:
#             x += 1
#             x_2 = list(bin(x)[2:])
#             x_2.reverse()
#             dif = 0
#             for i in range(len(x_2)):
#                 if i < len(num_2):
#                     if x_2[i] == num_2[i]:
#                         continue
#                     else:
#                         dif += 1
#                 else:
#                     if x_2[i] == 0:
#                         continue
#                     else:
#                         dif += 1
#                 if dif > 2:
#                     break
#             if dif <= 2:
#                 answer.append(x)
#                 break
            
        
#     return answer