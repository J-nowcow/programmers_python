#https://programmers.co.kr/learn/courses/30/lessons/42884
"""
자동차 10000대니까 n^2도 커팅 잘 하면 가능할듯
가장 먼저 나오는 순서대로 정렬한 다음 하나씩 배정해주는 방식으로 하면 될 것 같음

들어오는 시점이 가장 빠른 순서대로 정렬
가장 마지막 감시카메라의 위치 check로 받아줌

세가지 경우 가능
start <= check <= end : 아무것도 안해도 됨
check < start : check를 end 위치로 바꿔주고 카메라 1대 추가
end < check : check를 end 위치로 바꿔주되 카메라는 추가 x
"""

def solution(routes):
    routes.sort()
    check = routes[0][1]
    answer = 1
    
    for start, end in routes: # 시작 지점, 끝 지점
        if check < start:
            answer += 1; check = end
        elif end < check:
            check = end
    return answer

routes = [[-20,15], [-14,-5], [-18,-13], [-5,-3]]
print(solution(routes))
