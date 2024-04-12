import sys
sys.setrecursionlimit(10**7)

def recursion(room_info, rn):
    if rn in room_info:
        room_info[rn] = recursion(room_info, room_info[rn])
    else:
        room_info[rn] = rn+1
    return room_info[rn]

def solution(k, room_number):
    answer = []
    room_info = {}
    for rn in room_number:
        recursion(room_info, rn)
        answer.append(room_info[rn]-1)
    return answer