def solution(chicken):
    service = [chicken // 10, chicken % 10]
    answer = service[0]
    answer += (service[0] + service[1]) // 10
    while True:
        service = [(service[0] + service[1]) // 10, (service[0] + service[1]) % 10]
        if (service[0] + service[1]) // 10 == 0:
            break
        answer += (service[0] + service[1]) // 10
    return answer