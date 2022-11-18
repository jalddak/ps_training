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