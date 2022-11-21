def solution(want, number, discount):
    answer = 0
    for i in range(10, len(discount) + 1):
        start = i - 10
        check = True
        for j in range(len(want)):
            if discount[start:i].count(want[j]) < number[j]:
                check = False
                break
        if check:
            answer += 1
                
    return answer

    # array 에 count(매개변수)라는 메소드를 사용할 수 있었음