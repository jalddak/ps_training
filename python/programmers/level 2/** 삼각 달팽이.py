# 틀을 걍 잡아주고 거의 완전탐색식으로 풀었다. n이 조금만 더 커져도 아마 터질듯.

def solution(n):
    answer = [[0 for _ in range(i)] for i in range(1,n+1)]
    개수 = 0
    for i in range(1, n+1):
        개수 += i
        
    layer = 0
    index = 0
    num = 1
    command = '아래로'
    while True:
        if command == '아래로' and layer != n-1:
            answer[layer][index] = num
            num += 1
            layer += 1
        elif command == '위로':
            if answer[layer][index] == 0:
                answer[layer][index] = num
                layer -= 1
                index -= 1
                num += 1
            else:
                layer += 2
                index += 1
                command = '아래로'
            
        else:
            if index <= len(answer[layer])-1 and answer[layer][index] == 0:
                answer[layer][index] = num
                num += 1
                index += 1
            else:
                n -= 1
                layer -= 1
                index -= 2
                command = '위로'
        
        if num == 개수 + 1:
            break
    result = []
    for a in answer:
        result += a
    
    return result