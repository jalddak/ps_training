def solution(files):
    answer = []
    array_files = []
    for file in files:
        head = ''
        number = ''
        tail = ''
        n_start = 0
        for i in range(len(file)):
            if file[i].isdigit() and n_start == 0:
                n_start = i
                head = file[0:i]
            elif n_start != 0:
                if not file[i].isdigit():
                    number = file[n_start:i]
                    tail = file[i:]
                    break
                elif i-n_start == 5:
                    number = file[n_start:i]
                    tail = file[i:]
                    break
            if len(file)-1 == i:
                number = file[n_start:]
                
                
        array_file = [head, number, tail]
        array_files.append(array_file)
    array_files.sort(key=lambda x:(x[0].lower(), int(x[1])))
    for file in array_files:
        answer.append(''.join(file))
            
    return answer