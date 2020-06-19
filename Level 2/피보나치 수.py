#https://programmers.co.kr/learn/courses/30/lessons/12945
def solution(n):
    a=0;b=1
    for i in range(n):a,b=b,(a+b)%1234567
    return a

print(solution(5))
