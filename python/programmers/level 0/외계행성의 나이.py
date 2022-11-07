def solution(age):
    agelist = []
    answer = ''
    while age >= 10:
        agelist.append(age%10)
        age = age // 10
    agelist.append(age)
    agelist.reverse()
    
    for num in agelist:
        answer += chr(num + 97)
    
    return answer