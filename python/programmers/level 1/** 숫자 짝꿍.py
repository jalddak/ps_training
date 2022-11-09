def solution(X, Y):
    answer = ''
    X_check = set(list(X))
    Y_check = set(list(Y))
    
    intersection = X_check & Y_check
    intersection = list(intersection)
    intersection.sort(reverse=True)
    
    for num in intersection:
        X_cnt = X.count(num)
        Y_cnt = Y.count(num)
        cnt = 0
        if X_cnt < Y_cnt:
            cnt = X_cnt
        else:
            cnt = Y_cnt
        for _ in range(cnt):
            answer += num
    
    if len(answer) == 0:
        return '-1'
    if len(answer) == answer.count('0'):
        return '0'
    return answer

# 아래는 테스트하면서 여러 변형 주면서 풀어본 코드
# 결국은 처음생각인 위처럼 하는게 가장 속도가 빨랐다.
# 하지만 23번째 줄인 0이 여러개 걸려 00000 인지 확인하는 코드에서 단순하게 int(answer)를 갈겨버리는 바람에
# 엄청나게 긴 answer (300만자리까지 가능한 수) 에서는 시간초과가 난 것 같다.
# count가 문제인가 생각해봤는데 아니였고 그냥 int(answer) 이게 문제였다.

def solution(X, Y):
    answer = ''
    X_dict = {}
    for num in X:
        if num not in X_dict:
            X_dict[num] = 1
        else:
            X_dict[num] += 1
    Y_dict = {}
    for num in Y:
        if num not in Y_dict:
            Y_dict[num] = 1
        else:
            Y_dict[num] += 1
    
    intersection = list(set(list(X_dict.keys())) & set(list(Y_dict.keys())))
    intersection.sort(reverse=True)
    
    for num in intersection:
        X_cnt = X_dict[num]
        Y_cnt = Y_dict[num]
        cnt = 0
        if X_cnt < Y_cnt:
            cnt = X_cnt
        else:
            cnt = Y_cnt
        for _ in range(cnt):
            answer += num
            
    if len(answer) == 0:
        return '-1'
    if len(answer) == answer.count('0'):
        return '0'
    return answer