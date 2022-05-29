def solution(bridge_length, weight, truck_weights):
    answer = 0
    ing = []
    ing_weight = 0
    end = []
    while len(truck_weights) != 0 or len(ing) != 0:
        end_truck = 0
        for truck in ing:
            truck[1] += 1
            if truck[1] > bridge_length:
                end_truck = 1
                end.append(ing[0])
                ing_weight -= ing[0][0]
        if end_truck == 1:
            ing.pop(0)
        if len(truck_weights) > 0:
            wait = truck_weights.pop(0)
            if ing_weight + wait <= weight:
                ing.append([wait,1])
                ing_weight = ing_weight + wait
            else:
                truck_weights.insert(0,wait)
        answer += 1
    return answer