from collections import deque

people = [70, 50, 80, 50]
limit = 100

def solution(people, limit):
    answer = 0
    people.sort(reverse = True)
    people = deque(people)
    while len(people) != 0:
        present = people.popleft()
        while present < limit and len(people) > 0:
            if present + people[len(people)-1] <= limit:
                present += people.pop()
            else:
                break
        answer += 1
        print(answer, people)
    return answer

solution(people, limit)