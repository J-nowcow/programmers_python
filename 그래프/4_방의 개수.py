# https://programmers.co.kr/learn/courses/30/lessons/49190
"""
간선의 개수와, 간선들이 지나는 격자점의 개수 세주기
오일러의 정리: v - e + f = 1
-> 방의 개수 = 간선의 개수 - 격자점의 개수 + 1

파이썬 집합: add 시간복잡도 O(1)
간선 집합에 들어가는 정보
(x 출발, y 출발, x 도착, y 도착)이랑 (x 도착, y 도착, x 출발, y 출발)

꼭짓점 집합에 들어가는 정보
(x+a,y+b), (x+2a,y+2b)

한번에 거리 1말고 2씩 증가하게 하면
X자로 교차하는 것들도 꼭짓점으로 들어가지므로 예외 쉽게 처리 가능

간선도 두배로 늘어나지만 양쪽 방향을 둘다 넣으니까 그냥 길이 2짜리로 넣어주면 됨
"""

def solution(arrows):
    x = 0; y = 0 # 현재 좌표
    edge = set(); node = set([(0,0)]) # 간선 저장할 집합, 꼭짓점 저장할 집합
    # x: 0,1,7: 증가, 2,6: 유지, 3,4,5: 감소
    # y: 1,2,3: 증가, 0,4: 유지, 5,6,7: 감소
    
    for i in arrows:
        a = (int((i+1) % 8 < 3) - int(3 < (i+1) % 8 < 7))
        b = (int(0 < i < 4) - int(4 < i))
        
        # 집합에 꼭짓점 추가
        node.update([(x+a,y+b), (x+a*2,y+b*2)])
        # 집합에 간선 추가
        edge.update([(x,y,x+a*2,y+b*2),(x+a*2,y+b*2,x,y)])
        x += a*2; y += b*2
    
    return len(edge) - len(node) + 1

arrows = [6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]
print(solution(arrows))
