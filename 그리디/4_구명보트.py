#https://programmers.co.kr/learn/courses/30/lessons/42885
"""
리미트에 최대한 가깝게 계속 뽑아주면 그게 최솟값임
사람 수가 50000명 이므로 O(n^2)로는 안되지만 상수 커팅 잘 해주면 돌아갈지도
한번에 최대 2명이므로 그냥 정렬해준 다음에 양쪽 끝 뽑아주면 O(nlogn) 되는듯
"""

def solution(people, limit):
    people.sort()
    answer = 0
    s, e = 0, len(people)-1 # 가장 가벼운 사람과 무거운 사람 찾기
    while s <= e: # 같아지면 한명 남은거니까 더 커질때까지 반복
        if people[s] + people[e] <= limit:
            s += 1 # 가벼운 사람 데리고 탈 수 있으면 같이 타고
        e -= 1; answer += 1 # 무거운 사람은 항상 한명씩 줄어듦
    return answer

people = [70,50,80,50]
limit = 100
print(solution(people, limit))
