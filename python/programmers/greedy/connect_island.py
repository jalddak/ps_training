costs = [[0, 1, 1], [3, 4, 1], [1, 2, 2], [2, 3, 4]]
n = 5

def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    index = 0
    connect_set_list = []
    while index < len(costs):
        temp_set = set([costs[index][0], costs[index][1]])
        if index == 0:
            connect_set_list.append(temp_set)
            answer += costs[index][2]
            index += 1
            continue
        
        save_index = []
        for csl_index in range(len(connect_set_list)):
            if len(connect_set_list[csl_index] & temp_set) == 0:
                if csl_index == len(connect_set_list)-1 and len(save_index) == 0:
                    connect_set_list.append(temp_set)
                    answer += costs[index][2]
                continue
            elif len(connect_set_list[csl_index] & temp_set) == 1:
                if len(save_index) == 0:
                    connect_set_list[csl_index] = connect_set_list[csl_index] | temp_set
                    answer += costs[index][2]
                save_index.append(csl_index)
                continue
            elif len(connect_set_list[csl_index] & temp_set) == 2:
                break

        if len(save_index) == 2:
            connect_set_list[save_index[0]] = connect_set_list[save_index[0]] | connect_set_list[save_index[1]]
            connect_set_list.pop(save_index[1])
        save_index.clear()
        print (answer, connect_set_list)
        index += 1
    return answer

solution(n, costs)

# 다른사람들은 크루스칼알고리즘 이라는것을 사용함. 근데 찾아보니 내가 생각한거랑 비슷한 맥락인듯.