#https://programmers.co.kr/learn/courses/30/lessons/12953
"""
소인수분해해서 딕셔너리에서 찾아주기
"""

def solution(arr):
    answer = {}
    for i in arr: # 각 원소 소인수분해
        if i==1: continue # 1은 소인수 없음
        d = {}; t = 2
        while t <= i:
            if i % t == 0:
                if t in d: d[t] += 1
                else: d[t] = 1
                i //= t
            else: t += 1
        for prime in d: # 딕셔너리에 값 추가
            if prime in answer:
                answer[prime] = max(answer[prime], d[prime])
            else:
                answer[prime] = d[prime]
    a = 1
    for i in list(answer.items()):
        a *= (i[0] ** i[1])
    return a

arr = [2,6,8,14]
print(solution(arr))
