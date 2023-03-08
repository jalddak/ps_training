from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    truck_num = len(truck_weights)
    complete = 0
    ing_weight = 0
    ing = deque([])
    
    while complete != truck_num:
        answer += 1
        if len(truck_weights) != 0:
            if weight >= ing_weight + truck_weights[0]:
                truck_weight = truck_weights.popleft()
                ing_weight += truck_weight
                ing.append([truck_weight, 0])
        for i in range(len(ing)):
            ing[i][1] += 1
        if ing[0][1] == bridge_length:
            end_truck = ing.popleft()
            ing_weight -= end_truck[0]
            complete += 1
    return answer + 1