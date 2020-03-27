#https://programmers.co.kr/learn/courses/30/lessons/43104
"""
그냥 피보나치 돌려서 2(Fn + Fn-1) 출력하면 끝나는 문제...
이 왜 Level 3
"""

def solution(N):
    a,b = 0,1
    for i in range(N): a,b = b,a+b
    return 2*(a+b)


print(solution(1))
