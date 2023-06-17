def solution(today, terms, privacies):
    answer = []
    today = list(map(int,today.split('.')))
    
    dic_terms = {}
    for i in range(len(terms)):
        term = terms[i].split()
        dic_terms[term[0]] = int(term[1])
        
    for i in range(len(privacies)):
        privacie = privacies[i].split()
        date = list(map(int, privacie[0].split('.')))
        date[2] -= 1
        if date[2] == 0:
            date[2] = 28
            date[1] -= 1
        date[1] += dic_terms[privacie[1]]%12
        if date[1] > 12:
            date[1] -= 12
            date[0] += 1
        date[0] += dic_terms[privacie[1]]//12
        if date[0] < today[0]:
            answer.append(i+1)
        elif date[0] == today[0] and date[1] < today[1]:
            answer.append(i+1)
        elif date[0] == today[0] and date[1] == today[1] and date[2] < today[2]:
            answer.append(i+1)
    return answer