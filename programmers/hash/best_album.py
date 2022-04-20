def solution(genres, plays):
    answer = []
    hash = {}
    number = 0
    for genre in genres:
        if genre in hash:
            hash[genre][0] = hash[genre][0] + plays[number]
            hash[genre].append(number)
        else:
            hash[genre] = [plays[number], number]
        number += 1
    hash2 = sorted(hash.items(), key=lambda x: x[1][0], reverse=True)
    music_lists = list(dict(hash2).values())
    # 여기까진 해시로 장르별 음악횟수 계산하여 그 순서대로 나타낸것, 그리고 해당 장르에 속한 음악고유번호로 리스트합침.
    for mlist in music_lists:
        mlist.pop(0)
    # 여기까진 그냥 총 음악횟수 지워버리는 것.
    select_music = []
    for mlist in music_lists:
        for music in mlist:
            for i in range(len(select_music)):
                if plays[music] > plays[select_music[i]]:
                    select_music.insert(i, music)
                    break
            if len(select_music) < 2:
                select_music.append(music)
            if len(select_music) > 2:
                select_music.pop()
        for music in select_music:
            answer.append(music)
        select_music = []
    return answer