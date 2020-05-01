#https://programmers.co.kr/learn/courses/30/lessons/12934

def solution(n):
    if n ** 0.5 == int(n ** 0.5):
        return int((n**0.5+1)**2)
    return -1

print(solution(121))
