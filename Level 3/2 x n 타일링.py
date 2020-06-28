# https://programmers.co.kr/learn/courses/30/lessons/12900
"""
2xn 타일링: 피보나치 수열과 동일함
"""
def solution(n):
    a,b=0,1
    for i in range(n):
        a,b=b,a+b
    return b%1000000007

print(solution(5))
