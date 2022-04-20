numbers = [9, 99, 998]

# def solution(numbers):
#     answer = ''
#     temp = ''
#     index_list = []
#     number_list = []
#     recursion(numbers, temp, index_list, number_list)
#     number_list.sort()
#     bigest_num = number_list.pop()
#     answer += str(bigest_num)
#     print(answer)
#     return answer

# def recursion(numbers, temp, index_list, number_list):
#     for i in range(len(numbers)):
#         if i in index_list:
#             continue
#         else:
#             index_list.append(i)
#             temp2 = temp + str(numbers[i])
#             if len(index_list) == len(numbers):
#                 number_list.append(int(temp2))
#             else:
#                 recursion(numbers, temp2, index_list, number_list)
#             index_list.pop()

# def solution(numbers):
#     answer = ''
#     str_numbers = []
#     for number in numbers:
#         str_numbers.append(str(number))
#     str_numbers.sort(reverse = True)
#     i = 0
#     while i < len(str_numbers):
#         if i != len(str_numbers) -1:
#             if len(str_numbers[i]) > len(str_numbers[i+1]):
#                 if str_numbers[i][0:len(str_numbers[i+1])] == str_numbers[i+1]:

#                     temp_num1 = str_numbers[i] * 2
#                     temp_num2 = str_numbers[i+1] * 8
#                     temp_num2 = temp_num2[0:len(temp_num1)]
#                     if int(temp_num1) < int(temp_num2):
#                         pop = str_numbers.pop(i)
#                         str_numbers.insert(i+1, pop)
#                         if i >= 1:
#                             i -= 2
#         i += 1
#     for number in str_numbers:
#         answer += number
#     if str_numbers[0] == '0':
#         answer = int(answer)
#         answer = str(answer)
#     return answer

def solution(numbers):
    answer = ''
    str_numbers = []
    for number in numbers:
        multi_three_number_str = str(number) * 4
        str_numbers.append(multi_three_number_str)
    str_numbers.sort(reverse = True)
    for number in str_numbers:
        answer += number[0:len(number)//4]
    if answer[0] == '0':
        return '0'
    return answer

solution(numbers)