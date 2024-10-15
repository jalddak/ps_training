def solution(skill, skill_trees):
    answer = 0
    d = {}
    
    for i in range(1, len(skill)):
        d[skill[i]] = skill[i-1]
    
    for st in skill_trees:
        already = set()
        flag = True
        for s in st:
            if (s in d and d[s] in already) or s not in d:
                already.add(s)
                continue
            flag = False
            break
        if flag:
            answer += 1
                
    return answer

# 이전에 풀었던 방식. 방법이 나쁘지않음
def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        skill_copy = skill
        for s in skill_tree:
            if s in skill_copy:
                if s != skill_copy[0]:
                    answer -= 1
                    break
                else:
                    skill_copy = skill_copy[1:]
        answer += 1
    return answer