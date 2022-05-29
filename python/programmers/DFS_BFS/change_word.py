def solution(begin, target, words):
    candidates = []
    candidates.append(begin)
    answer = 0
    answer = make_tree(candidates, words, target, answer)
    return answer

# BFS 사용
def make_tree(candidates, words, target, answer):
    if len(candidates) == 0:
        return 0
    answer += 1
    for candidate in candidates:
        next_candidates = []
        i = 0
        while i < len(words):
            same_alpha = 0
            for j in range(len(candidate)):
                if candidate[j] == words[i][j]:
                    same_alpha += 1
            if same_alpha == len(candidate) - 1:
                if words[i] == target:
                    return answer
                next_candidates.append(words[i])
                words.pop(i)
                i -= 1
            i += 1
    answer = make_tree(next_candidates, words, target, answer)
    return answer