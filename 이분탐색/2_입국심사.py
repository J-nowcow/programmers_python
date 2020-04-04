#https://programmers.co.kr/learn/courses/30/lessons/43238
"""
사람 10억명, 심사 10억분
심사관 10만 명 이하
심사 시간 이진탐색 해주자

"""
def solution(n, times):
    begin = 0; end = 10**18 # 10억명, 10억분 -> 최대 10^18분 소요
    while begin <= end:
        mid = (begin+end)//2
        t = 0
        for i in times: t += mid // i # 각 심사대에서 심사받는 사람의 수
        if t < n: # 시간이 부족하다면
            begin = mid + 1
        else:
            end = mid - 1

    return begin

n = 6
times = [7,10]
print(solution(n,times))
