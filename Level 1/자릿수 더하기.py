#https://programmers.co.kr/learn/courses/30/lessons/12931

def solution(n):
    a = 0
    while n:
        a += n%10; n//=10
    return a

print(solution(123))
