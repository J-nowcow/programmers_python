#https://programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    d = {}
    answer = []
    for i, v in enumerate(genres):
        if v in d: d[v] += plays[i]
        else: d[v] = plays[i]
    rank = sorted(d.items(), key = lambda d:d[1], reverse = True)
    # rank: [('pop', 3100), ('classic', 1450)]

    
    for g, _ in rank:
        playlist = []
        for i in range(len(genres)):
            if g == genres[i]:
                playlist.append([plays[i],10000 - i])
        tmp = sorted(playlist, reverse = True)
        answer += [10000 - tmp[0][1]]
        if len(tmp) > 1: answer += [10000 - tmp[1][1]]

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 500, 500, 2500]))
