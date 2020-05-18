#https://programmers.co.kr/learn/courses/30/lessons/17680
"""
리스트 하나 만들어서 캐시 크기만큼 채워주기
이진트리로 짜면 log n으로 되겠지만 cachesize 최대가 30이라 굳이
"""
def solution(cacheSize, cities):
    answer = 0
    cities = [i.lower() for i in cities]
    cash = []
    for i in cities:
        if i in cash:
            cash.remove(i)
            answer += 1
        else: answer += 5
        # 캐시 업데이트
        cash.append(i)
        if len(cash) > cacheSize:
            cash.pop(0)
    return answer

cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
cacheSize = 3

print(solution(cacheSize, cities))
