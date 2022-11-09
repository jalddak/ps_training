def solution(babbling):
    answer = 0
    speaks = [ "aya", "ye", "woo", "ma" ]
    before = len(speaks)
    for word in babbling:
        before = ''
        stop = False
        while len(word) != 0 and not stop:
            stop = True
            for speak in speaks:
                if speak == before:
                    continue
                if word[:len(speak)] == speak:
                    word = word[len(speak):]
                    before = speak
                    stop = False
                    break
        if len(word) == 0:
            answer += 1
                
    return answer