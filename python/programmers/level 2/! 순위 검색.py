def bs(sorted_list, score):
    l, r = 0, len(sorted_list)
    
    while l < r:
        mid = (l+r) // 2
        
        if sorted_list[mid] < score:
            l = mid + 1
        else:
            r = mid
            
    return len(sorted_list) - l

def solution(info, query):
    answer = []
    scores = [[[[[] for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(3)]
    lang_i = {"cpp":0, "java":1, "python":2}
    tech_i = {"backend":0, "frontend":1}
    career_i = {"junior":0, "senior":1}
    food_i = {"chicken":0, "pizza":1}
    
    for elements in info:
        lang, tech, career, food, score = elements.split()
        scores[lang_i[lang]][tech_i[tech]][career_i[career]][food_i[food]].append(int(score))
    
    for l in range(3):
        for t in range(2):
            for c in range(2):
                for f in range(2):
                    scores[l][t][c][f].sort()
    
    for check in query:
        lang, tech, career, foodScore = check.split(" and ")
        food, score = foodScore.split()
        score = int(score)
        cnt = 0
        
        lang_c = [0, 1, 2]
        tech_c = [0, 1]
        career_c = [0, 1]
        food_c = [0, 1]
        
        if lang in lang_i:
            lang_c = [lang_i[lang]]
        if tech in tech_i:
            tech_c = [tech_i[tech]]
        if career in career_i:
            career_c = [career_i[career]]
        if food in food_i:
            food_c = [food_i[food]]
            
        for l in lang_c:
            for t in tech_c:
                for c in career_c:
                    for f in food_c:
                        cnt += bs(scores[l][t][c][f], score)
        answer.append(cnt)
    return answer