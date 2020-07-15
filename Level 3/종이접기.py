# https://programmers.co.kr/learn/courses/30/lessons/62049
"""
가운데 0 기준으로 왼쪽은 그대로, 오른쪽은 대칭이니까 반대로
"""
def solution(n):
    a = [0]
    for i in range(n-1):
        a = a + [0] + [1-i for i in a[::-1]]
    return a

print(solution(3))
