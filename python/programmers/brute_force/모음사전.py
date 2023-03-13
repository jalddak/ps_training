def solution(word):
    answer = 0
    test = []
    
    while True:
        answer += 1
        if len(test) != 5:
            test.append('A')
        else:
            for i in range(4, -1, -1):
                if test[i] == 'A':
                    test[i] = 'E'
                elif test[i] == 'E':
                    test[i] = 'I'
                elif test[i] == 'I':
                    test[i] = 'O'
                elif test[i] == 'O':
                    test[i] = 'U'
                elif test[i] == 'U':
                    test.pop()
                    continue
                break
                
        
        if ''.join(test) == word:
            return answer