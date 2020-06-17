#https://programmers.co.kr/learn/courses/30/lessons/12941
"""
재배열 부등식: 가장 큰거랑 가장 작은거끼리 곱해주는게 합이 가장 작게 나옴
"""
def solution(A,B):
    A.sort(); B.sort(reverse = True)
    return sum(a*b for a,b in zip(A,B))

A = [1,4,2]
B = [5,4,4]
print(solution(A,B))
