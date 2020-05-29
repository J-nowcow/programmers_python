# https://programmers.co.kr/learn/courses/30/lessons/62048
"""
가로와 세로의 공약수 계산하기
그 공약수마다 사각형 w//g + h//g - 1개 잘라짐
-> 총 사각형 w+h-g개 잘라짐
"""
def solution(w,h):
    a, b= max(w,h), min(w,h)
    while b: a,b = b,a%b
    return w*h - w - h + a
print(solution(8,12))
