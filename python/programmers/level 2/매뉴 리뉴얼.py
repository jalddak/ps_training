from itertools import combinations

def solution(orders, course):
    menus = {}
    for i in range(len(orders)-1):
        for j in range(i+1, len(orders)):
            first = set(orders[i])
            second = set(orders[j])
            intersection = list(first & second)
            if len(intersection) >= 2:
                menu_list = []
                for k in range(2, len(intersection) + 1):
                    menu_list += list(combinations(intersection, k))
                for menu in menu_list:
                    menu = list(menu)
                    menu.sort()
                    menu = ''.join(menu)
                    if menu not in menus:
                        menus[menu] = [i, j]
                    elif j not in menus[menu]:
                        menus[menu].append(j)
    most = {}
    for menu in menus:
        if len(menu) in course:
            if len(menu) not in most:
                most[len(menu)] = [0, []]
            num = most[len(menu)][0]
            length = len(menus[menu])
            if length > num:
                most[len(menu)][0] = length
                most[len(menu)][1] = [menu]
            elif length == num:
                most[len(menu)][1].append(menu)
    
    answer = []
    for key in most:
        answer += most[key][1]
    answer.sort()
    return answer