def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    i = 0
    while i < len(people):
        if people[i] + people[-1] <= limit:
            people.pop()
        answer += 1
        i += 1
    return answer