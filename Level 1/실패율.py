#https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    d = {} # 스테이지별 머무르고 있는 사람
    for i in stages:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    t = len(stages)
    d = sorted(d.items()) 
    f = {} # 실패한 사람 비율
    for i in d:
        f[i[0]] = i[1] / t
        t -= i[1]
    for i in range(1,N+1): # 실패율 0인 값 추가해주기
        if i not in f:
            f[i] = 0
    if N+1 in f: f.pop(N+1) # 가장 큰 값 있으면 제거
    f = sorted(f.items(), key = lambda x: (x[1], -x[0]), reverse = True)
    
    return [i[0] for i in f]

N = 4
stages = [4,4,4,4,4]
print(solution(N,stages))
