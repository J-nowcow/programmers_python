# https://programmers.co.kr/learn/courses/30/lessons/12920
"""
처리하는데 걸리는 총 시간 먼저 찾아주기
전체 걸리는 시간 10000 * n // len(cores) + 1 이하니까
최댓값 저렇게 잡아주고 시간에 대해 이진탐색
(time까지 몇 개의 연산이 시작됐는지 찾아주기)

시간 찾고 나면
각 코어에 대해 time - 1초까지 몇개의 코어 찾는지 연산해주기
그 다음 남은 양에 대해 time 초에 새 작업 시작하는 코어 탐색
"""
def solution(n,cores):
    answer = 0
    begin = 0; end = 10000 * n // len(cores) + 1
    while begin <= end:
        mid = (begin+end) // 2
        s = 0
        for i in cores:
            s += mid // i + 1
        if s >= n: # 이 시간 안에는 충분한 작업이 시작됐다면
            end = mid - 1
        else:
            begin = mid + 1
    time = begin - 1
    amount = 0
    for i in cores:
        amount += time // i + 1

    for i in range(len(cores)):
        if (time+1) % cores[i] == 0:
            amount += 1
            if amount == n:
                return i + 1
    

print(solution(6,[1,2,3]))
