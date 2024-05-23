d = {'A':'E', 'E':'I', 'I':'O', 'O':'U'}

def solution(word):
    answer = 0
    current = []
    while ''.join(current) != word:
        answer += 1
        if len(current) != 5:
            current.append('A')
            continue
        temp = current.pop()
        while temp == 'U':
            temp = current.pop()
        current.append(d[temp])
    return answer