#https://programmers.co.kr/learn/courses/30/lessons/42862
"""
여분 있을 때마다 하나씩 배정해주기
"""
def solution(n, lost, reserve):
    for i in range(1,n+1):
        if i in lost and i in reserve:
            lost.remove(i); reserve.remove(i)
    for i in range(1,n+1):
        if i in reserve:
            if i-1 in lost: lost.remove(i-1);
            elif i+1 in lost: lost.remove(i+1)
    return n-len(lost)

n = 5; lost = [2,4]; reserve = [1,3,5]
print(solution(n,lost,reserve))
