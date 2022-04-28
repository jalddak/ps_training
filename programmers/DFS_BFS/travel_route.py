def solution(tickets):
    answer = []
    answer, tickets_left = route('ICN', tickets, answer)
    return answer

def route(start, tickets, answer):
    candidates = []
    tickets_copy = []
    tickets_left = len(tickets)
    for ticket in tickets:
        tickets_copy.append(ticket)
        if ticket[0] == start:
            candidates.append(ticket)
    
    if len(candidates) == 0:
        answer.pop()
        print(answer, tickets_left, 'asd')
        return answer, tickets_left
    
    candidates.sort(key = lambda x:x[1])
    for candidate in candidates:
        next_ticket = candidate
        tickets_copy.remove(next_ticket)
        answer.append(next_ticket[0])
        if len(tickets_copy) != 0:
            print("1", answer, tickets_left, next_ticket[1], candidate, next_ticket, candidates)
            answer, tickets_left = route(next_ticket[1], tickets_copy, answer)
            print("2", answer, tickets_left, next_ticket[1], candidate, next_ticket, candidates)
            if tickets_left != 0:
                tickets_copy.append(next_ticket)
                continue
        else:
            answer.append(next_ticket[1])
            tickets_left = len(tickets_copy)
            print("3", answer, tickets_left, next_ticket[1], candidate, next_ticket, candidates)
            return answer, tickets_left
        return answer, tickets_left
    answer.pop()
    return answer, tickets_left

solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])