def solution(numbers, hand):
    L = [3, 0]
    R = [3, 2]
    answer = ''
    for num in numbers:
        num = num - 1
        row = num // 3
        col = num % 3
        if num == -1:
            row = 3
            col = 1
        if num+1 in [1, 4, 7]:
            answer += 'L'
            L = [row, col]
        elif num+1 in [3, 6, 9]:
            answer += 'R'
            R = [row, col]
            
        else:
            L_distance = abs(L[0]-row) + abs(L[1]-col)
            R_distance = abs(R[0]-row) + abs(R[1]-col)
            
            if L_distance < R_distance:
                answer += 'L'
                L = [row, col]
            elif L_distance > R_distance:
                answer += 'R'
                R = [row, col]
            else:
                if hand == 'left':
                    answer += 'L'
                    L = [row, col]
                else:
                    answer += 'R'
                    R = [row, col]
                    
            
    return answer