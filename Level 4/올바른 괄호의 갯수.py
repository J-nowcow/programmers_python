# https://programmers.co.kr/learn/courses/30/lessons/12929
"""
n번째 카탈란 수: 2nCn / (n+1)
"""
def solution(n):
    a=1
    for i in range(1,n+1):
        a*=((n+i)/i)
    return round(a/(n+1))

print(solution(5))
