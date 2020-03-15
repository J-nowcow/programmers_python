# https://programmers.co.kr/learn/courses/30/lessons/42578
"""
스파이가 가진 서로 다른 옷의 조합의 수 return 하는 문제
의상의 수가 30개 이하니까 대충 막 짜도 됨
딕셔너리로 종류별로 몇개인지 저장해서 sum(x+1) - 1 하면 됨
"""
from functools import reduce
# reduce 함수
"""
def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value

iterable의 요소들을 function의 대입하여 하나의 결과값이 나올 때까지 반복함
initializer을 주면 초기값을 설정해줄 수 있음
"""
def solution(clothes):
    d = {}
    for a,b in clothes:
        if b in d: d[b]+=1
        else: d[b] = 2
    return reduce(lambda x,y: x*y, list(d.values())) - 1



print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
