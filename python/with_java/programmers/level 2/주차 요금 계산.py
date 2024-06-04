def solution(fees, records):
    inInfo = {}
    timeInfo = {}
    for record in records:
        time, num, cmd = record.split()
        time = list(map(int, time.split(":")))
        time = time[0] * 60 + time[1]
        if cmd == "IN":
            inInfo[num] = time
        else:
            timeInfo[num] = timeInfo.get(num, 0) + time - inInfo[num]
            del inInfo[num]
    for num in inInfo:
        timeInfo[num] = timeInfo.get(num, 0) + 23 * 60 + 59 - inInfo[num]
    
    timeInfo = sorted(list(timeInfo.items()), key=lambda x:x[0])
    answer = [fees[1] for _ in range(len(timeInfo))]
    for i in range(len(timeInfo)):
        num, time = timeInfo[i]
        if time < fees[0]:
            continue
        time -= fees[0]
        per = 0
        if time % fees[2] != 0:
            per += 1
        per += time // fees[2]
        answer[i] += per * fees[3]
    
    return answer