# https://programmers.co.kr/learn/courses/30/lessons/12914
""" 피보나치와 동일함 """
def solution(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return b%1234567
print(solution(4))
