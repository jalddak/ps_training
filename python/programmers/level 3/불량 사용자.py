def check_candidates(user_id, banned_id):
    candidates = {}
    for i in range(len(banned_id)):
        b = banned_id[i]
        if b in candidates:
            continue
        for j in range(len(user_id)):
            check = True
            u = user_id[j]
            if len(b) != len(u):
                continue
            for k in range(len(b)):
                if b[k] == '*':
                    continue
                if b[k] != u[k]:
                    check = False
                    break
            if check:
                candidates[b] = candidates.get(b, [])
                candidates[b].append(u)
    return candidates

def permutation(depth, banned_id, candidates, answer_list, result):
    if depth == len(banned_id):
        result = list(result)
        result.sort()
        result = tuple(result)
        answer_list.add(result)
        return
    
    b = banned_id[depth]
    for c in candidates[b]:
        if c in result:
            continue
        result.add(c)
        permutation(depth+1, banned_id, candidates, answer_list, result)
        result.remove(c)

def solution(user_id, banned_id):
    answer = 0
    candidates = check_candidates(user_id, banned_id)
    answer_list = set()
    permutation(0, banned_id, candidates, answer_list, set())
    
    answer = len(answer_list)
    return answer