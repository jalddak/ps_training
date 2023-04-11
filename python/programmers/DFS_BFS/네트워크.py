def solution(n, computers):
    answer = 0
    networks = []
    for i in range(n):
        network = []
        union_check = 0
        union_index = []
        for j in range(n):
            if computers[i][j] == 1:
                network.append(j)
                for k in range(len(networks)):
                    if j in networks[k] and k not in union_index:
                        union_check = 1
                        union_index.append(k)
        union_index.sort()
        if union_check == 0:
            networks.append(network)
        else:
            for i in range(len(union_index)):
                network += networks.pop(union_index[i]-i)
            networks.append(list(set(network)))
    answer = len(networks)
    return answer