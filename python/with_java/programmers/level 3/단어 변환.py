def can_change(current, word):
    flag = 0
    result = False
    for i in range(len(current)):
        if current[i] != word[i]:
            flag += 1
            if flag > 1:
                break
    if flag == 1:
        result = True
    return result


def solution(begin, target, words):
    candidates = [(begin, 0)]
    visited = [False for _ in range(len(words))]
    answer = 0
    while candidates:
        current, cnt = candidates.pop()
        if current == target:
            answer = cnt
            break
        for i in range(len(words)):
            if visited[i]:
                continue
            if can_change(current, words[i]):
                visited[i] = True
                candidates.append((words[i], cnt+1))
    return answer