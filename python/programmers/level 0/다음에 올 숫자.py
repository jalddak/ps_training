def solution(common):
    for index in range(len(common)-2):
        if common[index+2] - common[index+1] != common[index+1] - common[index]:
            return common[len(common)-1] * (common[index+1] / common[index])
        else:
            return common[len(common)-1] + (common[index+1] - common[index])