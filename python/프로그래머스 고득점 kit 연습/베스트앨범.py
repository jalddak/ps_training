def solution(genres, plays):
    answer = []
    music = {}
    for i in range(len(genres)):
        if genres[i] not in music:
            music[genres[i]] = [plays[i], [i, plays[i]]]
        else:
            music[genres[i]][0] += plays[i]
            music[genres[i]].append([i, plays[i]])
            
    music = list(zip(list(music.keys()), list(music.values())))
    music.sort(key=lambda x:-x[1][0])
    
    for genre, play in music:
        need = play[1:]
        need.sort(key=lambda x:-x[1])
        cnt = min(len(need), 2)
        for i in range(cnt):
            answer.append(need[i][0])
            
    return answer