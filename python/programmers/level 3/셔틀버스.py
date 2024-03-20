def solution(n, t, m, timetable):
    answer = ''
    d = 540
    times = []
    for time in timetable:
        time = time.split(":")
        time = int(time[0]) * 60 + int(time[1])
        times.append(time)
    times.sort(reverse=True)
    
    minutes = 0
    while n > 0:
        bus = []
        while len(bus) < m and times and times[-1] <= d:
            bus.append(times.pop())
        if n == 1:
            if len(bus) == m:
                minutes = bus.pop() - 1
            else:
                minutes = d
        n -= 1
        d += t
    h, m = str(minutes//60) if (minutes//60)//10>0 else "0" + str(minutes//60), str(minutes%60) if (minutes%60)//10>0 else "0" + str(minutes%60)
    answer = h + ":" + m
    return answer