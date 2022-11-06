def solution(id_list, report, k):
    answer = []
    info_dict = {}
    stop_list = []
    for id in id_list:
        info_dict[id] = {'cnt':0, 'report':[]}
        
    for r in report:
        r = r.split()
        if r[1] not in info_dict[r[0]]['report']:
            info_dict[r[0]]['report'].append(r[1])
            info_dict[r[1]]['cnt'] += 1
        if info_dict[r[1]]['cnt'] >= k:
            if r[1] not in stop_list:
                stop_list.append(r[1])
            
    for id in id_list:
        result = 0
        for r_id in info_dict[id]['report']:
            if r_id in stop_list:
                result += 1
        answer.append(result)
    return answer