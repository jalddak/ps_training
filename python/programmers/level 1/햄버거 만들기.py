def solution(ingredient):
    answer = 0
    index = 0
    burger = []
    while index < len(ingredient):
        if ingredient[index] == 1:
            if len(burger) != 0 and burger[-1][-1] == 3:
                burger.pop()
                answer += 1
            else:
                burger.append([1])
        elif ingredient[index] == 2:
            if len(burger) != 0 and burger[-1][-1] == 1:
                burger[-1].append(2)
            elif len(burger) != 0:
                burger.clear()
        elif ingredient[index] == 3:
            if len(burger) != 0 and burger[-1][-1] == 2:
                burger[-1].append(3)
            elif len(burger) != 0:
                burger.clear()
        index += 1
    return answer