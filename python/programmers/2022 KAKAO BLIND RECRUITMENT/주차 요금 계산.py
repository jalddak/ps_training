import math

def solution(fees, records):
    answer = []
    records_in = {}
    records_stay = {}
    for record in records:
        record = record.split()
        
        time = record[0]
        time = time.split(':')
        time = int(time[0]) * 60 + int(time[1])
        
        if record[2] == 'IN':
            records_in[record[1]] = time
        elif record[2] == 'OUT':
            in_time = records_in[record[1]]
            del records_in[record[1]]
            stay_time = time - in_time
            if record[1] not in records_stay:
                records_stay[record[1]] = stay_time
            else:
                records_stay[record[1]] += stay_time
    
    for remain_car in records_in:
        time = 23 * 60 + 59
        in_time = records_in[remain_car]
        stay_time = time - in_time
        if remain_car not in records_stay:
            records_stay[remain_car] = stay_time
        else:
            records_stay[remain_car] += stay_time
    
    for car in records_stay:
        records_stay[car] -= fees[0]
        if records_stay[car] < 0:
            records_stay[car] = 0
            
    records_stay = sorted(records_stay.items())
    
    for record in records_stay:
        answer.append(fees[1] + math.ceil(record[1] / fees[2]) * fees[3])
        
    return answer