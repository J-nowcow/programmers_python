#https://programmers.co.kr/learn/courses/30/lessons/43236
"""
바위 5만개, distance 10억 이하
바위 중에 적당히 n개를 제거했을 때, minmax(바위 사이 거리의 최소의 최대) 구하기
일단 정렬해놓고
이진 탐색으로 distance 설정해 둔 뒤 그 거리를 만족시킬 수 있는지 탐색하자
찾는건 그리디로 해주면 될 듯
"""

def solution(distance, rocks, n):
    rocks.sort()
    
    begin = 0; end = distance # 가능한 거리 최댓값 10^9
    while begin <= end:
        mid = (begin+end) // 2 # mid : 돌 사이의 최소 거리
        dummy = 0 # 버릴 돌의 개수
        pos = 0 # 현재 가장 오른쪽 돌이 있는 위치
        for i in rocks:
            if i - pos < mid:
                dummy += 1 # 최소 거리보다 작은 위치면 버려줘야함
            else:
                pos = i # 아니면 가져가고 돌의 위치 바꿔주기
                
        if distance - pos < mid: # 마지막 돌이랑 도착 지점 사이 거리 체
            dummy += 1
            
        if dummy <= n: # 버리는 돌의 수가 n 이하면 가능한 경우임
            begin = mid + 1
        else: # 아니면 불가능한 경우니까 end 당겨오기
            end = mid - 1

    return end


distance = 25
rocks = [2, 14, 11, 21, 17]
n = 2
print(solution(distance, rocks, n))
