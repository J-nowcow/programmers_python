# https://programmers.co.kr/learn/courses/30/lessons/42587
def solution(priorities, location):
    d = {}
    for i in priorities:
        if i in d: d[i] += 1
        else: d[i] = 1
    answer = 0
    while True:
        a = max(d)
        for i in range(len(priorities)):
            if priorities[i] == a:
                priorities[i] = -1
                d[a] -= 1
                answer += 1
                if i == location: return answer
                if d[a] == 0: del d[a]; a = max(d)

print(solution([1, 1, 1, 1, 1, 1],0))
