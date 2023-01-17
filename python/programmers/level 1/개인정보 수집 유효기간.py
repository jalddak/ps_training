def solution(today, terms, privacies):
    answer = []
    today = today.split('.')
    today = list(map(int, today))
    
    d_terms = {}
    for term in terms:
        term = term.split()
        d_terms[term[0]] = int(term[1])
    
    index = 0
    for p in privacies:
        index += 1
        p = p.split()
        p[0] = list(map(int, p[0].split('.')))
        p[0][2] -= 1
        p[0][0] += d_terms[p[1]] // 12
        p[0][1] += d_terms[p[1]] % 12
        if p[0][1] > 12:
            p[0][1] -= 12
            p[0][0] += 1
            
        if p[0][0] < today[0]:
            answer.append(index)
        elif p[0][0] == today[0] and p[0][1] < today[1]:
            answer.append(index)
        elif p[0][0] == today[0] and p[0][1] == today[1] and p[0][2] < today[2]:
            answer.append(index)
            
        
        
    return answer