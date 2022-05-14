# 왜 인지는 모르나 백준 채점 프로그램에서 초반에 매우 느리게 챗점됨. 하지만 시간초과는 아님.

from itertools import combinations

def synergy_difference(synerge, s_team, l_team):
    s_team_synergy = 0
    for i in range(len(s_team)):
        for j in range(i+1, len(s_team)):
            s_team_synergy += (synerge[s_team[i]][s_team[j]] + synerge[s_team[j]][s_team[i]])
    l_team_synergy = 0
    for i in range(len(l_team)):
        for j in range(i+1, len(l_team)):
            l_team_synergy += (synerge[l_team[i]][l_team[j]] + synerge[l_team[j]][l_team[i]])
    
    result = s_team_synergy - l_team_synergy
    if s_team_synergy < l_team_synergy:
        result = -result

    return result
    

def main():
    N = int(input())
    minimum = 0
    synergy = [[0 for _ in range(N)] for _ in range(N)]
    human = []
    for i in range(N):
        synergy_row = list(map(int, input().split()))
        human.append(i)
        for j in range(N):
            synergy[i][j] = synergy_row[j]
            minimum += synergy_row[j]
    
    half_human = list(map(set, list(combinations(human, N//2))))
    while len(half_human) != 0:
        s_team = half_human.pop()
        l_team = []
        for i in range(len(half_human)):
            if s_team & half_human[i] == set():
                l_team = list(half_human.pop(i))
                s_team = list(s_team)
                minimum = min(minimum, synergy_difference(synergy, s_team, l_team))
                break
    print(minimum)
    return minimum


if __name__ == '__main__':
    main()