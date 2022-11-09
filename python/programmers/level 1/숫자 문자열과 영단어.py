def solution(s):
    answer = 0
    numlist = ['0','1','2','3','4','5','6','7','8','9']
    strlist = ['zero','one','two','three','four','five','six','seven','eight','nine']
    while not s.isdigit():
        for index in range(len(numlist)):
            s = s.replace(strlist[index], numlist[index])
            if s.isdigit():
                return int(s)
        
    return int(s)