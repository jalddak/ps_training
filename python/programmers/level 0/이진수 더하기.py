def solution(bin1, bin2):
    answer = format(int(bin1, 2) + int(bin2, 2), 'b')
    
#     answer = ''
#     bin1 = list(bin1)
#     bin1.reverse()
#     bin2 = list(bin2)
#     bin2.reverse()
    
#     길이차이 = len(bin1) - len(bin2)
#     if 길이차이 > 0:
#         for _ in range(길이차이):
#             bin2.append('0')
#     elif 길이차이 < 0:
#         for _ in range(길이차이):
#             bin1.append('0')
    
#     올림 = 0
#     for index in range(len(bin1)):
#         num = int(bin1[index]) + int(bin2[index]) + 올림
#         if num > 1:
#             num -= 2
#             올림 = 1
#         else:
#             올림 = 0
#         answer += str(num)
#     if 올림 == 1:
#         answer += str(올림)
        
#     answer = list(answer)
#     answer.reverse()
#     answer = ''.join(answer)
    
    return answer