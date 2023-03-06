def solution(genres, plays):
    answer = []
    g_dict = {}
    for i in range(len(genres)):
        if genres[i] not in g_dict:
            g_dict[genres[i]] = [plays[i] , i]
        else:
            g_dict[genres[i]][0] += plays[i]
            first = g_dict[genres[i]][1]
            
            if len(g_dict[genres[i]]) > 2:
                second = g_dict[genres[i]][2]
                if plays[first] < plays[i]:
                    g_dict[genres[i]][1] = i
                    g_dict[genres[i]][2] = first
                elif plays[second] < plays[i]:
                    g_dict[genres[i]][2] = i
                    
            elif plays[first] < plays[i]:
                g_dict[genres[i]][1] = i
                g_dict[genres[i]].append(first)
                
            else:
                g_dict[genres[i]].append(i)
                
    s_list = list(sorted(g_dict.values(), key=lambda x:x[0], reverse=True))
    for l in s_list:
        answer.append(l[1])
        if len(l) > 2:
            answer.append(l[2])
    return answer