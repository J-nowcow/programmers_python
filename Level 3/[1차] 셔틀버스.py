#https://programmers.co.kr/learn/courses/30/lessons/17678
"""
timetable 정렬한 다음에 각 셔틀에 어디까지 타는지 계산해서 answer 계속 업데이트
"""
def solution(n, t, m, timetable):
    # timetable 분단위 int값으로 바꾸고 정렬해준다.
    timetable = sorted([int(a.split(":")[0])*60 + int(a.split(":")[1]) for a in timetable])
    
    idx = 0
    answer = 0
    for i in range(n):
        now = 540 + t * i # 현재 시간
        for j in range(m):
            # 더이상 타야 될 사람 없으면 마지막 버스 오는 시간에 나간다.
            if idx == len(timetable):
                answer = now
                break
            # 사람이 또 탈 수 있다면 방금 탄 사람보다 1분 먼저 오면 탈 수 있다.
            if timetable[idx] <= now:
                idx += 1
                answer = timetable[idx-1] - 1
            # 더이상 못타고 자리가 남았다면 버스 오는 시간에 나가면 된다.
            else: 
                answer = now
    return "%02d:%02d"%(answer//60, answer%60)

n = 1
t = 1
m = 5
timetable = ["08:00", "08:01", "08:02", "08:03"]
print(solution(n,t,m,timetable))
