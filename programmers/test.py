def solution(arrows):
    answer = 0
    start = (0, 0)
    answer = draw(start, arrows, answer)
    print(answer)
    return answer

def draw(start, arrows, answer):
    present_node = start
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]
    node_dict = {present_node : []}
    for arrow in arrows:
        next_node = (present_node[0] + dx[arrow], present_node[1] + dy[arrow])
        if next_node not in node_dict:
            node_dict[next_node] = [present_node]
            node_dict[present_node].append(next_node)
            if arrow in [1,3,5,7]:
                cross_x = (present_node[0] + dx[arrow], present_node[1])
                cross_y = (present_node[0], present_node[1] + dy[arrow])
                if cross_x in node_dict:
                    if cross_y in node_dict[cross_x]:
                        answer += 1
        else:
            if present_node not in node_dict[next_node]:
                node_dict[next_node].append(present_node)
                node_dict[present_node].append(next_node)
                answer += 1
                if arrow in [1,3,5,7]:
                    cross_x = (present_node[0] + dx[arrow], present_node[1])
                    cross_y = (present_node[0], present_node[1] + dy[arrow])
                    if cross_x in node_dict:
                        if cross_y in node_dict[cross_x]:
                            answer += 1
        present_node = next_node
    return answer

solution([6, 0, 3, 0, 5, 2, 6, 0, 3, 0, 5])