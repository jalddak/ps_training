numbers = "011"

def solution(numbers):
    answer = 0
    temp = ''
    index_list = []
    number_list = []
    recursion(numbers, temp, index_list, number_list)
    number_list = list(set(number_list))
    i = 0
    while i < len(number_list):
        if number_list[i] == 0 or number_list[i] == 1:
            number_list.remove(number_list[i])
            i -= 1
        else:
            for j in range(2, number_list[i]):
                if number_list[i]%j == 0:
                    number_list.remove(number_list[i])
                    i -= 1
                    break
        i += 1
    answer = len(number_list)
    print(answer)
    return answer

def recursion(numbers, temp, index_list, number_list):
    for i in range(len(numbers)):
        if i in index_list:
            continue
        else:
            index_list.append(i)
            temp2 = temp + numbers[i]
            number_list.append(int(temp2))
            if len(index_list) == len(numbers):
                index_list.pop()
                continue
            else:
                recursion(numbers, temp2, index_list, number_list)
            index_list.pop()

solution(numbers)