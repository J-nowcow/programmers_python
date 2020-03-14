import heapq as hq

def solution(jobs):
    hq.heapify(jobs)
    n = len(jobs)
    time = 0
    ajobs = []
    answer = 0
    while jobs:
        tjobs = []
        while jobs:
            if jobs[0][0] <= time: tjobs.append(hq.heappop(jobs))
            else: break
        tjobs = [[b,a] for a,b in tjobs]
        ajobs += tjobs
        
        if ajobs:
            ajobs.sort(reverse = True)
            tmp = ajobs.pop()
            time += tmp[0]
            answer += (time - tmp[1]) # 처리된 시간에서 입력된 시간 뺀 값
        else: time+=1
        
    while ajobs:
        tmp = ajobs.pop()
        time += tmp[0]
        answer += (time - tmp[1])
            
    return answer//n

jobs = [[0, 3], [1, 9], [2, 6]]

print(solution(jobs))
