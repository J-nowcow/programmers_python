#https://programmers.co.kr/learn/courses/30/lessons/12943

def solution(num):
    a = 0
    while num-1: # num이 1 이상일 때
        if num&1: num = num*3+1 #비트연산: 홀수면 True 짝수면 False
        else: num //= 2
        a+=1
        if a==500: return -1
    return a

print(solution(6))
