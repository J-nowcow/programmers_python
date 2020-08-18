# https://programmers.co.kr/learn/courses/30/lessons/42586
def solution(progresses, speeds):
    answer = []
    while len(progresses) > 0:
        while progresses[0] < 100:
            for i in range(len(progresses)):
                progresses[i] += speeds[i]
        tmp = 0
        while progresses[0] >=100:
            del progresses[0]; del speeds[0]; tmp+=1
            if len(speeds) == 0: break
        answer += [tmp]
        
    return answer

print(solution([93, 30, 55], [1, 30, 5]))
