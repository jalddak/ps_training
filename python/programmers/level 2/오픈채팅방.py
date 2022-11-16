def solution(record):
    answer = []
    users = {}
    for cmd in record:
        cmd = cmd.split()
        if len(cmd) == 3:
            users[cmd[1]] = cmd[2]
    for cmd in record:
        cmd = cmd.split()
        message = users[cmd[1]] + "님이"
        if cmd[0] == 'Enter':
            message += " 들어왔습니다."
            answer.append(message)
        elif cmd[0] == 'Leave':
            message += " 나갔습니다."
            answer.append(message)
                
    return answer