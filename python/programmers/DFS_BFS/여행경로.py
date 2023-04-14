def solution(tickets):
    answer = ["ICN"]
    answer = dfs(tickets, answer)
                
    return answer

def dfs(tickets, answer):
    if len(tickets) == 0:
        return answer
    candidates = []
    i = 0
    while i < len(tickets):
        if tickets[i][0] == answer[-1]:
            candidates.append([tickets[i][1], i])
        i += 1
    
    if len(candidates) == 0:
        return -1
    candidates.sort(key=lambda x:x[0])
    for j in range(len(candidates)):
        index = candidates[j][1]
        c_answer = answer + [candidates[j][0]]
        c_tickets = tickets[0:index] + tickets[index+1:]
        result = dfs(c_tickets, c_answer)
        if result != -1:
            break
    return result