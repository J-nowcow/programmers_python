# https://programmers.co.kr/learn/courses/30/lessons/12979
"""
두 station 사이 거리 - 2w 만큼을 커버해야 함
(dist - 2w -1)//(2w+1) +1 개 필요
"""
def solution(n, stations, w):
    answer = 0
    stations = [-w] + stations + [n+w+1]
    for i in range(1,len(stations)):
        dist = stations[i] - stations[i-1] - 1
        answer += (dist - 2*w - 1) // (w*2 +1) + 1
        print(dist-2*w, answer)
    return answer

print(solution(16,[9],2))
