import heapq as hq
def solution(jobs):
    jobs = [[a[1],a[0]] for a in jobs]
    answer = 0
    hq.heapify(jobs)
    n = len(jobs)
    time = 0 # 마지막 작업이 끝난 시간
    
    while jobs:
        a = hq.heappop(jobs)
        if time <= a[1]:
            time = sum(a); answer += a[0]
        else:
            time += a[0]; answer += (time - a[1])
    return answer//n



jobs = [[0, 3], [1, 9], [2, 6]]

print(solution(jobs))
